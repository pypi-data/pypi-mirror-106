#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import time

import os, sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst
from base.temps_base import BaseTemps
from signaux.signal_complet import SignalComplet
from base.voie_base import Voie
from base.trigger_base import Trigger

import base.voie_base

import matplotlib.pyplot as plt
 
__all__ = ["SignalSysam"]



class SignalSysam(SignalComplet):
    def __init__(self, nom_voie, calibre = 10., liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):

        base_de_temps = BaseTemps(liste_tmin_tmax, Te)
        vecteur_signal = np.zeros(base_de_temps.N)
        SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)
        self.configurer_sysam(nom_voie, calibre)

    def configurer_sysam(self, nom_voie, calibre = 10., repetition = False):
        self.voie.nom = nom_voie
        self.voie.calibre = calibre
        self.voie.repetition = repetition

    def deconfigurer_sysam(self):
        self.voie = Voie()

    def configurer_trigger(self, seuil, montant=True, pretrigger=0, pretrigger_souple=False, hysteresys=False):
        self.trigger.seuil = seuil
        self.trigger.montant = montant
        self.trigger.pretrigger = pretrigger
        self.trigger.pretrigger_souple = pretrigger_souple
        self.trigger.hysteresys = hysteresys

    def deconfigurer_trigger(self):
        self.trigger = Voie()


if __name__ == "__main__":

    liste_tmin_tmax=[0, 1e-8]
    Te = 2e-7

    bdt = BaseTemps(liste_tmin_tmax, Te)
    vecteur_signal = np.zeros(bdt.convertir_n_vers_i(bdt.Nmax))

    liste_signaux = []
    for i in range(10): 
        liste_signaux.append(SignalSysam(bdt, vecteur_signal))


    liste_signaux[0].configurer_sysam("EA0")
    liste_signaux[1].configurer_sysam("SA2")
    liste_signaux[2].configurer_sysam("EA5")
    liste_signaux[7].configurer_sysam("DIFF2")

    print("fin")

