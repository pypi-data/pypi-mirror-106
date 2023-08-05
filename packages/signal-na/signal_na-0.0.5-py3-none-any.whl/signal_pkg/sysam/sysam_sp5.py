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

import signaux

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
#                 sys.sys.exit(0)
#             except Systemsys.exit:
#                 os._sys.exit(0)

class SysamSP5(Sysam4Methodes):
    def __init__(self, liste_signaux):
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
        elif "entree" in self.chaine_mode and "sortie" in self.chaine_mode:
            tmin, tmax = self.base_de_temps_entrees.calculer_liste_tmin_tmax()
            self.sysam.declencher_sorties(*self.calculer_arguments_declencher_sorties())
            if tmin != 0:
                time.sleep(tmin)
            self.sysam.acquerir()
            self.mettre_a_jour_entrees()
        elif "entree" in self.chaine_mode and "sortie" not in self.chaine_mode:
            tmin, tmax = self.base_de_temps_entrees.calculer_liste_tmin_tmax()
            self.sysam.acquerir()
            self.mettre_a_jour_entrees()            
        elif "sortie" in self.chaine_mode and "entree" not in self.chaine_mode:
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
    liste_tmin_tmax = [0, 2e-3]
    Te = 1e-4

    N = 10
    liste_signaux = []
    for i in range(N):
        liste_signaux.append(SignalGBF(liste_tmin_tmax = liste_tmin_tmax, Te = Te))

    # # tester acquisition non synchrone
    # liste_signaux[0].configurer_voie("EA1")
    # liste_signaux[1].configurer_voie("SA1")
    # liste_signaux[2].configurer_voie("DIFF2")

    # liste_signaux[2].configurer_trigger(0)
    # sysam = SysamSP5(liste_signaux)

    # SignalGBF.tracer_signaux(liste_signaux[0:3:2])

    # # tester acquisition synchrone
    # liste_signaux[0].configurer_voie("EA1")
    # liste_signaux[1].configurer_voie("SA1")
    # liste_signaux[2].configurer_voie("DIFF2")

    # sysam = SysamSP5(liste_signaux)

    # SignalGBF.tracer_signaux(liste_signaux[0:3])

    # tester acquisition sans entrées
    liste_signaux[0].configurer_voie("EA1")
    liste_signaux[1].configurer_voie("DIFF2")

    sysam = SysamSP5(liste_signaux)

    SignalGBF.tracer_signaux(liste_signaux[0:2])
