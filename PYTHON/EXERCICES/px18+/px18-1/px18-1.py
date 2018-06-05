#!/usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px18-1

def raccar(n):
	r= 1
	while (n - r**2) != 0 :
		if (r+n/r)/2. == r : 
			return r
		r = (r+n/r)/2.
	return r

n = int(raw_input("Nombre: "))
print raccar(n)

