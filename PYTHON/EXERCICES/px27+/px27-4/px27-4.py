#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px27-4
# modifier indexe-moi : "global", ("grosse")
# observer les effets et adapter le code.


# CHANGEMENT DE REPERTOIRE DE TRAVAIL
from os import getcwd, chdir
chemin = getcwd() + '/wdir'
chdir(chemin)

# VARIABLES GLOBALES
ponctuation = '(, . ")'

### STOP.LIST ###
# CREER STOP.LIST
def put_list(liste) :
	liste = liste.split()
	flux = open('stop.list','w')
	for mot in liste :
			flux.write(mot + '\n')
	flux.close()
	return
	
# LIRE STOP.LIST
def get_list(fichier) :
	put_list("ce de du en le la mais on ou par pas pour qui un une c'est dans s'en plus qu'elle")
	flux = open(fichier,'r')
	stoplist = flux.read().split()
	flux.close()
	return stoplist

# FONCTIONS AUXILLIAIRES
def nettoie(mot):
	for i in range(len(mot)):
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
stoplist = get_list('stop.list')
pilote('indexe-moi', {})
