#! /usr/bin/env python
# px06-2 version 1: fonction arite 0
# LIZOT Renaud
# 14509956


def instructions():
	while True:
		try:
			taille = int(raw_input('Taille: '))
			break
		except:	
			print 'Veuillez entrer un nombre entier'
			pass
	couleur = raw_input('Choisir une couleur entre bleu, rouge et vert: ').lower()
	while couleur not in ['rouge', 'bleu', 'vert'] : couleur = raw_input('Veuillez choisir entre BLEU, ROUGE et VERT: ').lower()
	if couleur == 'rouge' : couleur = 'red'
	if couleur == 'bleu' : couleur = 'blue'
	if couleur == 'vert' : couleur = 'green'
	for x in range(4):
		color(couleur)
		forward(taille)
		left(90)
	return taille, couleur

from turtle import *
instructions()
done()
