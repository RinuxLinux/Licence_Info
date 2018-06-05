#! /usr/bin/env python
# px06-3
# LIZOT Renaud
# 14509956

from turtle import *

def polygone(taille, nb_cotes, couleur):
	for x in range(nb_cotes):
		color(couleur)		
		forward(taille)
		left(360/nb_cotes)
	return

def nb_cote():
	while True:
		try:
			x = int(raw_input('Nombre de cotes (entier superieur ou egal a 3): '))
			break
		except:
			print 'Veuillez entrer un nombre entier superieur ou egal a 3'
			pass
	return x
	
def isSup(x):
		if x < 3 : return False
		else:
			return True

#taille
while True:
	try:
		t = int(raw_input('Quelle taille: '))
		break
	except:
		print 'Veuillez entrer un nombre entier'
		pass

# n cotes
n = nb_cote()
Sup = isSup(n)
while Sup is False:
	n = nb_cote()
	Sup = isSup(n)
	
#couleur
while True:
		try:
			c = raw_input('Quelle couleur (in english please!): ')
			color(c)
			reset()
			break
		except:
			print 'Veuillez choisir une couleur en anglais (ex.: red, yellow, green, blue, etc.)'
			pass

polygone(t, n, c)
done()
