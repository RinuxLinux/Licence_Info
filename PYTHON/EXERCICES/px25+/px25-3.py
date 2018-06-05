#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px25-3
# changer valeurs de deplacement dans handlers

from Tkinter import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ variables globales
D = 50 					# diamètre
X, Y = 10, 10 			# coordonnées initiales

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ animation
def avance(delta_X, delta_Y) :
	global X, Y
	X, Y = X + delta_X, Y + delta_Y
	C.coords(boule, X, Y, X + D, Y + D)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ handlers
def bas() : avance(0, 15)
def haut() : avance(0, -15)
def droite() : avance(15, 0)
def gauche() : avance(-15, 0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ widgets
top = Tk()
top.title("animation manuelle")

C = Canvas(top, bg='light yellow', height=500, width=400)
boule = C.create_oval(X, Y, X + D, Y + D, width=5, fill='blue')
C.pack(side=LEFT)

Button(top, text='gauche', command=gauche).pack()
Button(top, text='droite', command=droite).pack()
Button(top, text='monte', command=haut).pack()
Button(top, text='descend', command=bas).pack()
Button(top, text='stop', command=top.destroy).pack(side=BOTTOM)

top.mainloop()
