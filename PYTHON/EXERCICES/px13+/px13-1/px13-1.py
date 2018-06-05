#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px13-1

def conjugue(verbe, personne):
	ps = 'je tu il nous vous ils'.split()
	ip1 = 'e es e ons ez ent'.split()
	return ps[personne-1] + ' ' + verbe[:-2] + ip1[personne-1]
	
v = 'tirer'
p = 1
print conjugue(v, p)
print ''
print "Pour tous les tester d'un coup: for p in range(1,7) : print conjugue(v, p)"
for p in range(1,7) : print conjugue(v, p)

