#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px12-3

# Recoder px10-1 et px10-3 selon approche fonctionnelle

########
#px10-1#
########

#Soit Z = []; coder M → [[1,2,3],[4,5,6]]. Generaliser.

Z = []
M=[[i+j for i in range(1,4)] for j in [0,3]]
print 'M ', M

"Z ne me sert a rien mais tant pis."
Z = []
n = 4 #ligne
m = 3 #colonne
M = [[i+j for i in range(1,n+1)] for j in range(0,n*m,n)]
print 'M ', M

########
#px10-3#
########

#Coder la transposition de M → [[1,4],[2,5],[3,6]]. Generaliser.

M = [[1,2,3],[4,5,6]]
transposed = [[M[i][j] for j in range(0,3)] for i in [0,1]]
print 'transposed ', transposed

M = [[1,2,3],[4,5,6]]
transposed = [[row[i] for row in M] for i in range(3)]
print 'transposed ', transposed

transposed = [[M[i][j] for j in range(0,3)] for i in [0,1]]
print 'transposed ', transposed

M = [[1,2,3],[4,5,6]]
m=[]
for j in range(0,3):
	m.append([M[i][j] for i in range(0,2)])
	
print 'm ',m
print 'M ',M
raw_input('stop')
