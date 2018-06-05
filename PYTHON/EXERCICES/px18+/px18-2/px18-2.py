#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px18-2

# Opérations
def affecte(valeur, adresse) : m[adresse] = valeur
def divise(x, y, adresse): m[adresse] = m[x] / m[y]
def ajoute(x, y, adresse): m[adresse] = m[x] + m[y]
def encore(adresse): m['pc'] = adresse

# Séquenceur
def run(fois):
	for x in range(4*fois):
		a = m['pc']
		apply(op[m[a][0]], m[a][1:])
		if m[a][0] !=3: m['pc'] += 4
	return m[1000]						

# Définitions m et op		
m = {}
m[2997] = [1, 1, 1000]				# placer r initial = 1 en 1000
m[3001] = [1, 2, 1020]				# placer diviseur = 2 en 1020
m[3005] = [1, 3006, 2000]			# placer carré en 2000
m[3009] = [1, 3010, 2001]			# placer tours en 2001
m[3013] = [2, 2000, 1000, 1010]			# diviser n/r
m[3017] = [4, 1000, 1010, 1010]			# ajouter r + n/r
m[3021] = [2, 1010, 1020, 1000]			# diviser (r+n/r)/2
m[3025] = [3, 3013]				# retour à m[3013]
m['pc'] = 2997

op = {1: affecte, 2: divise, 3: encore, 4: ajoute}

# Nombre
m[3005][1] = float(raw_input('Nombre: '))
# Tours:
m[3009][1] = int(raw_input('Nombre de tours: '))

print run(m[3009][1])

