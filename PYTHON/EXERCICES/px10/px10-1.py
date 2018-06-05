#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px10-1

Z = []
M = []
row = 3
col = 5

Z= [i for i in range(1,row*col+1)]
#M = [[0 for i in range(col)] for j in range(row)]
print 'Z ', Z

x = 0
while x+col <= len(Z):
	M += [Z[x:x+col]]
	x = x + col
	
print 'M ', M

