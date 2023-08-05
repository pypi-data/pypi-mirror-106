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

from sysam.sysam_3_test import Sysam3Test

from signaux.signal_gbf import SignalGBF
from signaux.signal_fourier import SignalFourier
from signaux.signal_sysam import SignalSysam

import base.voie_base

class Sysam4Methodes(Sysam3Test):

    def calculer_arguments_config_entrees(self):
        if "entree" in self.chaine_mode:
            voies = [s.voie.calculer_numero() for s in self.liste_entrees]
            calibres = [s.voie.calibre for s in self.liste_entrees]
            diff = [s.voie.calculer_numero() for s in self.liste_entrees_diffs]
            return voies, calibres, diff
        return None

    def calculer_arguments_config_echantillon(self):
        if "entree" in self.chaine_mode:
            if self.base_de_temps_entrees:
                techant = self.base_de_temps_entrees.Te / base.voie_base.T_sysam
                nbpoints = self.base_de_temps_entrees.N
                return techant, nbpoints
        return None

    def calculer_arguments_config_trigger(self):
        if "trigger" in self.chaine_mode:
            st = self.liste_triggers[0]
            voie = st.voie.calculer_numero()
            seuil = st.trigger.seuil
            montant = 1 if st.trigger.montant == True else 0
            pretrigger = st.trigger.pretrigger
            pretrigger_souple = 1 if st.trigger.pretrigger_souple == True else 0
            hysteresys = 1 if st.trigger.hysteresys == True else 0
            return voie, seuil, montant, pretrigger, pretrigger_souple, hysteresys
        return None

    def calculer_arguments_config_sortie(self, n):
        if "sortie"+str(n) in self.chaine_mode and "synchrone" not in self.chaine_mode:
            nsortie = n
            s = self.liste_sortie1[0] if n == 1 else self.liste_sortie2[0]
            techant = s.base_de_temps.Te / base.voie_base.T_sysam
            tensions = s.vecteur_signal
            repetition = -1 if s.voie.repetition else 0

            return nsortie, techant, tensions, repetition

        return None

    def calculer_arguments_declencher_sorties(self):
        if "sortie" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            s1 = 1 if self.liste_sortie1 else 0
            s2 = 1 if self.liste_sortie2 else 0
            return s1, s2
        return None

    def calculer_arguments_acquerir_avec_sorties(self):
        if "synchrone" in self.chaine_mode:
            tensions1 = self.liste_sortie1[0].vecteur_signal if "sortie1" in self.chaine_mode else np.zeros(1)
            tensions2 = self.liste_sortie2[0].vecteur_signal if "sortie2" in self.chaine_mode else np.zeros(1)
            return tensions1, tensions2
        return None


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
    s2 = SignalSysam("DIFF2", 10., liste_tmin_tmax_entrees_2, Te_entrees_2, "s2")
    s3 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_1, nom="s3")
    s4 = SignalGBF("carre", 1e3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_2, nom="s4")

    s3.configurer_voie("SA1", repetition = False)
    s4.configurer_voie("SA2", repetition = True)
    

    s2.configurer_trigger(0.)
    sysam = Sysam4Methodes()
    print(sysam.chaine_mode)
    print(sysam.test_signaux)

    print(sysam.calculer_arguments_config_entrees())
    print(sysam.calculer_arguments_config_echantillon())
    print(sysam.calculer_arguments_config_trigger())
    print(sysam.calculer_arguments_config_sortie(1))
    print(sysam.calculer_arguments_config_sortie(2))
    print(sysam.calculer_arguments_acquerir_avec_sorties())
    # lancer_acquisition()