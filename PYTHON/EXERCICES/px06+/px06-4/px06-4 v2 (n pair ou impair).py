#! /usr/bin/env python
# px06-4 v2
# LIZOT Renaud
# 14509956

from turtle import *

def star(taille, nb_branches, couleur):
	angle = 720./n
	for x in range(nb_branches):
		color(couleur)		
		forward(taille)
		left(angle)
	return
	
def starPair(taille, nb_branches, couleur):
	angle = 720./n
	for x in range(nb_branches/2):
		color(couleur)
		forward(taille)
		left(angle)
	penup()
	forward(taille/2.)
	right(90)
	forward(ba)
	left((180+angle)/2)
	pendown()
	for x in range(nb_branches/2):
		color(couleur)
		forward(taille)
		left(angle)
	return
	
def branches():
	while True:
		try:
			n = int(raw_input('Nombre de branches (entier superieur a 4): '))
			break
		except:
			print 'Veuillez entrer un nombre entier superieur a 4'
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
		c = raw_input('Couleur (en anglais, please!): ').lower()
		color(c)
		reset()
		bye()
		break
	except:
		print 'Veuillez donner une couleur en anglais (ex.: red, blue, green, yellow, etc.)'
		pass
		
# Branches & angle d'attaque de la tortue
n = branches()


# Controles:
Inf = isInf(n)
impair = isImpair(n)

while Inf is True :
	n = branches()
	Inf = isInf(n)
	impair = isImpair(n)

# bloc de calculs pour quand impair is False
from math import *
ac = t*1/2.
angle_gravite = 360.0/n
angle_isocele = (180-angle_gravite)/2.0
# tan B = AC/BA, A etant angle droit
Tan = (tan(radians(angle_isocele)))
ba = ac/Tan
bc = sqrt(ba**2 + ac**2)

if impair is True: 
	star(t,n,c)
else: 
	starPair(t,n,c)

done()
