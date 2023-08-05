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

from sysam.sysam_2_mode import Sysam2Mode

from signaux.signal_gbf import SignalGBF
from signaux.signal_fourier import SignalFourier
from signaux.signal_sysam import SignalSysam

import base.voie_base

from signaux.signal_base import *

class Sysam3Test(Sysam2Mode):
    def __init__(self, liste_signaux = None):
        Sysam2Mode.__init__(self, liste_signaux)
        if self.tester_liste_signaux():
            self.test_signaux = True
        else:
            self.test_signaux = False
            exit()


    ##################################################################################################################
    ## tester liste signaux
    ##################################################################################################################
    def tester_liste_signaux(self):
        # Générer Te_entrées_min
        liste_Te = [0.]
        if "entree" in self.chaine_mode:
            liste_Te.append(base.voie_base.Te_direct)
        if "multiplex" in self.chaine_mode:
            liste_Te.append(base.voie_base.Te_multiplex)
        if "synchrone" in self.chaine_mode:
            liste_Te.append(base.voie_base.Te_sortie)
        self.Te_entree_min = np.max(liste_Te)

        # Générer Te_sorties_min
        liste_Te = [0.]
        if "sortie" in self.chaine_mode:
            liste_Te.append(base.voie_base.Te_sortie)
        if "multiplex" in self.chaine_mode and "synchrone" in self.chaine_mode:
            liste_Te.append(base.voie_base.Te_multiplex)
        self.Te_sortie_min = np.max(liste_Te)

        # Générer base de temps entrées
        if self.liste_entrees_simples:
            self.base_de_temps_entrees = self.liste_entrees_simples[0].base_de_temps
        elif self.liste_entrees_diffs:
            self.base_de_temps_entrees = self.liste_entrees_diffs[0].base_de_temps
        else:
            self.base_de_temps_entrees = None

        # tester validite des noms des voies
        liste_signaux_noms_voies_ko = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_sysam() and (not s.voie.tester_nom()))
        if liste_signaux_noms_voies_ko:
            print("Problème avec les noms des voies voie suivants:\n -> ", end = "")
            afficher_liste_signaux(liste_signaux_noms_voies_ko)
            return False

        # tester compatibilités entre les noms des voies
        liste_paires_signaux_noms_voies_ko = lister_paires_signaux_test(self.liste_signaux, lambda s1, s2: s1.voie.tester_sysam() and s2.voie.tester_sysam() and not s1.voie.tester_compatibilite_nom(s2.voie))
        if liste_paires_signaux_noms_voies_ko:
            print("Problème de compatibilité entre les noms des paires de voies voie suivants:\n -> ", end="")
            afficher_liste_paires_signaux(liste_paires_signaux_noms_voies_ko)
            return False

        # tester trigger
        if self.liste_sorties_triggers:
            print("Problèmes des triggers sont affectés sur des sorties:\n -> ", end="")
            afficher_liste_signaux(self.liste_sorties_triggers)
            return False

        if len(self.liste_entrees_triggers) > 1:
            print("Problèmes plusieurs triggers sont affectés sur des entrées:\n -> ", end="")
            afficher_liste_signaux(self.liste_entrees_triggers)
            return False

        # tester entrees echantillonnés trop vite
        liste_entrees_echantillonnees_trop_vite = lister_signaux_test(self.liste_entrees, lambda s: s.base_de_temps.Te < self.Te_entree_min)
        if liste_entrees_echantillonnees_trop_vite:
            print("Les entrees suivantes ne respectent pas Te > ", self.Te_entree_min, "s\n -> ", end = '')
            afficher_liste_signaux(liste_entrees_echantillonnees_trop_vite)
            return False

        # tester sorties echantillonnées trop vite
        liste_sorties_echantillonnees_trop_vite = lister_signaux_test(self.liste_sorties, lambda s: s.base_de_temps.Te < self.Te_sortie_min)
        if liste_sorties_echantillonnees_trop_vite:
            print("Les sorties suivantes ne respectent pas Te > ", self.Te_sortie_min, "s\n -> ", end = '')
            afficher_liste_signaux(liste_sorties_echantillonnees_trop_vite)
            return False

        # tester compatibilités entre les bases de temps des entrées
        liste_paires_entrees_bases_de_temps_ko = lister_paires_signaux_test(self.liste_entrees, lambda s1, s2: s1.base_de_temps != s2.base_de_temps)
        if liste_paires_entrees_bases_de_temps_ko:
            print("Problème de compatibilité entre les bases de temps des entrées voie suivantes:\n -> ", end="")
            afficher_liste_paires_signaux(liste_paires_entrees_bases_de_temps_ko)
            return False

        # tester validite des bases de temps de sortie
        if "synchrone" in self.chaine_mode:
            liste_sorties_echantillonnage_ko = lister_signaux_test(self.liste_sorties, lambda s: s.base_de_temps.Te != self.base_de_temps_entrees.Te)
            if liste_sorties_echantillonnage_ko:
                print("Problème de périodes d'échantillonnage sur les sorties suivantes (ES synchrones):\n -> ", end="")
                afficher_liste_signaux(liste_sorties_echantillonnage_ko)
                return False

        # tester si les sorties commencent à t=0
        liste_sorties_tardives = lister_signaux_test(self.liste_sorties, lambda s: s.base_de_temps.Nmin != 0)
        if liste_sorties_tardives:
            print("Les sorties suivantes ne débutent pas à t=0:\n -> ", end="")
            afficher_liste_signaux(liste_sorties_tardives)


        # tester espace memoire
        liste_signaux_sysam = lister_signaux_test(self.liste_signaux, lambda s: s.voie.tester_sysam())
        liste_N_ech = [s.base_de_temps.N for s in liste_signaux_sysam]

        if np.sum(liste_N_ech) > base.voie_base.N_ech_max:
            print("Trop d'échantillons stockés en mémoire (max = {0})".format(base.voie_base.N_ech_max))
            for i in range(len(liste_signaux_sysam)):
                _str = "-> {0:15}".format(convertir_signal_vers_str(liste_signaux_sysam[i]))  + "{0:10} éch.".format(liste_N_ech[i])
                print(_str)
            return False

        return True

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
    sysam = Sysam3Test()

    print(sysam.chaine_mode)
    print(sysam.test_signaux)

