# Prototype pédagogique de recommandation vidéo

## Lire le notebook
Ouvrir Recommandation_video_pedagogique.ipynb dans Jupyter ou VS Code. Les sorties enregistrées permettent de lire les calculs, les tableaux et les figures sans nouvelle exécution. La section 5 présente un exemple de calcul à la main. La section 10 explique la liste recommandée et la section 11 propose la démonstration.

## Refaire l’expérience
Utiliser un environnement Python avec les dépendances de requirements.txt. Au besoin, lancer `python -m pip install -r requirements.txt`. Pour ouvrir Jupyter, lancer `python -m jupyterlab` depuis ce dossier. Le notebook cherche small_matrix.csv via la variable RECO_CSV, puis dans le dossier du notebook, puis dans data/ à la racine du dépôt. Le jeu de données reste dans son emplacement d’origine.

Redémarrer le noyau et exécuter les cellules dans l’ordre. L’exécution écrit les sorties dans resultats_pedagogiques et y remplace les fichiers du même nom. Les paramètres de l’expérience et l’empreinte du CSV figurent dans resultats_pedagogiques/manifest.json. La comparaison avec l’archive et avec le notebook d’origine réexécuté figure dans Comparaison_des_executions.md.

## Démonstration locale
Le modèle est déjà exporté. Depuis ce dossier, avec Python et NumPy installés, lancer :

    python resultats_pedagogiques/api_demo.py

Dans le navigateur, ouvrir http://127.0.0.1:8000/health ou http://127.0.0.1:8000/recommendations?user_id=14&k=10. L’option seen accepte des IDs vidéo séparés par des virgules. Ctrl+C arrête le serveur dans le terminal. Les tests enregistrés vérifient les réponses des routes par appel direct.

## Résultats
Les tableaux CSV contiennent les résultats complets avant arrondi. partitions.npz contient les trois masques et les identifiants. modele_demo.npz contient les scores, le catalogue et l’historique nécessaires au service. tests.json récapitule les contrôles et conclusions.md reprend les chiffres recalculés.
