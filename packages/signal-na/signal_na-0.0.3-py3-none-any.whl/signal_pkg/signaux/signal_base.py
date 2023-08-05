#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import copy
from math import ceil, floor

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence
from base.mesure_base import Mesures
from base.voie_base import Voie
from base.trigger_base import Trigger

__all__ = ["SignalBase", "convertir_liste_signaux_vers_str", "convertir_liste_paires_signaux_vers_str", "afficher_liste_paires_signaux", "afficher_liste_signaux", "lister_signaux_test", "lister_paires_signaux_test"]

def convertir_liste_signaux_vers_str(liste_signaux):
    _str = ""
    for s in liste_signaux:
        _str += "{0:15}".format(str(s))
    return _str

def convertir_liste_paires_signaux_vers_str(liste_paires_signaux):
    _str = ""
    for p in liste_paires_signaux:
        _str += "{0:40}".format(str(p[0]) + " et " + str(p[1]))
    return _str

def afficher_liste_paires_signaux(liste_paires_signaux):
    print(convertir_liste_paires_signaux_vers_str(liste_paires_signaux))

def afficher_liste_signaux(liste_signaux, end = "\n"):
    print(convertir_liste_signaux_vers_str(liste_signaux))

def lister_signaux_test(liste_signaux, fonction_test):
    liste_signaux_test = []
    for s in liste_signaux:
        if fonction_test(s):
            if s not in liste_signaux_test:
                liste_signaux_test.append(s)
    liste_signaux_test.sort(key = lambda s: s.voie.calculer_numero())
    return liste_signaux_test
    
def lister_paires_signaux_test(liste_signaux, fonction_test):
    lister_paires_signaux_test = []
    for s1 in liste_signaux:
        for s2 in liste_signaux:
            if s1 != s2:
                if fonction_test(s1, s2):
                    if [s1, s2] not in lister_paires_signaux_test and [s2, s1] not in lister_paires_signaux_test:
                        lister_paires_signaux_test.append([s1, s2])
    for l in lister_paires_signaux_test: 
        l.sort(key = lambda s: s.voie.nom)
    lister_paires_signaux_test.sort(key = lambda l: l[0].voie.calculer_numero())
    return lister_paires_signaux_test

class SignalBase():

    liste_signaux = []
    
    def __init__(self, base_de_temps, vecteur_signal, nom = ""):
        self.base_de_temps = base_de_temps.copier()
        self.base_de_frequence = BaseFrequence(base_de_temps)
        self.mesures = Mesures()
        self.voie = Voie()
        self.trigger = Trigger()

        assert  base_de_temps.N == len(vecteur_signal), """Erreur dans le module SignalBase:
         -> La base de temps et le signal doivent avoir la même dimension"""

        self.__chercher_nom_valide(nom)
        self.vecteur_signal = vecteur_signal
        self.liste_signaux.append(self)

    def copier(self, nom = ""):
        sortie = copy.deepcopy(self)
        sortie.mesures = Mesures()
        sortie.voie = Voie()
        sortie.trigger = Trigger()
        sortie.liste_signaux.append(sortie)
        if nom != "":
            sortie.nom = nom + "_copié"
        return sortie

    def calculer_vecteur_t(self, liste_imin_imax):
        return self.base_de_temps.calculer_vecteur_t(liste_imin_imax)

    def calculer_vecteur_f(self, liste_imin_imax):
        return self.base_de_frequence.calculer_vecteur_f(liste_imin_imax)


    def __tester_nom(self):
        for s in self.liste_signaux:
            if s != self and s.nom == self.nom:
                return False
        return True

    def __chercher_nom_valide(self, nom):
        if nom == "":
            nom = "s"
        self.nom = nom
        i = 2
        while self.__tester_nom() == False:
            self.nom = nom + "_" + str(i)
            i = i + 1

    def configurer_voie(self, nom_voie, calibre = 10., repetition = False):
        self.voie.nom = nom_voie
        self.voie.calibre = calibre
        self.voie.repetition = repetition

    def deconfigurer_voie(self):
        self.voie = Voie()

    def configurer_trigger(self, seuil, montant=True, pretrigger=0, pretrigger_souple=False, hysteresys=False):
        self.trigger.seuil = seuil
        self.trigger.montant = montant
        self.trigger.pretrigger = pretrigger
        self.trigger.pretrigger_souple = pretrigger_souple
        self.trigger.hysteresys = hysteresys

    def deconfigurer_trigger(self):
        self.trigger = Voie()

    def __str__(self):
        chaine = self.nom
        if self.voie.nom != None:
            chaine += "({0})".format(self.voie.nom)
        else:
            chaine += "(X)"
        if self.trigger.seuil != None:
            chaine += "T".format(self.voie.nom)
        return chaine

if __name__ == "__main__":
    pass
    # Te = 1e-1
    # T = 1

    # liste_tmin_tmax = -1, 3

    # bdt = BaseTemps(liste_tmin_tmax, Te)
    # bdt_periode = BaseTemps([0,T], Te)
    # vecteur_t = bdt.calculer_vecteur_t()
    # vecteur_t_periode = bdt_periode.calculer_vecteur_t()
    # vecteur_signal = np.cos(2*np.pi*vecteur_t)
    # vecteur_periode_signal = np.cos(2*np.pi*vecteur_t_periode)
    # s1 = SignalBase(bdt, vecteur_signal, nom = "s1")
    # s2 = SignalBase(bdt, vecteur_signal, nom = "s2")

    # liste_signaux = []
    # for i in range(10):
    #     liste_signaux.append(SignalBase(bdt, vecteur_signal))

    # print("*"*100)
    # for s in liste_signaux:
    #     print(s.nom)        

