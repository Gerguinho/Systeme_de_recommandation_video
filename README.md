# Système de recommandation vidéo (KuaiRec)

Prototype de moteur de recommandation vidéo réalisé pendant mon stage de S7. À partir de 4,7 millions d'interactions utilisateur–vidéo du jeu de données public [KuaiRec](https://kuairec.com/), il propose à chaque utilisateur une liste de 10 vidéos. Il compare plusieurs modèles avec un protocole d'évaluation fixé à l'avance.

**Stack :** Python · pandas · NumPy · SciPy · scikit-learn (SVD) · matplotlib · Jupyter

## Démarche

1. **Audit des données** : types, valeurs manquantes, doublons, valeurs aberrantes (`watch_ratio > 1`), densité de la matrice, empreinte SHA-256 du CSV.
2. **Protocole d'évaluation** : découpage 60 / 20 / 20 par utilisateur (entraînement / validation / test). Une vidéo est jugée pertinente si `watch_ratio ≥ 0,8`. Métriques : Precision@10, Recall@10, NDCG@10 et couverture du catalogue.
3. **Références (baselines)** : aléatoire, popularité brute, popularité des vidéos pertinentes, taux de visionnage lissé.
4. **Filtrage collaboratif** : factorisation SVD des préférences résiduelles (rangs 16, 32 et 64).
5. **Modèle hybride** : mélange pondéré entre la SVD et la popularité (α de 0 à 1), avec α choisi sur la validation.
6. **Bilan sur le test réservé** : le test n'est consulté qu'une fois le modèle choisi. Intervalle de confiance bootstrap sur l'écart de NDCG et analyse de sensibilité au seuil de pertinence.
7. **Cold start** : repli sur la popularité pour les utilisateurs sans historique.
8. **Mise à disposition** : export du modèle et API HTTP locale (`/health`, `/recommendations`).

## Résultats (test, 1 411 utilisateurs, 3 327 vidéos)

| Modèle | Precision@10 | NDCG@10 | Couverture du catalogue |
|---|---:|---:|---:|
| Aléatoire | 0,475 | 0,470 | 98,4 % |
| Popularité (nb d'interactions) | 0,455 | 0,435 | 3,3 % |
| Taux de visionnage lissé (référence) | 0,903 | 0,910 | 3,0 % |
| SVD rang 16 | 0,871 | 0,875 | 49,2 % |
| **Hybride α = 0,25 (retenu)** | **0,902** | **0,908** | **7,7 %** |

**Lecture critique :** l'hybride a une précision équivalente à la meilleure référence et couvre **2,5 fois plus de catalogue**. En revanche, son écart de NDCG avec la référence n'est pas significatif (IC 95 % : [−0,0056 ; +0,0022]). Les scores élevés s'expliquent par le protocole : le classement se fait parmi les vidéos que chaque utilisateur a réellement vues, et une vidéo bien regardée est un cas fréquent. Pour les nouveaux utilisateurs, le repli sur la popularité obtient une Precision@10 de 0,91.

## Organisation du dépôt

```
version_complete/        Notebook principal (29 cellules, exécuté) + résultats + API
version_pedagogique/     Même expérience, expliquée pas à pas (96 cellules, calculs à la main)
notebooks/               Première exploration (baseline par popularité)
requirements.txt
```

Les deux versions donnent les mêmes résultats (voir `version_pedagogique/Comparaison_des_executions.md`).

## Lancer le projet

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

Les notebooks sont enregistrés avec leurs sorties : on peut les lire sans rien exécuter. Pour refaire l'expérience, téléchargez KuaiRec 2.0, puis placez `small_matrix.csv` dans `data/` ou indiquez son chemin avec la variable d'environnement `RECO_CSV`.

**API de démonstration** (une fois le notebook exécuté, ce qui génère `modele_demo.npz`) :

```bash
cd version_complete
python resultats_recommandation/api_demo.py
```

Puis ouvrez `http://127.0.0.1:8000/recommendations?user_id=14&k=10`.

## Limites

- Évaluation hors ligne uniquement : aucun test A/B, aucun gain métier mesuré.
- Pas de métadonnées vidéo, donc pas de modèle basé sur le contenu ni de cold start vidéo.
- L'API est une démonstration locale : elle n'est pas prévue pour être exposée sur Internet.

## Auteur

Bryan Hounang Petcheu · [GitHub](https://github.com/Gerguinho)
