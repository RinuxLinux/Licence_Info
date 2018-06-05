#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px13-2

def conjugue(verbe):
	ps = 'je tu il nous vous ils'.split()
	ip1 = 'e es e ons ez ent'.split()
	return [ps[x] + ' ' + verbe[:-2] + ip1[x] for x in range(0,6)]
	
v = 'tirer'
print conjugue(v)
