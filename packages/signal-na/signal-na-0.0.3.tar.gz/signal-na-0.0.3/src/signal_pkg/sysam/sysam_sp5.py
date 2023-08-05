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

import base.temps_base
import base.voie_base


from sysam.sysam_4_methodes import Sysam4Methodes

__all__ = ["demarrer_sysam"]

def demarrer_sysam(liste_signaux=None):
    with SysamSP5(liste_signaux) as sysam:
        pass

# def demarrer_sysam(liste_signaux=None):
#     if __name__ == '__main__':
#         try:
#             sysam = SysamSP5(liste_signaux)
#         except KeyboardInterrupt:
#             print('Interrupted')
#             try:
#                 sys.exit(0)
#             except SystemExit:
#                 os._exit(0)

class SysamSP5(Sysam4Methodes):
    def __init__(self, liste_signaux = None):
        Sysam4Methodes.__init__(self, liste_signaux)
        print(self.chaine_mode)
        if "entree" in self.chaine_mode:
            self.sysam.config_entrees(*self.calculer_arguments_config_entrees())
            self.sysam.config_echantillon(*self.calculer_arguments_config_echantillon())

        if "trigger" in self.chaine_mode:
            self.sysam.config_trigger(*self.calculer_arguments_config_trigger())
        else:
            self.sysam.desactiver_trigger()

        if "sortie1" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            self.sysam.config_sortie(*self.calculer_arguments_config_sortie(1))

        if "sortie2" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            self.sysam.config_sortie(*self.calculer_arguments_config_sortie(2))


        if "synchrone" in self.chaine_mode:
            self.sysam.acquerir_avec_sorties(*self.calculer_arguments_acquerir_avec_sorties())
            self.mettre_a_jour_entrees()
        elif "entree" in self.chaine_mode:
            tmin, tmax = self.base_de_temps_entrees.calculer_liste_tmin_tmax()
            self.sysam.declencher_sorties(*self.calculer_arguments_declencher_sorties())
            if tmin != 0:
                time.sleep(tmin)
            self.sysam.acquerir()
            self.mettre_a_jour_entrees()
        elif "sortie" in self.chaine_mode:
            self.sysam.declencher_sorties(*self.calculer_arguments_declencher_sorties())
            test_fin = False
            while not test_fin:
                chaine = input("On arrête les signaux o/N?")
                if chaine == "o" or chaine == "O":
                    test_fin = True

    def mettre_a_jour_entrees(self):
        temps = self.sysam.temps()
        entrees = self.sysam.entrees()
        voies = self.calculer_arguments_config_entrees()[0]

        if "synchrone" not in self.chaine_mode:
            Nsysam = np.max(base.temps_base.BaseTemps.liste_bases_de_temps_sysam) + 1
            base.temps_base.BaseTemps.liste_bases_de_temps_sysam.append(Nsysam)
        else:
            Nsysam = None

        for s in self.liste_entrees:
            voie = s.voie.calculer_numero()
            indice = voies.index(voie)
            s.vecteur_signal = np.array(entrees[indice])
            s.base_de_temps = base.temps_base.convertir_vecteur_t_vers_base_de_temps(np.array(temps[indice]))
            s.base_de_temps.Nsysam = Nsysam

if __name__ == "__main__":
    liste_tmin_tmax_entrees_1 = [0, 2e-3]
    Te_entrees_1 = 1e-4

    liste_tmin_tmax_entrees_2 = [0, 2e-3]
    Te_entrees_2 = 1e-4

    liste_tmin_tmax_sortie_1 = [0, 2e-3]
    Te_sortie_1 = 1e-4

    liste_tmin_tmax_sortie_2 = [0, 2e-3]
    Te_sortie_2 = 1e-4

    # s1 = SignalSysam("EA7", 10., liste_tmin_tmax_entrees_1, Te_entrees_1, "s1")
    # s2 = SignalSysam("DIFF2", 10., liste_tmin_tmax_entrees_2, Te_entrees_2, "s2")
    s3 = SignalGBF("carre", 1e3, 3, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_1, nom="s3")
    s4 = SignalGBF("carre", 1e3, 4, liste_tmin_tmax = liste_tmin_tmax_sortie_1, Te = Te_sortie_2, nom="s4")

    s3.configurer_voie("SA1", repetition = True)
    s4.configurer_voie("SA1", repetition = True)
    
    # s1.configurer_trigger(0.)

    demarrer_sysam()

    SignalSysam.tracer_signaux([s1, s2, s3, s4])

    s8 = s1+s2
    s9 = s3+s4
    s10 = s1+s3

    print(s1.base_de_temps == s3.base_de_temps)
