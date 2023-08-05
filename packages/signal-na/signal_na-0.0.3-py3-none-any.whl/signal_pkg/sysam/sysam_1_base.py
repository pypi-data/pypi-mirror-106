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

from signaux.signal_gbf import SignalGBF
from signaux.signal_fourier import SignalFourier
from signaux.signal_sysam import SignalSysam

import base.voie_base


from signaux.signal_base import *

class Sysam1Base():
    def __init__(self, liste_signaux = None):
        if liste_signaux != None:
            self.liste_signaux = liste_signaux
        else:
            self.liste_signaux = SignalSysam.liste_signaux

        afficher_liste_signaux(self.liste_signaux)
        self.sysam = pycan.Sysam("SP5")

        self.liste_entrees_simples = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_entree_simple())
        self.liste_entrees_diffs = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_entree_diff())
        self.liste_entrees = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_entree())
        self.liste_sorties = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_sortie())
        self.liste_sortie1 = lister_signaux_test(self.liste_sorties, lambda s: s.voie.nom == "SA1")
        self.liste_sortie2 = lister_signaux_test(self.liste_sorties, lambda s: s.voie.nom == "SA2")
        self.liste_triggers = lister_signaux_test(self.liste_signaux, lambda s: s.trigger.tester_trigger())
        self.liste_entrees_triggers = lister_signaux_test(self.liste_entrees, lambda s: s.trigger.tester_trigger())
        self.liste_sorties_triggers = lister_signaux_test(self.liste_sorties, lambda s: s.trigger.tester_trigger())

        
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        # self.voie.stopper_sorties(1, 1)
        # self.voie.close()
        pass

    def __del__(self):
        self.sysam.close()
    

if __name__ == "__main__":
    liste_tmin_tmax_entrees_1 = [0, 2e-3]
    Te_entrees_1 = 1e-4

    liste_tmin_tmax_entrees_2 = [0, 2e-3]
    Te_entrees_2 = 1e-4

    liste_tmin_tmax_sortie_1 = [0, 2e-3]
    Te_sortie_1 = 1e-4

    liste_tmin_tmax_sortie_2 = [0, 2e-3]
    Te_sortie_2 = 1e-4

    s1 = SignalGBF()
    s1 = SignalSysam("EA1", 10., liste_tmin_tmax_entrees_1, Te_entrees_1, "s1")
    s2 = SignalSysam("EA2", 10., liste_tmin_tmax_entrees_2, Te_entrees_2, "s2")
    s3 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_1, nom="s3")
    s4 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_2, nom="s4")

    s3.configurer_voie("SA1", repetition = True)
    s4.configurer_voie("SA2", repetition = True)
    
    # s1.configurer_trigger(0.)
    sysam = Sysam1Base()


    # lancer_acquisition()