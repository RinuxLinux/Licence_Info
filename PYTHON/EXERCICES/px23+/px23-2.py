#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
#[px23-2]
#modifier encore le code pour dessiner en 4 couleurs"selon la conjonction des parités de l'abscisse
#et de l'ordonnée du clic.

# Handler ?
def manager(event) :
	position(event)
	dessine(event)

def position(click) :
	afficheur ['text'] = "%s, %s" % (click.x, click.y)

def colour(x, y):
	#x, y = event.x, event.y
	if x % 2 is 0:
		if y % 2 is 0: couleur = 'green'		#pair pair
		else: couleur ='blue'					#pair impair
	if x % 2 is not 0 :							
		if y % 2 is not 0 : couleur = 'red'		#impair impair
		else: couleur = 'pink'					#impair pair

def dessine(event):
	x, y = event.x, event.y
	ew = event.widget
	r = 10
	if x % 2 is 0:
		if y % 2 is 0: couleur = 'green'		#pair pair
		else: couleur ='blue'					#pair impair
	if x % 2 is not 0 :							
		if y % 2 is not 0 : couleur = 'red'		#impair impair
		else: couleur = 'pink'					#impair pair
	ew.create_oval(x - r, y - r, x + r, y + r, fill=couleur, outline="")

from Tkinter import *

top = Tk()
# canvas
C = Canvas(top, width=400, height=400, bg="light yellow")
C.pack()
C.bind("<Button-1>", manager)
# afficheur
afficheur = Label(top)
afficheur.pack()

top.mainloop()


# j'aurai bien aimé faire une fonction couleur mais je pige pas encore bien comment ça marche ces histoires de click/event