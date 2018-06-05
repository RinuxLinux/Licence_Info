#! /usr/bin/env python
# LIZOT Renaud
# 14509956
# px06-1

from turtle import *
valeur = int(raw_input('Combien de pas pour la tortue? '))
for x in range(4):
     color('blue')
     forward(valeur)
     left(90)
done()

