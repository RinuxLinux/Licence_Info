#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px12-1

"Convertir expression suivante en une	"
"construction 'for' standard générant	"
"exactement le même résultat:		"
"	L = []				"
"	for Z in'abcd': L += [Z.upper()]"

L = [Z.upper() for Z in 'abcd']
print L
 
