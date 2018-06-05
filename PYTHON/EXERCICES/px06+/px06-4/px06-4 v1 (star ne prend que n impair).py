#! /usr/bin/env python
# px06-4 v1
# LIZOT Renaud
# 14509956

from turtle import *

def star(taille, nb_cote, couleur):
	for x in range(nb_cote):
		color(couleur)		
		forward(taille)
		left(720.0/nb_cote)
	return taille, nb_cote, couleur

def branches():
	while True:
		try:
			n = int(raw_input('Nombre de cotes (entier impair superieur a 4): '))
			break
		except:
			print 'Veuillez entrer un nombre entier impair superieur a 4'
			pass
	return n

def isImpair(x):
	if x%2 == 0 : return False
	else:
		return True
	
def isInf(x):
	if x > 4 : return False
	else:
		return True
	
# taille
while True:
	try:
		t = int(raw_input('Taille: '))
		break
	except:
		print 'Veuillez entrer un nombre entier'
		pass

# Couleur
while True:
	try: 
		c = raw_input('Couleur (en anglais, please!): ')
		color(c)
		reset()
		bye()
		break
	except:
		print 'Veuillez donner une couleur en anglais (ex.: red, blue, green, yellow, etc.)'
		pass
		
# Branches
n = branches()

# controles:
Inf = isInf(n)
impair = isImpair(n)
while Inf is True or impair is False:
	n = branches()
	impair = isImpair(n)
	Inf = isInf(n)

# C'est parti

reset()
star(t, n, c)
done()
