import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
import numpy as np


def indexer_utilisateurs(identifiants):
    positions = {}
    for position, identifiant in enumerate(identifiants):
        positions[int(identifiant)] = position
    return positions


def choisir_videos(catalogue, scores, historique, deja_vues, k):
    disponible = np.ones(len(catalogue), dtype=bool)
    if historique is not None:
        disponible = ~historique.copy()
    if deja_vues is not None:
        signalees = np.isin(catalogue, list(deja_vues))
        disponible &= ~signalees
    candidats = np.flatnonzero(disponible)
    ordre = np.lexsort((catalogue[candidats], -scores[candidats]))
    choix = candidats[ordre[:k]]
    return catalogue[choix].astype(int).tolist()


def construire_reponse(user_id, videos, mode):
    return {"user_id": int(user_id), "mode": mode, "video_ids": videos, "nombre_retourne": len(videos)}


class Recommender:
    def __init__(self, path=None):
        if path is None:
            path = Path(__file__).resolve().parent / "modele_demo.npz"
        with np.load(path, allow_pickle=False) as donnees_modele:
            self.users = donnees_modele["users"]
            self.items = donnees_modele["items"]
            self.scores = donnees_modele["scores"]
            self.seen = donnees_modele["seen"]
            self.pop = donnees_modele["popularity"]
        self.lookup = indexer_utilisateurs(self.users)

    def recommend(self, user_id, k=10, seen=()):
        if not 1 <= k <= 100:
            raise ValueError("k doit être entre 1 et 100")
        position = self.lookup.get(int(user_id))
        if position is None:
            scores, historique, mode = self.pop, None, "repli_popularite"
        else:
            scores, historique, mode = self.scores[position], self.seen[position], "modele_selectionne"
        videos = choisir_videos(self.items, scores, historique, seen, k)
        return construire_reponse(user_id, videos, mode)


def traiter(path, service):
    adresse = urlparse(path)
    if adresse.path == "/health":
        return 200, {"status": "ok"}
    if adresse.path != "/recommendations":
        return 404, {"error": "Route inconnue"}
    try:
        parametres = parse_qs(adresse.query)
        utilisateur = int(parametres["user_id"][0])
        longueur = int(parametres.get("k", ["10"])[0])
        valeurs_vues = parametres.get("seen", [""])[0].split(",")
        deja_vues = [int(valeur) for valeur in valeurs_vues if valeur]
        return 200, service.recommend(utilisateur, longueur, deja_vues)
    except (KeyError, ValueError, TypeError):
        return 400, {"error": "Paramètres invalides : user_id entier, k entre 1 et 100, seen IDs séparés par virgules"}



def lancer_serveur():
    service = Recommender()

    class Gestionnaire(BaseHTTPRequestHandler):
        def do_GET(self):
            statut, reponse = traiter(self.path, service)
            contenu = json.dumps(reponse, ensure_ascii=False).encode("utf-8")
            self.send_response(statut)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(contenu)))
            self.end_headers()
            self.wfile.write(contenu)

    with ThreadingHTTPServer(("127.0.0.1", 8000), Gestionnaire) as serveur:
        print("API locale sur http://127.0.0.1:8000 · arrêt avec Ctrl+C")
        try:
            serveur.serve_forever()
        except KeyboardInterrupt:
            pass



if __name__ == "__main__":
    lancer_serveur()
