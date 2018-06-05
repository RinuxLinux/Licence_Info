#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px12-2

# convertir expression [[x*y for x in [2,3]] for y in [5,6,7]] en construction 'for' standard
# resultat : [[10,15],[12,18],[14,21]]

L = []

L = [[x*y for x in [2,3]] for y in [5,6,7]] 
print L
