# -*- coding: utf-8 -*-
"""
Class

@author: Jean Collomb
"""

###############################################################################
###----> Importation packages

from numpy import array, zeros, concatenate
from random import uniform, randint, choice
from pickle import dump as dp
from pickle import load as ld
from os import getcwd, mkdir


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
        self.nombre_individus_duel      = self.nombre_individus - (self.nombre_individus_ellistisme + self.nombre_individus_croisement)
        
        self.dossier_travail            = getcwd()
        self.dossier_sauvegarde         = self.dossier_travail + str('\sauvegarde')
    
    ###---------------------------------------------------------------------###
    ###--------------> Fonctions objective et contraintes
    def fct_fonction_objective (self):
        '''
        '''
        
        #--- Exemple : FL3/48EI
        F = 700
        L = 850
        
        for individu in range(self.nombre_individus):
            
            if self.population_generation[individu][0] == 0:
                E = 210000
            elif self.population_generation[individu][0] == 1:
                E = 70000
            else:
                E = 150000
            
            I = (self.population_generation[individu][1]*self.population_generation[individu][2]**3)/12
            self.population_generation[individu][-1] = (F*L**3)/(48*E*I)
             
    
    ###---------------------------------------------------------------------###
    ###--------------> Creation de la population initiale
    def fct_tri(self) :
        '''
        Fonction permettant de trier les individus en fonction de la fonction
        objective
        '''
        self.population_generation_old = array(sorted(self.population_generation.tolist(), key = lambda x: x[-1], reverse = False)).copy()
    
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
        
        self.population_generation = self.population_initiale.copy()
        self.fct_fonction_objective()
        try:
            mkdir(self.dossier_sauvegarde)
        except:
            pass
        self.fct_tri()
        
        with open(self.dossier_sauvegarde + str('\sauvegarde.ppj'), 'wb') as sauvegarde:
            dp(self.population_generation_old, sauvegarde)
            sauvegarde.close()
        
        self.population_generation_old= zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        self.population_generation    = zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        
    ###---------------------------------------------------------------------###
    ###--------------> Fonction de croisement, selection et mutation
    def fct_sauvegarde_generation (self):
        '''
        Fonction permettant la sauvegarde de la generation."
        '''
        
        with open(self.dossier_sauvegarde + str('\sauvegarde.ppj'), 'rb') as lecture:
            population_stockee = ld(lecture)
            lecture.close()
        
        population = concatenate((population_stockee, self.population_generation_old))
        
        with open(self.dossier_sauvegarde + str('\sauvegarde.ppj'), 'wb') as sauvegarde:
            dp(population, sauvegarde)
            sauvegarde.close()
        
        self.population_generation_old= zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        self.population_generation    = zeros((self.nombre_individus, self.nombre_fonction + len(self.parametres_discrets) + len(self.parametres_continus)))
        
    def fct_lecture_sauvegarde (self):
        '''
        Fonction permettant la lecture du fichier sauvegarde."
        '''
        population_generation_stockee = ld(open(self.dossier_sauvegarde + str('\sauvegarde.ppj'), 'rb'))
        self.population_generation_old = population_generation_stockee[-self.nombre_individus:]
        return population_generation_stockee
        
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
            
    def fct_selection_ellistisme (self) :
        '''
        Fonction permettant de selectionner les meilleurs individus de la generation
        pour les integrer a la generation suivante.
        '''
        
        for individu in range(self.nombre_individus_ellistisme):
            self.population_generation[individu] = self.population_generation_old[individu].copy()
    
    def fct_croisement (self) :
        '''
        Fonction permettant de creer des individus croises de manière aléatoire
        dans la nouvelle génération.
        '''
        nombre_ind_ellite = self.nombre_individus_ellistisme
        
        for individu in range(self.nombre_individus_croisement):
            id_pere = randint(0, self.nombre_individus-1)
            id_mere = randint(0, self.nombre_individus-1)
            
            for discret in range(len(self.parametres_discrets)):
                self.population_generation[nombre_ind_ellite + individu][discret] = choice([self.population_generation_old[id_pere][discret], self.population_generation_old[id_mere][discret]]).copy()
            
            for continu in range(len(self.parametres_continus)):
                self.population_generation[nombre_ind_ellite + individu][len(self.parametres_discrets) + continu] = choice([self.population_generation_old[id_pere][len(self.parametres_discrets) + continu], self.population_generation_old[id_mere][len(self.parametres_discrets) + continu]]).copy()
    
    def fct_selection_duel (self) :
        '''
        Fonction permettant de confronter deux individus aléatoire et de
        sélectionner le meilleur pour la génération suivante.
        '''
        nombre_ind_ellite = self.nombre_individus_ellistisme
        nombre_ind_croise = self.nombre_individus_croisement
        
        for individu in range(self.nombre_individus_duel):
            id_1 = randint(0, self.nombre_individus-1)
            id_2 = randint(0, self.nombre_individus-1)
            
            cout_1 = self.population_generation_old[id_1][-1]
            cout_2 = self.population_generation_old[id_2][-1]
            
            if cout_1 < cout_2:
                self.population_generation[nombre_ind_ellite + nombre_ind_croise + individu] = self.population_generation_old[id_1].copy()
            else:
                self.population_generation[nombre_ind_ellite + nombre_ind_croise + individu] = self.population_generation_old[id_2].copy()
        

    ###---------------------------------------------------------------------###
    ###--------------> Optimisaton simple - boucle sur les générations
    def fct_optimisation_simple (self) :
        '''
        '''
        
        self.fct_initialisation_population()
        
        for generation in range(self.nombre_generation) :
            self.fct_lecture_sauvegarde()
            self.fct_selection_ellistisme()
            self.fct_croisement()
            self.fct_selection_duel()
            self.fct_mutation()
            self.fct_fonction_objective()
            self.fct_tri()
            self.fct_sauvegarde_generation()
        
    
    
    ###---------------------------------------------------------------------###
    ###--------------> Multi-optimisation - Variation des donnees de l'algorithme






###############################################################################
###############################################################################
###############################################################################