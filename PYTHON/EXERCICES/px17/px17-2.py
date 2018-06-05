#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px17-2

def traduis(dic, phrase):
	trad = []
	for mot in phrase.split():
		try:	
			trad += [dic[mot]]
		except:
			x = raw_input('Traduis-moi "%s": ' %mot)
			dic[mot] = x
			trad += [dic[mot]]
	return ' '.join(trad)

FA =  {'boit': 'drinks', 'cherche': 'seeks', 'le': 'the', 'la': 'the', 'mort': 'dead', 'bonne': 'good', 'est': 'is', 'hamster': 'hamster', 'chat': 'cat', 'mange': 'eats', 'gros': 'big', 'mère': 'mother', 'un': 'a', 'soupe': 'soup', 'chien': 'dog', 'petit': 'little', 'ta': 'your'}
AF = {}
for x in FA.keys(): AF[FA[x]] = x
print AF
print FA

while 1:
	phrase = raw_input('Quelle phrase : ')
	if phrase in ['q','exit']: break
	print traduis(AF, phrase)
	print AF


