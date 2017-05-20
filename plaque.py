#!/usr/bin/python
# -*- encoding : iso-8859-15 -*-
# $Id: $

"""
Permet de jouer avec l'encodage des plaques
mineralogiques europeennes.
""" 
import re

__author__= "godzillux"
__date__ = "20 mai 2017"
__version__ = "0.0.0.1"
__credits__ = ""

class Plaque:
    """
    encapsule les fonctions du module.
    """
    def __init__(self, chaine="", numero=-1):
        if(numero != -1):
            self.numero = numero
            self.chaine = "%s%d%s" % int2plaque(numero)
        elif(chaine != ""):
            if(not chk(chaine)):
                raise Exception("La chaine '%s' ne semble pas valide" % (chaine))
            self.chaine = net(chaine)
            self.numero = plaque2int(chaine)
        else:
            raise RuntimeError("impossible de contruire une plaque sans numero ni chaine !")
    def __repr__(self):
        return self.chaine

def net(s):
    """
    nettoie la chaine afin d'etre decodee
    """
    return s.replace(":", "", 2)

"""
Permet d'identifier un double de lettre sur la plaque
"""
LETTRES = re.compile(r"[A-Z]{2}")

def chk(s):
    """
    Verifie que la plaque a decoder est correcte.
    """
    s = net(s)
    if(len(s) != 7):
        return False
    if(re.match(LETTRES, s[0:2]) is None):
        return False
    if(re.match(LETTRES, s[5:7]) is None):
        return False
    return True
    
def int2ascii(x):
    """
    convertit un entier en sa representation ascii
    """
    return chr((x/26)+65) + chr((x%26)+65)

def int2plaque(x):
    """
    convertit un entier en une plaque.
    """
    m=(x%999)+1
    d=(x/999)%676
    g=(x/999/676)%676
    return (int2ascii(g),m, int2ascii(d))

def ascii2int(d):
    """
    convertit les 2 lettres d'une plaque en entier
    """
    return ((ord(d[0])-65)*26) + (ord(d[1])-65)

def plaque2int(x):
    """
    convertit une plaque en entier
    """
    if(len(x)==9):
        (g,m,d) = x.split(":")
    elif(len(x)==7):
        (g,m,d) = (x[0:2], x[2:5], x[5:7])
    else:
        raise Exception("Taille %d de chaine %s non geree" % (len(x), x))
    
    d=ascii2int(d)
    g=ascii2int(g)
    m=int(m)-1
    return m+(999*d)+(999*676*g)

def information():
    """
    Affiche des informations generales pour test.
    """
    print("Analyse les plaques d'Europe")
    nbrPlaque=26*26*26*26*999
    print("nombre de plaque %d" % nbrPlaque)
    print("affichage de la plaque mediane")
    mediane=nbrPlaque/2
    print(mediane)
    #228 488 000
    #676 676 999
    for a in xrange(mediane/2/2/2, mediane/2/2/2+999):
        print(("%s:%03d:%s->" % int2plaque(a)) + str(a))
    print("NA:010:AA->%d" % (plaque2int("NA:010:AA")))

#information()
p = Plaque(chaine="AA:123:AA")
print(p)
p = Plaque(numero=99999)
print(p)
