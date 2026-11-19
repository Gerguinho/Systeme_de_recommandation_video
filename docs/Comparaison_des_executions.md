# Vérification de la copie pédagogique

Les résultats de la copie proviennent d’une exécution complète de ses cellules, dans l’ordre, avec le CSV fourni. Deux références sont utilisées : les fichiers enregistrés dans le ZIP d’origine et une nouvelle exécution du code du notebook d’origine sur cette machine.

## Environnement

Les 46 cellules de code de la copie ont été exécutées successivement dans un processus Python neuf. Les sorties texte, tableaux et graphiques ont été enregistrés dans le notebook. Le démarrage du noyau Jupyter par connexion locale est resté bloqué dans cet environnement. La réexécution du notebook d’origine a utilisé le même mode d’exécution et les mêmes bibliothèques.

- Archive — python 3.12.15, pandas 3.0.3, numpy 2.4.6, scipy 1.18.0, scikit-learn 1.9.0.
- Réexécution — python 3.14.7, pandas 3.1.1, numpy 2.5.4, scipy 1.18.1, scikit-learn 1.9.1.

SHA-256 du CSV : `6b601cd38b2600d8734b4aede309ad73d1e201fdc4bd76d4bc7d2534793d7d15`.

## Comparaison avec les résultats archivés

Manifeste hors versions : valeurs identiques.
Statuts des tests de fonction, d’export et de routes hors réseau identiques.

| Fichier de résultats | Lignes | Valeurs numériques différentes | Écart absolu maximum |
|---|---:|---:|---:|
| cold_start_utilisateur.csv | 2 | 0 | 0 |
| incertitude.csv | 2 | 6 | 6.087180613e-05 |
| qualite.csv | 8 | 0 | 0 |
| sensibilite.csv | 9 | 3 | 1.384561586e-05 |
| test_comparaison.csv | 6 | 4 | 7.087172218e-05 |
| test_par_utilisateur.csv | 8466 | 9 | 0.1 |
| validation.csv | 12 | 2 | 3.567928334e-06 |

Les lignes et colonnes sont comparées dans leur ordre d’écriture, avant arrondi des résultats.

- Partitions et identifiants : tableaux identiques case par case.
- Scores exportés : 152723 valeurs différentes sur 4694397. Écart absolu maximal 0.000375717878.
- Historique, catalogue et scores de popularité de repli : tableaux identiques.
- Listes de dix en démonstration, sans exclusions supplémentaires : 1399/1411 identiques dans le même ordre. Nombre de listes dont le contenu diffère : 1.

## Comparaison avec le code d’origine réexécuté sur cette machine

Manifeste hors versions : valeurs identiques.
Statuts des tests de fonction, d’export et de routes hors réseau identiques.

| Fichier de résultats | Lignes | Valeurs numériques différentes | Écart absolu maximum |
|---|---:|---:|---:|
| cold_start_utilisateur.csv | 2 | 0 | 0 |
| incertitude.csv | 2 | 0 | 0 |
| qualite.csv | 8 | 0 | 0 |
| sensibilite.csv | 9 | 0 | 0 |
| test_comparaison.csv | 6 | 0 | 0 |
| test_par_utilisateur.csv | 8466 | 0 | 0 |
| validation.csv | 12 | 0 | 0 |

Les lignes et colonnes sont comparées dans leur ordre d’écriture, avant arrondi des résultats.

- Partitions et identifiants : tableaux identiques case par case.
- Scores exportés : 0 valeurs différentes sur 4694397. Écart absolu maximal 0.
- Historique, catalogue et scores de popularité de repli : tableaux identiques.
- Listes de dix en démonstration, sans exclusions supplémentaires : 1411/1411 identiques dans le même ordre. Nombre de listes dont le contenu diffère : 0.

## Portée

Les contrôles de l’API portent sur le calcul et le routage par appel direct. Le transport HTTP, la tenue en charge et l’intégration avec la plateforme de l’entreprise restent à évaluer.
