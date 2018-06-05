#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px27-1

def pilote(fichier, dex) :
	flux = open(fichier, 'r')
	for n, ligne in enumerate(flux) :
		dex = indexe(dex, ligne.split(), n + 1)
	flux.close()
	prd(dex)
	return dex

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

def nettoie(x) : return x

def prd(d) :
	for c in sorted(d) :
		print '\t', c, ':', d[c]

stoplist = 'ce de du en le la mais on ou par pas pour qui un une'.split()
pilote('indexe-moi', {})
