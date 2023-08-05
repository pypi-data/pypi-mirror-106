import numpy as np
import matplotlib.pyplot as plt

import os, sys, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

try:
    import pycanum.main as pycan
except:
    # print("Attention: la bibliothèque pycanum n'est pas installée")
    # print(" -> Fonctionnement en mode émulation")
    import acquisition.emulateur_sysam_sp5 as pycan


from sysam.sysam_1_base import Sysam1Base
from signaux.signal_gbf import SignalGBF
from signaux.signal_fourier import SignalFourier
from signaux.signal_sysam import SignalSysam

import base.voie_base


from signaux.signal_base import *

class Sysam2Mode(Sysam1Base):
    def __init__(self, liste_signaux = None):
        Sysam1Base.__init__(self, liste_signaux)
        self.generer_chaine_mode()

    def generer_chaine_mode(self):
        liste_paires_signaux_multiplex = lister_paires_signaux_test(self.liste_signaux, lambda s1, s2: s1.voie.tester_necessite_multiplexage(s2.voie))

        test_multiplex = True if liste_paires_signaux_multiplex else False
        test_entree = True if self.liste_entrees else False
        test_sortie = True if self.liste_sorties else False
        test_sortie1 = True if self.liste_sortie1 else False
        test_sortie2 = True if self.liste_sortie2 else False
        test_trigger = True if self.liste_triggers else False

        test_synchrone = False
        if not test_trigger and test_entree and test_sortie:
            if self.liste_entrees_simples: 
                if self.liste_entrees_simples[0].base_de_temps.Nmin == 0:
                    test_synchrone = True
            if self.liste_entrees_diffs: 
                if self.liste_entrees_diffs[0].base_de_temps.Nmin == 0:
                    test_synchrone = True

        chaine_mode = ""
        chaine_mode = chaine_mode + "-entree-" if test_entree else chaine_mode
        chaine_mode = chaine_mode + "-sortie1-" if test_sortie1 else chaine_mode
        chaine_mode = chaine_mode + "-sortie2-" if test_sortie2 else chaine_mode
        chaine_mode = chaine_mode + "-multiplex-" if test_multiplex else chaine_mode
        chaine_mode = chaine_mode + "-synchrone-" if test_synchrone else chaine_mode
        chaine_mode = chaine_mode + "-trigger-" if test_trigger else chaine_mode
        
        self.chaine_mode = chaine_mode


if __name__ == "__main__":
    liste_tmin_tmax_entrees_1 = [0, 2e-3]
    Te_entrees_1 = 1e-4

    liste_tmin_tmax_entrees_2 = [0, 2e-3]
    Te_entrees_2 = 1e-4

    liste_tmin_tmax_sortie_1 = [0, 2e-3]
    Te_sortie_1 = 1e-4

    liste_tmin_tmax_sortie_2 = [0, 2e-3]
    Te_sortie_2 = 1e-4

    s1 = SignalSysam("EA1", 10., liste_tmin_tmax_entrees_1, Te_entrees_1, "s1")
    s2 = SignalSysam("EA2", 10., liste_tmin_tmax_entrees_2, Te_entrees_2, "s2")
    s3 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_1, nom="s3")
    s4 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_2, nom="s4")

    s3.configurer_voie("SA1", repetition = True)
    s4.configurer_voie("SA2", repetition = True)
    
    # s1.configurer_trigger(0.)
    sysam = Sysam2Mode()

    print(sysam.chaine_mode)

    # lancer_acquisition()