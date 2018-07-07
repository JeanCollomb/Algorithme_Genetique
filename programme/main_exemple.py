# -*- coding: utf-8 -*-
"""
Exemple

@author: Jean Collomb
"""

###############################################################################
###----> Importation packages

from class_ga import Algorithme_Genetique


###############################################################################
###----> Parametres

nombre_individus         = 20
nombre_generation        = 10
probabilite_mutation     = 0.05
probabilite_croisement   = 0.25
probabilite_ellitisme    = 0.1

parametres_discrets      = [['eau', 'huile'], ['acier', 'aluminium', 'cuivre']]
parametres_continus      = [[1, 10], [0, 100], [0.3, 0.8]]

nombre_fonctions         = 1

parametres_algorithme    = [nombre_individus, 
                            nombre_generation, 
                            probabilite_mutation, 
                            probabilite_croisement, 
                            probabilite_ellitisme]

parametres_produit       = [parametres_discrets, 
                            parametres_continus, 
                            nombre_fonctions]

###############################################################################
###----> Initialisation

exemple = Algorithme_Genetique(parametres_algorithme, parametres_produit)

###############################################################################
###----> Population initiale

exemple.fct_initialisation_population()
a = exemple.population_generation
b = exemple.population_generation_old

exemple.fct_croisement()
c = exemple.population_generation

#exemple.fct_optimisation_simple()

#exemple.fct_mutation()
#b = exemple.population_generation

###############################################################################
###############################################################################
###############################################################################