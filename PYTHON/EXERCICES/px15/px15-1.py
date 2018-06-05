#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px15-1

def RomDec(R):
	N = 0
	for x in range(len(R)-1):
		if R[x] < R[x+1]: N-= R[x]
		else: 
			N+= R[x]
	N += R[-1]
	return N

conv = {'C':100,'D':500,'I':1,'M':1000,'L':50,'V':5,'X':10}


while 1:
	R = raw_input('Chiffre romain: ').upper()
	if R in ['q','exit']: break
	R = [conv[x] for x in R.upper()]
	print R
	print RomDec(R)

raw_input('pause')


