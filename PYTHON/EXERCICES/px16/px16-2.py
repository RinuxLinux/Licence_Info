#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px16-2

def decorticage(mot):
	decorticage = {}
	for lettre in mot:
		decorticage[lettre] = decorticage.get(lettre,0)+1
	return decorticage

mot = 'désespérés'
mot2 = 'salsifis du samedi'
print decorticage(mot)
print decorticage(mot2)
