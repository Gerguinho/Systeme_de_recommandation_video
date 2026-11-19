# Projet de recommandation vidéo : livraison du prototype

## Commencer
1. Ouvrir Projet_recommandation_video_complet.ipynb dans Jupyter. Les résultats et graphiques sont déjà enregistrés : on peut les lire sans recalculer.
2. Pour recalculer, placer small_matrix.csv à côté du notebook. Il provient du jeu de données public KuaiRec et n’est pas inclus dans le dépôt (400 Mo).
3. Installer les dépendances si nécessaire : `python -m pip install -r requirements.txt`.
4. Redémarrer le noyau puis exécuter toutes les cellules. Le dossier resultats_recommandation est régénéré et ses fichiers homonymes sont remplacés. Faire une copie des anciens résultats avant une nouvelle expérience.
5. Le notebook cherche le CSV dans cet ordre : variable d’environnement `RECO_CSV`, dossier du notebook, puis `data/` à la racine du dépôt. Exemple sous Windows : `set RECO_CSV=D:\chemin\vers\small_matrix.csv` avant de lancer Jupyter.

Le notebook conserve les commentaires pédagogiques, les hypothèses, les limites et les conclusions fondées sur les sorties. Ce n'est pas un simple script à exécuter sans lecture. Commencer par les sections 1 et 2, puis lire les définitions des métriques.

## Contenu
- Notebook exécuté : audit, graphiques, baselines, SVD collaborative, hybride, validation/test et cold start utilisateur.
- resultats_recommandation/*.csv : données de qualité et résultats détaillés.
- partitions.npz : masques des mêmes partitions à réutiliser, IDs utilisateurs et vidéos.
- modele_demo.npz : scores du modèle sélectionné et historique d'entraînement nécessaire au filtrage ; ne pas publier ces données comme une API ouverte.
- manifest.json : paramètres, versions de l'exécution, empreinte SHA-256 du CSV et modèle choisi.
- api_demo.py : API locale à lancer séparément.
- tests.json : périmètre exact des tests exécutés.
- conclusions.md : synthèse des observations et des limites.

## API locale
Dans le dossier extrait :
`python resultats_recommandation/api_demo.py`

Ouvrir : `http://127.0.0.1:8000/recommendations?user_id=14&k=10`
Autres routes : `/health` et `/recommendations?user_id=14&k=10&seen=183,148`.
Arrêt : Ctrl+C. L'API retourne au plus k vidéos, accompagnées du nombre réellement retourné.

Les tests ont vérifié la fonction, l'export/rechargement et les routes hors réseau. Le transport HTTP réel et la charge ne sont pas certifiés par cette livraison. L'API utilise uniquement la bibliothèque standard et NumPy, pas FastAPI.

## Ce qui n'est pas prétendu
- Pas de plateforme vidéo complète ni de déploiement en production.
- Pas de modèle basé contenu ou de cold start vidéo (métadonnées absentes).
- Pas de garantie de gain par rapport à la popularité lissée : le test ne montre pas d'avantage NDCG établi pour l'hybride.
- Pas de comparaison directe avec l'ancien score 0,417, car le protocole a changé.
- Pas d'audit de conformité ou de sécurité de production.

## Reproductibilité
L'évaluation couvre tous les utilisateurs du CSV valide. Les hyperparamètres sont sélectionnés sur validation ; le test est utilisé pour le bilan. Une graine fixe génère des graines distinctes pour chaque utilisateur. Les différences de versions et de bibliothèques numériques peuvent produire de petites variations : le manifeste enregistre l'environnement d'exécution.
Les durées d'entraînement affichées sont propres à la machine d'exécution et ne constituent pas des tests de performance de l'API.

## Suite de stage
Comprendre et vérifier chaque partie ; adapter les données et l'API à la future application avec l'entreprise ; définir le contrat de données, le catalogue actif et la protection des historiques ; réaliser une nouvelle validation avant production. L'entreprise doit valider les hypothèses métier.
