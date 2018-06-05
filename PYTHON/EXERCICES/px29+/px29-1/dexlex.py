#! /usr/bin/env python
#-*-coding : utf-8 -*-
# Renaud Lizot
# 14509956
# px29-1 dexlex

from os import chdir, getcwd
from urllib import urlopen

ponctuation = '(, . " ) : ; ? ! [ ] | { } -'


def ajoute(dex, mot, ligne):
	if mot in dex:
		if ligne in dex[mot] : pass
		else: dex[mot].append(ligne)
	else: dex[mot] = [ligne]
	return dex


def borner(m) :
	bornes = []
	borne1 = borne2 = m[0]
	for element in m[1:] :
		if element == borne2 +1 :
			borne2 = element
		else :
			bornes.append(str(borne1) if borne1 == borne2 else '%s-%s' %(borne1, borne2))
			borne1 = borne2 = element
	bornes.append(str(borne1) if borne1 == borne2 else '%s-%s' %(borne1, borne2))
	return ', '.join(bornes)


def dec_enc(mot, charset): return mot.decode(charset).encode('utf-8')


def get_charset(url): 
	try:
		return dict(urlopen(url).info())['content-type'].split()[1].split('=')[1]
	except: 
		for line in urlopen(url):
			if line.find('<meta') < 0 : continue
			x = line.find('charset=')
			if not x < 0 : return line[x + len('charset='):-2]


def get_files(argv, option): return argv[1]


def get_list(fichier) :
	put_list('go.list', "travail logiciels solution programme informatique python programmation universit\xc3\xa9 paris informatique actualit\xc3\xa9s")
	put_list('stop.list', "ce de du en # le la les je tu il elle nous vous ils elles et donc or ou mais n' j' qu' l' on ou par pas pour qui un une c'est dans s'en plus qu'elle")
	flux = open(fichier,'r')
	liste = flux.read().split()
	flux.close()
	return liste


def get_option(argv): return 'go' if '-go' in argv else 'stop'


def get_urls(argv):
	urls = []
	for i in argv:
		if i.startswith('http://') or i.startswith('https://'): urls.append(i)
		if i.startswith('www.'): urls.append('http://' + i)
	return None if urls == [] else urls
	
	
def indexe(dex, mots, reference, liste, switch, option):
	charset = get_charset(reference) if switch is 'url' else None
	for mot in mots:
		mot = mot.lower()
		if switch is 'url': mot = dec_enc(trad_code_html(mot), charset)
		mot = nettoie(mot)
		if option is 'go':
			if mot in liste: dex = ajoute(dex, mot, reference)
		else:
			if mot not in liste: dex = ajoute(dex, mot, reference)
	return dex


def nettoie(mot):
	exclusions = ["c'", "d'", "j'", "l'", "m'", "n'", "s'", "t'", "y'"]
	try:
		for i in range(len(mot)):
			if mot[-1] in ponctuation : mot = mot[:-1]
			if mot[0] in ponctuation : mot = mot[1:]
		for ex in exclusions:
			if mot.startswith(ex): mot = mot.replace(ex, '')
		return mot
	except:
		return '#'


def nettoie_html(ligne):
	p = {'<script' : '</script>', '<' : '>', '<style>' : '</style>'}
	x = y = 0
	while x != -1 and y != -1:
		for element in p.keys():
			x = ligne.find(element)
			y = ligne.find(p[element])
			if x > y : 
				if y != -1: ligne = ligne.replace(ligne[0:y+len(p[element])], ' ')
			if x < y and x != -1:
				if y != -1: ligne = ligne.replace(ligne[x:y+len(p[element])],' ')
				else: ligne = ligne.replace(ligne[x:], ' ')
	return ligne	
	
def prd(d, switch):
	if d == {} : 
		print 'Aucun(s) r\xc3\xa9sultat(s) trouv\xc3\xa9(s)'
		pass
	for c in sorted(d):
		print '\t', c, ' : ', borner(d[c]) if switch is 'file' else ' ; '.join(d[c])


def put_list(fichier, liste) :
	liste = liste.split()
	flux = open(fichier,'w')
	for mot in liste :
			flux.write(mot + '\n')
	flux.close()
	return	
	

def trad_code_html(mot):
	dico = {'&agrave;' : '\xc3\xa0', '&acirc;' : '\xc3\xa2', '&eacute;' : '\xc3\xa9', '&egrave;' : '\xc3\xa8', '&ecirc;' : '\xc3\xaa', '&ucirc;' : '\xc3\xbb', '&ugrave;' : '\xc3\xb9', '&icirc;' : '\xc3\xae', '&ocirc;' : '\xc3\xb4', '&ccedil;' : '\xc3\xa7', '&aelig;' : '\xc3\xa6', '&euml;' : '\xc3\xab', '&uuml;' : '\xc3\xbc', '&iuml;' : '\xc3\xaf', '&oelig;' : '\xc5\x93', '&laquo;' : '"', '&raquo;' : '"', '&rsquo;' : "'", '&euro;' : '\xe2\x82\xac', '&nbsp;' : '|', '&#160;' : '', '&#8217;' : "'"}
	for cle in dico.keys():
		if mot.find(cle) != -1 : mot = mot.replace(cle, dico[cle])
	return mot
