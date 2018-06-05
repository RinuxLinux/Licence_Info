#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
#[px23-1]
#variante de couleur, fonction de la parité": modifier le code ci-dessus pour afficher un disque de
#couleur rouge si l'abscisse du clic est paire, et verte si elle est impaire.

# Handler ?
def manager(event) :
	position(event)
	dessine(event)

def position(click) :
	afficheur ['text'] = "%s, %s" % (click.x, click.y)
	
def dessine(event):
	x, y = event.x, event.y
	ew = event.widget
	r = 10
	#if (x/2. - x/2) == 0 : couleur = 'red'
	if x % 2 : couleur = 'red'
	else: couleur = 'green'
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