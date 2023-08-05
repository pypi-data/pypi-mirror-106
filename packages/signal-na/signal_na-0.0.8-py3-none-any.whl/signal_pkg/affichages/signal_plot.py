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
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps

__all__ = ["tracer_signaux"]

def tracer_signaux(liste_signaux, liste_tmin_tmax = [None, None], superposition = True, nom_fichier = ""):
    SignalPlot.tracer_signaux(liste_signaux, liste_tmin_tmax, superposition, nom_fichier)

class SignalPlot(SignalBase):
    def tracer_signal(self, liste_tmin_tmax=[None, None], nom_fichier = ""):
        tmin, tmax = liste_tmin_tmax

        fig = plt.figure()
        ax = fig.add_subplot(111)

        tmin, tmax = self.__choisir_liste_tlim([self], liste_tmin_tmax)
        ax.set_xlim(tmin, tmax)

        imin, imax = self.__choisir_liste_ilim([tmin, tmax])

        plt.xlabel("$t$ (en s)")
        plt.ylabel("$u$ (en V)")
        self.__tracer_signal([imin, imax])
        if self.__tester_legende([self]):
            plt.legend()
        if nom_fichier != "":
            fig.savefig(nom_fichier)
        plt.show()
        
    def tracer_signaux(liste_signaux, liste_tmin_tmax = [None, None], superposition = True, nom_fichier = ""):
        if len(liste_signaux) > 0:
            test_bases_de_temps_compatibles = True
            Nsysam = liste_signaux[0].base_de_temps.Nsysam
            for s in liste_signaux:
                if s.base_de_temps.Nsysam != Nsysam:
                    print("Certains signaux proviennent de bases de temps incompatibles (acquisitions Sysam)")
                    return
            if superposition == True:
                fig = SignalPlot.__tracer_signaux_superposes(liste_signaux, liste_tmin_tmax)
            else:
                fig = SignalPlot.__tracer_signaux_non_superposes(liste_signaux, liste_tmin_tmax)
            if nom_fichier != "":
                fig.savefig(nom_fichier)
            plt.show()

    def __tracer_signal(self, liste_imin_imax):
        imin, imax = liste_imin_imax
        vecteur_t = self.calculer_vecteur_t([imin, imax])
        if self.nom != "":
            plt.plot(vecteur_t, self.vecteur_signal[imin:imax], label = self.nom)
        else:
            plt.plot(vecteur_t, self.vecteur_signal[imin:imax])

    def __choisir_liste_tlim(self, liste_signaux, liste_tmim_tmax):
        tmin, tmax = liste_tmim_tmax
        _tmin = np.min([s.base_de_temps.calculer_t(s.base_de_temps.Nmin) for s in liste_signaux])
        _tmax = np.max([s.base_de_temps.calculer_t(s.base_de_temps.Nmax) for s in liste_signaux])
        if tmin == None:
            tmin = _tmin
        if tmax == None:
            tmax = _tmax
        return tmin, tmax

    def __choisir_liste_ilim(self, liste_tmim_tmax):
        tmin, tmax = liste_tmim_tmax
        _tmin , _tmax = self.base_de_temps.calculer_t(self.base_de_temps.Nmin), self.base_de_temps.calculer_t(self.base_de_temps.Nmax)
        if tmin < _tmin:
            tmin = _tmin
        if tmax > _tmax:
            tmax = _tmax
        Nmin, Nmax = self.base_de_temps.calculer_n(tmin), self.base_de_temps.calculer_n(tmax)
        return self.base_de_temps.convertir_n_vers_i(Nmin), self.base_de_temps.convertir_n_vers_i(Nmax)

    def __tester_legende(self, liste_signaux):
        for s in liste_signaux:
            if s.nom != "":
                return True
        return False

    def __tracer_signaux_superposes(liste_signaux, liste_tmin_tmax = [None, None]):
        Nsignaux = len(liste_signaux)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        _tmin, _tmax = liste_signaux[0].__choisir_liste_tlim(liste_signaux, liste_tmin_tmax)
        ax.set_xlim(_tmin, _tmax)

        plt.xlabel("$t$ (en s)")
        plt.ylabel("$u$ (en V)")
        for i in range(Nsignaux):
            imin, imax = liste_signaux[i].__choisir_liste_ilim([_tmin, _tmax])
            liste_signaux[i].__tracer_signal([imin, imax])
        if liste_signaux[0].__tester_legende(liste_signaux):
            plt.legend()
        return fig

    def __tracer_signaux_non_superposes(liste_signaux, liste_tmin_tmax = [None, None]):
        Nsignaux = len(liste_signaux)
        assert Nsignaux < 10, "Trop de tracés pour un tracé sur différents axes"

        _tmin, _tmax = liste_signaux[0].__choisir_liste_tlim(liste_signaux, liste_tmin_tmax)

        fig = plt.figure()
        liste_axes = []

        for i in range(Nsignaux):
            chaine_subplot = "{0}1{1}".format(Nsignaux, i+1)
            liste_axes.append( fig.add_subplot(int(chaine_subplot) ) )
            liste_axes[i].set_xlim(_tmin, _tmax)
            imin, imax = liste_signaux[i].__choisir_liste_ilim([_tmin, _tmax])
            liste_signaux[i].__tracer_signal([imin, imax])
            plt.xlabel("$t$ (en s)")
            plt.ylabel("$u$ (en V)")
            if liste_signaux[i].__tester_legende([liste_signaux[i]]):
                plt.legend()
        return fig

        
if __name__ == "__main__":
    Te1 = 1e-4
    liste_tmin_tmax1 = -1.05, 0.35

    Te2 = 1e-3
    liste_tmin_tmax2 = 0.05, 1.05

    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)
    bdt2 = BaseTemps(liste_tmin_tmax2, Te2)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_t2 = bdt2.calculer_vecteur_t()
    vecteur_signal1 = np.cos(2*np.pi*vecteur_t1)
    vecteur_signal2 = np.sin(2*np.pi*vecteur_t2)

    s1 = SignalPlot(bdt1, vecteur_signal1)
    s1.tracer_signal()


    s2 = SignalPlot(bdt2, vecteur_signal2)

    tracer_signaux([s1, s2], superposition = False)
    # s2.tracer_signal()
    
