#! /usr/bin/env python
# -*-coding: utf-8 -*-
# px10-2

def col2(x):
	extrait = []	
	for i in range(len(x[0])):
		extrait += [x[1][i-1]]
	return extrait

def col3(M):
	extrait2 = []	
	for i in range(col):
		extrait2 += [M[1][i]]
	return extrait2

M = [[1,2,3],[4,5,6]]
row = 2
col = 3
#extrait = []
#extrait2 = []
print M
print col2(M)
print M
print col3(M)

