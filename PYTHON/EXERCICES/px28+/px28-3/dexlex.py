#! /usr/bin/env python
#-*-coding : utf-8 -*-
# Renaud Lizot
# 14509956
# px28-3 - dexlex
# module dexlex avec fonctions et donnees globales + coeur du script a part


# CHANGEMENT DE REPERTOIRE DE TRAVAIL
from os import getcwd, chdir
chemin = getcwd() + '/wdir'
chdir(chemin)


# VARIABLES GLOBALES
ponctuation = '(, . " ) : ; ? ! [ ]'


### STOP.LIST ###
# CREER STOP.LIST
def put_list(fichier, liste) :
	liste = liste.split()
	flux = open(fichier,'w')
	for mot in liste :
			flux.write(mot + '\n')
	flux.close()
	return
	
# LIRE STOP.LIST
def get_list(fichier) :
	if fichier == 'stop.list':
		put_list('stop.list', "ce de du en # le la les je tu il elle nous vous ils elles et donc or ou mais ( - , . ) n' j' qu' l' ... .. : ; ? ! [ ] on ou par pas pour qui un une c'est dans s'en plus qu'elle")
	else: 		
		put_list('go.list', "bouts frustration global programme progressivement valeur")
	flux = open(fichier,'r')
	liste = flux.read().split()
	flux.close()
	return liste


# FONCTIONS AUXILLIAIRES
def nettoie(mot) :
	try:
		for i in range(len(mot)) :
			if mot[-1] in ponctuation : mot = mot[:-1]
			if mot[0] in ponctuation : mot = mot[1:]
			if "'" in mot: mot = mot.split("'")[1:]
		return mot.lower()
	except:
		return '#'
		
def indexe(dex, mots, ligne, liste, option) :
	for mot in mots :
		mot = nettoie(mot)
		if option == '-stop' :
			if mot.lower() not in liste : dex = ajoute(dex, mot, ligne)
		if option == '-go' :
			if mot.lower() in liste : dex = ajoute(dex, mot, ligne)			
	return dex
	
def ajoute(dex, mot, ligne) :
	if mot in dex :
		if ligne in dex[mot] : pass
		else : dex[mot].append(ligne)
	else : dex[mot] = [ligne]
	return dex

def borner(m) :
	bornes = []
	borne1 = borne2 = m[0]
	for element in m[1:] :
		if element == borne2 +1 :
			borne2 = element
		else :
			bornes.append(str(borne1) if borne1 == borne2 else '%s-%s' %(borne1, borne2))
			borne1 = borne2 = element
	bornes.append(str(borne1) if borne1 == borne2 else '%s-%s' %(borne1, borne2))
	return ', '.join(bornes)

def prd(d) :
	for c in sorted(d) :
		print '\t', c, ' :', borner(d[c])
