#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px11-1

def pluriel(mot) :
	exceptions = ['oeil', 'yeux', 'œil', 'yeux', 'ail', 'aulx', 'vieil', 'vieux', 'ciel', 'cieux', 'aïeul', 'aïeux']
	if mot in exceptions : return exceptions[exceptions.index(mot) + 1]
	elif mot in ['bleu', 'pneu', 'emeu', 'bancal', 'banal', 'portail', 'étal', 'serval', 'caracal', 'régal', 'naval', 'glacial', 'natal', 'bal', 'carnaval', 'chacal', 'festival', 'récital'] : return mot + 's'
	elif mot in ['hibou', 'pou', 'caillou', 'genou', 'bijou', 'joujou', 'chou'] : return mot + 'x'
	elif mot in ['bail', 'corail', 'émail', 'soupirail', 'travail', 'vantail', 'vitrail', 'bétail', 'portail'] :
		if mot == 'bétail' : return 'bestiaux'
		else : return mot[0:-2] + 'ux'
	else:
		if mot[-3:] == 'eau' : return mot + 'x'
		elif mot[-3:] in ['eil', 'iel', 'eul', 'ail', 'uil'] : return mot + 's'
		else :
			if mot[-2:] == 'al' : return mot[0:-2] + 'aux'
			elif mot[-2:] == 'eu': return mot + 'x'
			elif mot[-2:] in ['ou', 'au', 'el', 'il', 'ru', 'tu', 'pu', 'su', 'du', 'lu', 'vu', 'nu', 'mu'] : return mot + 's'
			else :
				if mot[-1] in ['z', 'x', 's'] : return mot
				else: return mot + 's'

while 1 :
	mot = raw_input('Mot:      ').lower()
	if mot.lower() in ['q', 'exit', 'quit'] : break
	print 'Pluriel: ', pluriel(mot)
