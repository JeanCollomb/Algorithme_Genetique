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

nombre_individus         = 10
nombre_generation        = 20

parametres_discrets      = [['eau', 'huile'], ['acier', 'aluminium', 'cuivre']]
parametres_continus      = [[1, 10], [0, 100], [0.3, 0.8]]

nombre_fonctions         = 1

parametres_algorithme    = [nombre_individus, nombre_generation]
parametres_produit       = [parametres_discrets, parametres_continus, nombre_fonctions]

###############################################################################
###----> Initialisation

exemple = Algorithme_Genetique(parametres_algorithme, parametres_produit)

###############################################################################
###----> Population initiale



###############################################################################
###############################################################################
###############################################################################