#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px13-3

ps = 'je tu il nous vous ils'.split()
ip1 = 'e es e ons ez ent'.split()
v = 'filer rigoler conjuguer'.split()
conj = []

for y in range(len(v)):
	temp = []
	for x in range(len(ps)):
		temp.append(ps[x] + ' ' + v[y][:-2] + ip1[x])
	conj.append(temp)
print conj

