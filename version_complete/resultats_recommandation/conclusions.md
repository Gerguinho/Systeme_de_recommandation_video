## Lecture critique des résultats de cette exécution

### Données : ce qui est établi
- Les **4 676 570 lignes** ont été contrôlées ; aucun couple utilisateur-vidéo répété, aucune durée invalide et aucune valeur essentielle manquante n'ont été détectés.
- **181 992 lignes (3,89157 %) manquent dans chacune des colonnes temporelles**. Ce constat porte sur tout le fichier, pas sur l'extrait initial à 3,79 %.
- Six ratios présentent un écart absolu supérieur à 0,001 avec le calcul durée regardée / durée vidéo. Ils sont affichés dans l'audit ; le ratio source est conservé. Il faut documenter cette différence, pas affirmer que toutes les valeurs sont exactement identiques.
- La matrice observée est dense à **99,6202 %**. Cette propriété facilite les évaluations sur réponses connues, mais ne supprime pas les biais du jeu de données.

### Modèles : le résultat important n'est pas seulement le score le plus élevé
Le meilleur rang collaboratif sur validation est **16**. Le poids hybride retenu est **25 % de rang collaboratif et 75 % de rang de popularité**. Ce poids porte sur les rangs percentiles, pas directement sur des probabilités.

Le candidat retenu sur validation, **Hybride_0.25**, obtient sur le test :
- Precision@10 : **0.9022** ;
- NDCG@10 : **0.9081** ;
- couverture du catalogue : **7.66%**.

La baseline **Taux_lisse** atteint une Precision@10 de **0.9027**, une NDCG@10 de **0.9097** et une couverture de **2.98%**. L'hybride ne démontre donc **pas un gain de précision ou de NDCG** face à cette référence. Sa différence NDCG vaut -0.0016, avec IC bootstrap 95 % [-0.0056 ; +0.0022], qui recouvre zéro. Cela n'établit pas non plus une équivalence statistique.

En revanche, sa couverture est plus élevée dans cette expérience. C'est un compromis à discuter avec l'entreprise, **pas une mesure de diversité sémantique**. Le collaboratif seul couvre encore davantage de vidéos, mais perd en pertinence moyenne dans ce protocole. Il serait incorrect d'en conclure que tout filtrage collaboratif est inférieur : un seul modèle pédagogique et une grille limitée ont été testés.

### Pourquoi les scores semblent élevés
La pertinence est définie par un signal indirect relativement fréquent. Parmi plusieurs centaines de candidats observés, une méthode peut choisir dix vidéos généralement bien regardées. Un score d'environ 0,90 ne signifie donc ni 90 % de satisfaction réelle, ni 90 % de réussite sur tous les utilisateurs futurs.

L'ancien **0,417 n'est pas une référence directement comparable** : il concernait 100 utilisateurs, un entraînement sur 80 % et des candidats différents. Ici, les 1 411 utilisateurs sont évalués avec des partitions 60/20/20 et des candidats observés. Ce notebook ne revendique pas un passage de 41,7 % à 90 % à protocole constant.

Le rappel est faible malgré une précision élevée : les utilisateurs ont beaucoup plus de dix positifs dans leurs candidats. Retrouver dix éléments ne couvre qu'une petite partie de ces positifs. Ce n'est pas une contradiction ; précision et rappel répondent à des questions différentes.

### Décision et prochaine étape scientifique
Conserver le candidat choisi sur validation comme démonstrateur, et la popularité lissée comme référence forte. Ne pas changer de gagnant après consultation du test. Avant toute revendication produit, tester d'autres découpages, une validation temporelle adaptée aux dates manquantes, puis les données de l'entreprise. La stratégie de cold start utilisateur est un repli non personnalisé ; le cold start vidéo reste non évalué faute de métadonnées.
