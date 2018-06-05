#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px13-4

ps = 'je tu il nous vous ils'.split()
ip1 = 'e es e ons ez ent'.split()
v = 'filer rigoler conjuguer'.split()
conjugue = []

conj = [[ps[x] + ' ' + v[y][:-2] + ip1[x] for x in range(0,6)] for y in range(len(v))]
print conj

