#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px25-5
# ajouter nouvelle fonctionnalité: 
# clic dans Canvas déplace boule en ce point

from Tkinter import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ variables globales
D = 50 					# diamètre
X, Y = 10, 10 			# coordonnées initiales
h_canvas = 500
w_canvas = 400
w_boule = 5

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ animation
def avance(delta_X, delta_Y) :
	global D, X, Y
	X, Y = X + delta_X, Y + delta_Y
	C.coords(boule, X, Y, X + D, Y + D)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ handlers
def place(event):
	global D
	X, Y = event.x, event.y
	C.coords(boule, X-D/2., Y-D/2., X + D/2., Y + D/2.)
		
def bas() : avance(0, 15)
def haut() : avance(0, -15)
def droite() : avance(15, 0)
def gauche() : avance(-15, 0)
def reinit() :
	global h_canvas, w_canvas,w_boule, D
	C.coords(boule, w_canvas-w_boule-D, h_canvas-w_boule-D, w_canvas-w_boule, h_canvas-w_boule)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ widgets
top = Tk()
top.title("animation manuelle")

C = Canvas(top, bg='light yellow', height=h_canvas, width=w_canvas)
boule = C.create_oval(X, Y, X + D, Y + D, width=w_boule, fill='blue')
C.pack(side=LEFT)

C.bind("<Button-1>", place)

Button(top, text='gauche', command=gauche).pack()
Button(top, text='droite', command=droite).pack()
Button(top, text='monte', command=haut).pack()
Button(top, text='descend', command=bas).pack()
Button(top, text='stop', command=top.destroy).pack(side=BOTTOM)
Button(top, text='Reinitialiser', command=reinit).pack(side=BOTTOM)



top.mainloop()
