# -*- coding: utf-8 -*-
"""
Class

@author: Jean Collomb
"""

###############################################################################
###----> Importation packages

from numpy import array, zeros, savetxt
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
    ###--------------> Fonctions objective et contraintes
    def fct_fonction_objective (self):
        '''
        '''
        
        #--- Exemple
        for individu in range(self.nombre_individus):
            self.population_generation[individu][-1] = self.population_generation[individu][2] * self.population_generation[individu][3] * self.population_generation[individu][4]
        
        #--- Ne pas modifier
        self.population_generation_old = array(sorted(self.population_generation.tolist(), key = lambda x: x[-1], reverse = True))
    
    
    ###---------------------------------------------------------------------###
    ###--------------> Creation de la population initiale
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
        
        self.population_generation = self.population_initiale
        self.fct_fonction_objective()
        
    ###---------------------------------------------------------------------###
    ###--------------> Fonction de croisement, selection et mutation
    def fct_sauvegarde_generation (self, chemin = None):
        '''
        Fonction permettant la sauvegarde de la generation."
        '''
        self.population_generation_old = self.population_generation
        fichier_export = open('generations.ppj', 'ab')
        savetxt(fichier_export, self.population_generation_old, delimiter = '   ')
        fichier_export.close()
        
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
        Fonction permettant de creer des individus croises de manière aléatoire
        dans la nouvelle génération.
        '''
        
        for individu in range(self.nombre_individus_croisement):
            id_pere = randint(0, self.nombre_individus-1)
            id_mere = randint(0, self.nombre_individus-1)
            
            for discret in range(len(self.parametres_discrets)):
                self.population_generation[individu][discret] = choice([self.population_generation_old[id_pere][discret], self.population_generation_old[id_mere][discret]])
            
            for continu in range(len(self.parametres_continus)):
                self.population_generation[individu][len(self.parametres_discrets) + continu] = choice([self.population_generation_old[id_pere][len(self.parametres_discrets) + continu], self.population_generation_old[id_mere][len(self.parametres_discrets) + continu]])
    
    def fct_selection_ellistisme (self) :
        '''
        '''
        
        pass
    
    def fct_selection_duel (self) :
        '''
        Fonction permettant de confronter deux individus aléatoire et de
        sélectionner le meilleur pour la génération suivante.
        '''
        
        pass

    ###---------------------------------------------------------------------###
    ###--------------> Optimisaton simple - boucle sur les générations
    def fct_optimisation_simple (self) :
        '''
        '''
        
        for generation in range(self.nombre_generation) :
            self.fct_croisement()
            self.fct_selection_ellistisme()
            self.fct_selection_duel
            self.fct_mutation()
            self.fct_sauvegarde_generation()
        
    
    
    ###---------------------------------------------------------------------###
    ###--------------> Multi-optimisation - Variation des donnees de l'algorithme






###############################################################################
###############################################################################
###############################################################################