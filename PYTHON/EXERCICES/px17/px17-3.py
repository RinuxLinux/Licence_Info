#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px17-3

FA =  {'boit': 'drinks', 'cherche': 'seeks', 'le': 'the', 'la': 'the', 'mort': 'dead', 'bonne': 'good', 'est': 'is', 'hamster': 'hamster', 'chat': 'cat', 'mange': 'eats', 'gros': 'big', 'mère': 'mother', 'un': 'a', 'soupe': 'soup', 'chien': 'dog', 'petit': 'little', 'ta': 'your'}
AF = dict(zip(FA.values(),FA.keys()))
espanol = dict(zip(['uno','dos'],[1,2]))
print AF
print espanol
print FA.values()
print FA.keys()

a = FA.values()
b = FA.keys()
test = dict(zip(a,b))
print test
