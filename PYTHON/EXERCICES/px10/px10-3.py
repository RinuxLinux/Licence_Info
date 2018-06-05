#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px10-3

m = [[1,2,3],[4,5,6]]
p = [[1,4],[2,5],[3,6]]
row = 2
col = 3
m2 = []

for j in range(0,3):
	for i in range(0,2):
		m2.append(m[i][j])

print m2

transposed = []
matrix = [[1,2,3],[4,5,6]]
for i in range(3):
	transposed.append([row[i] for row in matrix])

print transposed

