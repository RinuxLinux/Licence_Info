#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px17-1

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

FA = {'le':'the','chat':'cat'}
while 1:
	phrase = raw_input('Quelle phrase : ')
	if phrase in ['q','exit']: break
	print traduis(FA, phrase)
	print FA
