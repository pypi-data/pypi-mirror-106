#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from traitements.signal_fft import SignalFFT
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence

__all__ = ["tracer_spectres"]

def tracer_spectres(liste_signaux, liste_fmin_fmax = [None, None], superposition = True, nom_fichier = ""):
    SignalFFTPlot.tracer_spectres(liste_signaux, liste_fmin_fmax, superposition)

class SignalFFTPlot(SignalFFT, SignalBase):
    def tracer_spectre(self, liste_fmin_fmax=[None, None], nom_fichier = ""):
        fmin, fmax = liste_fmin_fmax

        fig = plt.figure()
        ax = fig.add_subplot(111)

        fmin, fmax = self.__choisir_liste_flim([self], liste_fmin_fmax)
        ax.set_xlim(fmin, fmax)

        imin, imax = self.__choisir_liste_ilim([fmin, fmax])

        plt.xlabel("$f$ (en Hz)")
        plt.ylabel("$U$ (en SI)")
        self.__tracer_spectre([imin, imax])
        if self.__tester_legende([self]):
            plt.legend()
        if nom_fichier != "":
            fig.savefig(nom_fichier)
        plt.show()

    def tracer_spectres(liste_signaux, liste_fmin_fmax = [None, None], superposition = True, nom_fichier = ""):
        assert len(liste_signaux) > 0
        if superposition == True:
            fig = SignalFFTPlot.__tracer_spectres_superposes(liste_signaux, liste_fmin_fmax)
        else:
            fig = SignalFFTPlot.__tracer_spectres_non_superposes(liste_signaux, liste_fmin_fmax)
        if nom_fichier != "":
            fig.savefig(nom_fichier)
        plt.show()
        
    def __tracer_spectre(self, liste_imin_imax):
        imin, imax = liste_imin_imax
        vecteur_spectre = self.calculer_vecteur_spectre(liste_imin_imax)
        vecteur_f = self.base_de_frequence.calculer_vecteur_f(liste_imin_imax)
        if self.nom != "":
            plt.plot(vecteur_f, vecteur_spectre, label = "Spectre_de_" + self.nom)
        else:
            plt.plot(vecteur_f, vecteur_spectre)

    def __choisir_liste_flim(self, liste_signaux, liste_fmim_fmax):
        fmin, fmax = liste_fmim_fmax
        _fmin = 0
        _fmax = np.max([1/(2*s.base_de_temps.Te) for s in liste_signaux])
        if fmin == None:
            fmin = _fmin
        if fmax == None:
            fmax = _fmax
        return fmin, fmax

    def __choisir_liste_ilim(self, liste_fmim_fmax):
        fmin, fmax = liste_fmim_fmax
        _fmin , _fmax = 0, 1/(2*self.base_de_temps.Te)
        if fmin < 0:
            fmin = _fmin
        if fmax > _fmax:
            fmax = _fmax
        return self.base_de_frequence.calculer_i(fmin), self.base_de_frequence.calculer_i(fmax)

    def __tracer_spectres_superposes(liste_signaux, liste_fmin_fmax = [None, None]):
        Nsignaux = len(liste_signaux)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        _fmin, _fmax = liste_signaux[0].__choisir_liste_flim(liste_signaux, liste_fmin_fmax)
        ax.set_xlim(_fmin, _fmax)

        plt.xlabel("$f$ (en Hz)")
        plt.ylabel("$U$ (en SI)")
        for i in range(Nsignaux):
            imin, imax = liste_signaux[i].__choisir_liste_ilim([_fmin, _fmax])
            liste_signaux[i].__tracer_spectre([imin, imax])
        if liste_signaux[0].__tester_legende(liste_signaux):
            plt.legend()
        return fig

    def __tester_legende(self, liste_signaux):
        for s in liste_signaux:
            if s.nom != "":
                return True
        return False

    def __tracer_spectres_non_superposes(liste_signaux, liste_fmin_fmax = [None, None]):
        Nsignaux = len(liste_signaux)
        assert Nsignaux < 10, "Trop de tracés pour un tracé sur différents axes"


        _fmin, _fmax = liste_signaux[0].__choisir_liste_flim(liste_signaux, liste_fmin_fmax)

        fig = plt.figure()
        liste_axes = []

        for i in range(Nsignaux):
            chaine_subplot = "{0}1{1}".format(Nsignaux, i+1)
            liste_axes.append( fig.add_subplot(int(chaine_subplot) ) )
            liste_axes[i].set_xlim(_fmin, _fmax)
            imin, imax = liste_signaux[i].__choisir_liste_ilim([_fmin, _fmax])
            liste_signaux[i].__tracer_spectre([imin, imax])
            plt.xlabel("$f$ (en Hz)")
            plt.ylabel("$U$ (en SI)")
            if liste_signaux[i].__tester_legende([liste_signaux[i]]):
                plt.legend()
        return fig

        
if __name__ == "__main__":
    Te1 = 1e-4
    liste_tmin_tmax1 = 0, 10

    Te2 = 1e-3
    liste_tmin_tmax2 = 0.05, 1.05

    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)
    bdt2 = BaseTemps(liste_tmin_tmax2, Te2)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_t2 = bdt2.calculer_vecteur_t()
    vecteur_signal1 = 3*np.cos(2*np.pi*30*vecteur_t1)
    vecteur_signal2 = np.sin(2*np.pi*10*vecteur_t2)

    s1 = SignalFFTPlot(bdt1, vecteur_signal1, nom="s1")
    s2 = SignalFFTPlot(bdt2, vecteur_signal2, nom="s2")


    # s1.tracer_spectre([10, 50])
    tracer_spectres([s1, s2], [-25, 50], superposition = True)

    # plt.show()
    # SignalPlot.tracer_signaux([s1, s2], [0, 1], superposition = True)
    # s2.tracer_signal()
    
