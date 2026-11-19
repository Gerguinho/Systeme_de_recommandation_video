# Système de recommandation vidéo — Stage technique S7

Moteur de recommandation de vidéos courtes construit sur le jeu de données KuaiRec 2.0 (`small_matrix.csv`). Le projet compare des recommandations par popularité, un filtrage collaboratif (SVD) et une approche hybride, puis sert le modèle retenu par une API locale.

## Organisation du dossier

| Élément | Contenu |
|---|---|
| `Systeme_recommandation_video.ipynb` | Notebook principal : données, protocole, modèles, évaluation, API |
| `donnees/` | `small_matrix.csv` (interactions) et `item_categories.csv` (catégories des vidéos) |
| `resultats/` | Sorties du notebook : tableaux CSV, modèle exporté, `api_demo.py` |
| `docs/` | Documentation : comparaison des exécutions, puis rapport de stage |
| `archives/` | Version d'origine du prototype (15/11/2026), à ne pas modifier |
| `requirements.txt` | Bibliothèques Python nécessaires |
| `.venv/`, `.idea/` | Environnement Python et configuration IntelliJ (générés, ne pas éditer) |

## Lire le notebook
Ouvrir le dossier dans IntelliJ IDEA, puis `Systeme_recommandation_video.ipynb`. Les sorties enregistrées permettent de lire les calculs, les tableaux et les figures sans nouvelle exécution. La section 5 présente un exemple de calcul à la main, la section 10 explique la liste recommandée et la section 11 propose la démonstration.

## Refaire l'expérience
L'environnement `.venv` contient déjà les dépendances. Pour le recréer : `python -m venv .venv` puis `.venv\Scripts\python -m pip install -r requirements.txt`.

Redémarrer le noyau et exécuter les cellules dans l'ordre, depuis le dossier du projet. Le notebook lit `donnees/small_matrix.csv` et écrit ses sorties dans `resultats/`, en remplaçant les fichiers du même nom. Les paramètres de l'expérience et l'empreinte SHA-256 du CSV figurent dans `resultats/manifest.json`. La comparaison avec l'archive et avec le notebook d'origine réexécuté figure dans `docs/Comparaison_des_executions.md`.

## Démonstration locale
Le modèle est déjà exporté. Depuis le dossier du projet, lancer :

    .venv\Scripts\python resultats\api_demo.py

Dans le navigateur, ouvrir http://127.0.0.1:8000/health ou http://127.0.0.1:8000/recommendations?user_id=14&k=10. L'option `seen` accepte des IDs vidéo séparés par des virgules. Ctrl+C arrête le serveur.

## Résultats
Les tableaux CSV de `resultats/` contiennent les résultats complets avant arrondi. `partitions.npz` contient les trois masques et les identifiants. `modele_demo.npz` contient les scores, le catalogue et l'historique nécessaires au service. `tests.json` récapitule les contrôles et `conclusions.md` reprend les chiffres recalculés.

## Source des données
KuaiRec 2.0 — copie d'origine dans `D:\Etudes\Stage_data_KuaiRec\KuaiRec\KuaiRec 2.0\data\`.
