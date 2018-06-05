#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px11-2

def pluriel(mot):
	exceptions = ['oeil', 'yeux', 'œil', 'yeux', 'ail', 'aulx', 'vieil', 'vieux', 'ciel', 'cieux', 'aïeul', 'aïeux']
	if mot in exceptions: return exceptions[exceptions.index(mot) + 1]
	elif mot in ['bleu', 'pneu', 'emeu', 'bancal', 'banal', 'portail', 'étal', 'serval', 'caracal', 'régal', 'naval', 'glacial', 'natal', 'bal', 'carnaval', 'chacal', 'festival', 'récital']: return mot + 's'
	elif mot in ['hibou', 'pou', 'caillou', 'genou', 'bijou', 'joujou', 'chou']: return mot + 'x'
	elif mot in ['bail', 'corail', 'émail', 'soupirail', 'travail', 'vantail', 'vitrail', 'bétail', 'portail']:
		if mot == 'bétail': return 'bestiaux'
		else: return mot[0:-2] + 'ux'
	else:
		if mot[-3:] == 'eau': return mot + 'x'
		elif mot[-3:] in ['eil', 'iel', 'eul', 'ail', 'uil']: return mot + 's'
		else:
			if mot[-2:] == 'al': return mot[0:-2] + 'aux'
			elif mot[-2:] == 'eu': return mot + 'x'
			elif mot[-2:] in ['ou', 'au', 'el', 'il', 'ru', 'tu', 'pu', 'su', 'du', 'lu', 'vu', 'nu', 'mu']: return mot + 's'
			else:
				if mot[-1] in ['z', 'x', 's']: return mot
				else: return mot + 's'

mots = ["hors-d'œuvre", 'bal', 'régal', 'banal', 'canal', 'étal', 'pascal', 'portail', 'bétail', 'travail', 'œil', 'écœuré', 'hameçon', 'ex-æquo', 'niño', 'mépris', 'landau', 'rideau', 'jeu', 'bleu', 'clou', 'genou', 'prix', 'bocal', 'bancal', 'roux', 'pou', 'soleil', 'ciel', 'écureuil', 'fonctionnel', 'fonction', 'auroch', 'riz', 'souris', 'signet', 'long', 'nef', 'blond', 'jockey', 'papa', 'risotto', 'ventru', 'métier', 'aïeul']

print 'Mots:'
print mots
print ' '
print 'Pluriels:'
print [pluriel(x) for x in mots]

