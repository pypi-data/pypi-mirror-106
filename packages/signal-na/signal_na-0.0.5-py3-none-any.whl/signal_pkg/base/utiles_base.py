import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps


def str_liste(liste, sep1 = ", ", sep2 = " et ", begin = "", end = ""):
    str_ = sep1.join([str(e) for e in liste[:-1]])
    if len(liste)>1:
        str_ = sep2.join([str_, str(liste[-1])])
    else:
        str_ = str(liste[0])
    return "".join([begin, str_, end])

def str_liste_de_listes(liste_de_listes, 
    sep11 = ", ", sep12 = " et ", begin1 = "", end1 = "", 
    sep21 = ", ", sep22 = " et ", begin2 = "(", end2 = ")"
    ):
        liste_str = []
        for liste in liste_de_listes:
            liste_str.append(str_liste(liste, sep21, sep22, begin2, end2))
        return str_liste(liste_str, sep11, sep12, begin1, end1)
                
def print_liste(liste, sep1 = ", ", sep2 = " et ", begin = "", end = ""):
    print(str_liste(liste, sep1, sep2, begin, end))

def print_liste_de_listes(liste_de_listes, 
    sep11 = ", ", sep12 = " et ", begin1 = "", end1 = "", 
    sep21 = ", ", sep22 = " et ", begin2 = "(", end2 = ")"
    ):
    print(str_liste_de_listes(liste_de_listes, sep11, sep12, begin1, end1, sep21, sep22, begin2, end2))

def lister_test(liste, fonction_test, cle_de_tri):
    liste_test = []
    for e in liste:
        if fonction_test(e):
            if e not in liste_test:
                liste_test.append(e)
    liste_test.sort(key = cle_de_tri)
    return liste_test

def lister_paires_test(liste, fonction_test, cle_de_tri_1, cle_de_tri_2):
    liste_paires_test = []
    for e1 in liste:
        for e2 in liste:
            if e1 != e2:
                if fonction_test(e1, e2):
                    if [e1, e2] not in liste_paires_test and [e2, e1] not in liste_paires_test:
                        p = [e1, e2]
                        p.sort(key = cle_de_tri_2)
                        liste_paires_test.append(p)
    liste_paires_test.sort(key = cle_de_tri_1)
    return liste_paires_test


if __name__ == "__main__":
    bdt = BaseTemps([0,1], 1e-3)

    N = 4
    liste = []
    for i in range(N):
        liste.append(SignalBase(bdt))

    print(str_liste(liste, begin = "(", end = ")"))
    N1, N2 = 3, 2
    liste_de_listes = []
    for i in range(N1):
        liste = []
        for i in range(N2):
            liste.append(SignalBase(bdt))
        liste_de_listes.append(liste)

    print(str_liste_de_listes(liste_de_listes))



