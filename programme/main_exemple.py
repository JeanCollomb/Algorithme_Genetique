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

nombre_individus         = 150
nombre_generation        = 500
probabilite_mutation     = 0.05
probabilite_croisement   = 0.25
probabilite_ellitisme    = 0.1

parametres_discrets      = [['acier', 'aluminium', 'cuivre']]
parametres_continus      = [[5, 30], [5, 50]]

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

#exemple.fct_initialisation_population()
#a = exemple.population_generation.copy()
#b = exemple.population_generation_old.copy()

#exemple.fct_croisement()
#exemple.fct_selection_ellistisme()
#c = exemple.population_generation.copy()

exemple.fct_optimisation_simple()
#a = exemple.fct_lecture_sauvegarde()
#b = exemple.population_generation_old.copy()


#
#exemple.fct_initialisation_population()
#exemple.fct_lecture_sauvegarde()
#a = exemple.population_generation_old.copy()
#
#
#
#
#exemple.fct_selection_ellistisme()
#b = exemple.population_generation.copy()
#exemple.fct_croisement()
#c = exemple.population_generation.copy()
#exemple.fct_selection_duel()
#d = exemple.population_generation.copy()
#exemple.fct_mutation()
#e = exemple.population_generation.copy()
#exemple.fct_fonction_objective()
#exemple.fct_tri()
#f = exemple.population_generation_old.copy()
#
#
#
#exemple.fct_sauvegarde_generation()
#g = exemple.fct_lecture_sauvegarde()
#h = exemple.population_generation_old.copy()


###############################################################################
###############################################################################
###############################################################################