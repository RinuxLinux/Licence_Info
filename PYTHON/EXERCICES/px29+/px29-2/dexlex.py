#! /usr/bin/env python
#-*-coding : utf-8 -*-
# Renaud Lizot
# 14509956
# px29-1 dexlex

from os import chdir, getcwd
from urllib import urlopen


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


def dec_enc(mot, charset): 
	try: 
		return mot.decode(charset).encode('utf-8')
	except:
		t = []
		for m in mot:
			t.append(unicode(m, errors='ignore').encode('utf-8'))
		return ' '.join(t)


def get_charset(url): 
	try:
		return dict(urlopen(url).info())['content-type'].split()[1].split('=')[1]
	except: 
		flux = urlopen(url)
		data = flux.read()
		flux.close()
		exclusion = '= " >'
		if data.find('charset=') != -1: 
			x = data[data.find('charset=')+8:data.find('charset=')+20]
			for ex in exclusion:
				x = x.replace(ex, ' ')
			return x.split()[0]
		else: return 'utf-8'


def get_files(argv, option): return argv[1]


def get_hlinks(urls):
	list_urls = []
	for url in urls:
		list_urls.append(url)
		flux = urlopen(url)
		data_list = flux.read().split('"')
		flux.close()
		for el in data_list:
			if el.endswith('href='): list_urls.append(data_list[data_list.index(el)+1])
	list_urls = tri_hlinks_doublons(list_urls)
	list_urls = tri_hlinks_junk(list_urls)
	list_urls = get_urls(list_urls)
	return list_urls


def get_list(fichier) :
	put_list('go.list', "south park mkv South Park")
	put_list('stop.list', "ce de du en # le la les je tu il elle nous vous ils elles et donc or ou mais n' j' qu' l' on ou par pas pour qui un une c'est dans s'en plus qu'elle '\xc2\xab', '\xc2\xbb'")
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
	#print 'charset \t', charset, '\t reference \t', reference
	if switch is 'url':
		mots = trad_code_html(nettoie_html(mots)).split()
	for mot in mots:
		mot = nettoie(mot.lower()) if switch is 'file' else nettoie(dec_enc(mot, charset))
		if option is 'go':
			if mot in liste: dex = ajoute(dex, mot, reference)
		else:
			if mot not in liste: dex = ajoute(dex, mot, reference)
	return dex


def nettoie(mot):
	ponctuation = '(, . " ) : ; ? ! [ ] / | { } -'
	exclusions = ["c'", "d'", "j'", "l'", "m'", "n'", "s'", "t'", "y'"]
	tri = ['\xc2\xab', '\xc2\xbb']
	try:
		for i in range(len(mot)):
			if mot[-1] in ponctuation : mot = mot[:-1]
			if mot[0] in ponctuation : mot = mot[1:]
		for ex in exclusions:
			if mot.startswith(ex): mot = mot.replace(ex, '')
		for t in tri:
			if mot.find(t): mot = mot.replace(t, ' ')
		return mot
	except:
		return '#'


def nettoie_html(data):
	p = {'<script' : '</script>', '<' : '>', '<style>' : '</style>'}
	x = y = 0
	while x + y != -2:
		for element in p.keys():
			x = data.find(element)
			y = data.find(p[element])
			if x > y : 
				if y != -1: data = data.replace(data[0:y+len(p[element])], ' ')
			if x < y and x != -1:
				if y != -1: data = data.replace(data[x:y+len(p[element])],' ')
				else: data = data.replace(ligne[x:], ' ')
	return data	


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
	d = {'\xc3\xa0' : ['&agrave;', '\xe0'], '\xc3\xa2' : ['&acirc;'], '\xc3\xa9' : ['&eacute;', '\xe9', '%C3%A9'], '\xc3\xa8' : ['&egrave;', '\xe8'], '\xc3\xaa' : ['&ecirc;', '\xea'], '\xc3\xbb' : ['&ucirc;'], '\xc3\xb9' : ['&ugrave;'], '\xc3\xae' : ['&icirc;', '\xee'], '\xc3\xb4' : ['&ocirc;'], '\xc3\xa7' : ['&ccedil;', '\xe7'], '\xc3\xa6' : ['&aelig;'], '\xc3\xab' : ['&euml;'], '\xc3\xbc' : ['&uuml;'], '\xc3\xaf' : ['&iuml;'], '\xc5\x93' : ['&oelig;'], '"' : ['&laquo;', '&raquo;', '\xc2\xab', '\xc2\xbb'], '\xe2\x82\xac' : ['&euro;'], ' ' : ['&nbsp;', '&#160;', '\xe2\x80\xa6', '\xef\xbb\xbf'], "'" : ['&#8217;', '&#039;', '&#39;', '&rsquo;', '\xe2\x80\x99']}
	for i in range(len(d)): 
		valeurs = d.items()[i][1]
		cle = d.items()[i][0]
		for v in valeurs:
			if mot.find(v) != -1 : mot = mot.replace(v, cle)
	return mot


def tri_hlinks_doublons(liste):
	no_duplicate_list = []
	for x in liste:	
		if x not in no_duplicate_list: no_duplicate_list.append(x)
	return no_duplicate_list


def tri_hlinks_junk(list_urls):
	exclu_end = '.css .jpg .js .ico .gif .png .cx .pdf .mobi'.split()
	exclu_start = 'mailto:'.split()
	hlink_sorted = list_urls
	# terminaisons
	for link in list_urls:
		for e in exclu_end: 
			if link.endswith(e): hlink_sorted.remove(link)
	# mailto:
	for link in hlink_sorted:
		for s in exclu_start: 
			if link.startswith(s): hlink_sorted.remove(link)
	return hlink_sorted



