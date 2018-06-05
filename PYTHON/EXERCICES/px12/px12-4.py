#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px12-4

# Recoder px10-4 selon approche fonctionnelle

########
#px10-4#
########

#Soit M = []; coder a partir de M:
# [[1,1,1...1],[2,4,8...],etc

M = []
M.append([[x**i for i in range(1,11)] for x in range(1,6)])
print M
