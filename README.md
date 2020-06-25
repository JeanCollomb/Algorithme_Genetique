[![DOI](https://zenodo.org/badge/140018461.svg)](https://zenodo.org/badge/latestdoi/140018461)


# Algorithme_Genetique

« Les algorithmes génétiques appartiennent à la famille des algorithmes évolutionnistes. 
Leur but est d'obtenir une solution approchée à un problème d'optimisation, 
lorsqu'il n'existe pas de méthode exacte (ou que la solution est inconnue) pour le résoudre en un temps raisonnable. 
Les algorithmes génétiques utilisent la notion de sélection naturelle et l'appliquent à une population de 
solutions potentielles au problème donné. La solution est approchée par « bonds » successifs, 
comme dans une procédure de séparation et évaluation, à ceci près que ce sont des formules qui sont recherchées 
et non plus directement des valeurs. » 
[Wikipédia – Algorithme génétique](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique)

Ce script python ce propose de faire se travail.


## Pour commencer

Récupérer les fichiers :
- main_exemple.py
- class_ga.py


```
Pré-requis :
- Posséder les packages : numpy, pickle, os, random, tqdm
```


## Fonctionnement

La démarche de fonctionnement classique d'un algorithme génétique est la suivante :
* Evaluation de la fonction objective pour chaque individu de la population N
* Sélection
* Croisement
* Mutation
* Création d'une nouvelle population N+1
Répétition de chacun de ces étapes jusqu'à convergence.

```
A noter :
Pour les étapes de sélection, croisement et mutation, différentes méthodes existes. 
```

## Tâches réalisées

* Génération de la population initiale
* Fonction de sélection par ellitisme
* Fonction de sélection par duel/tournoi
* Fonction de croisement uniforme
* Fonction de mutation uniforme


## Tâches à faire
* Sélection par : roulette, reste stochastique, rang, échantillonage stochastique universel
* Croisement : arithmétiques et géométriques, SBX,à 1 point ou multi-points
* Mutation non-uniforme
* Gestion des contraintes par : réparation, pénalisation, modification
* Scaling
* Niching
* Critère de convergence
* Export graphique
