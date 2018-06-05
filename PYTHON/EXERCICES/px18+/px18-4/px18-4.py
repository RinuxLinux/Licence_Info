#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px18-4

# Opérations
def affecte(valeur, adr1, adr2) : m[adr1] = valeur
def divise(x, y, adresse): m[adresse] = m[x] / m[y]
def ajoute(x, y, adresse): m[adresse] = m[x] + m[y]
def encore(adresse): m['pc'] = adresse

# Séquenceur
def run(fois):
	resultat = []
	for x in range(4*fois):
		a = m['pc']
		apply(op[m[a][0]], m[a][1:])
		if a in [2001, 2013] : resultat.append(m[3000])
		if m[a][0] !=3: m['pc'] += 4
	return resultat						
 
# Définitions		
m = {}
m[1997] = [1, 1, 2999, 3000]				
m[2001] = [1, 0, 3000, 2004]				
m[2005] = [1, 1, 3001, 3001]			
m[2009] = [4, 3000, 3001, 3002]		
m[2013] = [2, 3001, 2999, 3000]		
m[2017] = [2, 3002, 2999, 3001]		
m[2021] = [3, 2009]				
m['pc'] = 1997

op = {1: affecte, 2: divise, 3: encore, 4: ajoute}

# Tours:
tours = int(raw_input('Nombre de tours: '))

print run(tours)
