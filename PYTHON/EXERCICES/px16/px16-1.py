#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px16-1

mot = 'anticonstitutionnellement'
decorticage = {}
for lettre in mot:
	decorticage[lettre] = decorticage.get(lettre,0)+1
print decorticage 
