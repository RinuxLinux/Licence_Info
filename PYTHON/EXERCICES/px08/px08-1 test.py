#! /usr/bin/env python
#-*-coding: utf-8 -*-
def mois(x):
	for value in moisDict:
		x = key
	return x

erreurs=[['Hiroshima',1945,'aout',6],['Nagasaki',1945,'aout',9]]

moisDict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'aout', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

#month
jour1 = erreurs[0][3]
jour2 = erreurs[1][3]
mois1 = erreurs[0][2]
mois2 = erreurs[1][2]
annee1 = erreurs[0][1]
annee2 = erreurs[1][1]

#tout1 = annee1,mois(mois1),jour1
#tout2 = annee2,mois(mois2),jour2

print mois(mois1)
print mois(mois2)
print jour1
print jour2


#ajout 0
if len(str(jour1)) == 1: erreurs[0][3] = 0 + erreurs[0][3] 
if len(str(jour2)) == 1: erreurs[1][3] = 0 + erreurs[1][3]

print erreurs[0][3]


print tout1
print tout2

