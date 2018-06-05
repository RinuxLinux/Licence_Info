#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px27-2
# adapter le programme px27-1 de sorte que la stoplist soit enregistrée avec un saut de ligne


# CHANGEMENT DE REPERTOIRE DE TRAVAIL
from os import getcwd, chdir
chemin = getcwd() + '/wdir'
chdir(chemin)

# VARIABLES GLOBALES
ponctuation = '(, . ")'
stoplist = "ce de du en le la mais on ou par pas pour qui un une c'est dans s'en plus qu'elle".split()

# STOP.LIST
flux = open('stop.list','w')
for mot in stoplist :
	flux.write(mot + '\n')

flux.close()
flux = open('stop.list','r')
stoplist = flux.read().split()
flux.close()

# FONCTIONS AUXILLIAIRES
def nettoie(mot):
	if mot[-1] in ponctuation : mot = mot[:-1]
	if mot[0] in ponctuation : mot = mot[1:]
	return mot

def indexe(dex, mots, ligne) :
	for mot in mots :
		mot = nettoie(mot)
		if mot.lower() in stoplist : pass
		else : dex = ajoute(dex, mot, ligne)
	return dex

def ajoute(dex, mot, ligne) :
	if mot in dex :
		if ligne in dex[mot] : pass
		else : dex[mot].append(ligne)
	else : dex[mot] = [ligne]
	return dex

def prd(d) :
	for c in sorted(d) :
		print '\t', c, ':', d[c]

# FONCTION PRINCIPALE		
def pilote(fichier, dex) :
	flux = open(fichier, 'r')
	for n, ligne in enumerate(flux) :
		dex = indexe(dex, ligne.split(), n + 1)
	flux.close()
	prd(dex)
	return dex

# APPEL PRINCIPAL
pilote('indexe-moi', {})
