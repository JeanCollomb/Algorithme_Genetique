# -*- coding: utf-8 -*-
"""
Class

@author: Jean Collomb
"""

###############################################################################
###----> Importation packages

from numpy import array, zeros
from random import uniform, randint, choice


###############################################################################

class Algorithme_Genetique () :
    '''
    '''
    
    ###---------------------------------------------------------------------###
    def __init__ (self, parametres_algorithme, parametres_produit) :
        '''
        '''
        self.nombre_individus         = parametres_algorithme[0]
        self.nombre_generation        = parametres_algorithme[1]
        self.probabilite_mutation     = parametres_algorithme[2]
        self.probabilite_croisement   = parametres_algorithme[3]
        self.probabilite_ellitisme    = parametres_algorithme[4]
        
        self.parametres_discrets      = parametres_produit[0]
        self.parametres_continus      = parametres_produit[1]
        self.nombre_fonction          = parametres_produit[2]
        
        self.population_initiale     = zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        self.population_generation_old= zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        self.population_generation    = zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        self.nombre_individus_mutation= int(round(self.nombre_individus * self.probabilite_mutation,0))
        self.nombre_individus_croisement= int(round(self.nombre_individus * self.probabilite_croisement,0))
        self.nombre_individus_ellistisme= int(round(self.nombre_individus * self.probabilite_ellitisme,0))
    
    ###---------------------------------------------------------------------###
    def fct_initialisation_population (self) :
        '''
        Fonction permettant la création d'un attribut 'population initiale' 
        de manière aléatoire en fonction des paramètres variables saisis par
        l'utilisateur.
        '''
        
        for individu in range(self.nombre_individus):
            
            for discret in range(len(self.parametres_discrets)):
                self.population_initiale[individu][discret] = randint(0, len(self.parametres_discrets[discret]) - 1)
            
            for continu in range(len(self.parametres_continus)):
                self.population_initiale[individu][len(self.parametres_discrets) + continu] = uniform(self.parametres_continus[continu][0], self.parametres_continus[continu][1])
        
        self.population_generation_old = self.population_initiale
        
    ###---------------------------------------------------------------------###
    def fct_mutation (self) :
        '''
        Fonction permettant de creer des individus mutes de manière aléatoire 
        dans la nouvelle génération.
        '''
        
        for individu in range(len(self.population_generation)):
            
            for discret in range(len(self.parametres_discrets)):
                test_proba = randint(0, 100)
                if test_proba <= self.probabilite_mutation :
                    self.population_generation[individu][discret] = randint(0, len(self.parametres_discrets[discret]) - 1)
                
            for continu in range(len(self.parametres_continus)):
                test_proba = randint(0, 100)
                if test_proba <= self.probabilite_mutation :
                    self.population_generation[individu][len(self.parametres_discrets) + continu] = uniform(self.parametres_continus[continu][0], self.parametres_continus[continu][1])
            
    def fct_croisement (self) :
        '''
        '''
        
        pass
    
    def fct_selection_ellistisme (self) :
        '''
        '''
        
        pass
    
    def fct_selection_duel (self) :
        '''
        '''
        
        pass








###############################################################################
###############################################################################
###############################################################################