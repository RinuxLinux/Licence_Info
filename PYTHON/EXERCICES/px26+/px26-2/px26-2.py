#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px26-2
# y = tan(x)

from Tkinter import *
from math import *

def pixel(w, x, y, c):								# width, abs, ord, couleur
	w.create_rectangle(x, y, x, y, fill=c, outline=c)

def position(click) :
	afficheur ['text'] = "%s, %s" % (click.x, click.y)

T = Tk()											# set up master widget
T.title('y = tan(x)')
W = 500
H = 500
F = Canvas(T, width=W, height=H, bg='light yellow')
F.pack()
Button(T, text='Fermer', command=T.destroy).pack()
# afficher coords (pour m'aider à comprendre, je le laisse quand meme)
F.bind("<Button-1>", position)
afficheur = Label(T)
afficheur.pack()

F.create_line(W/2, H-25, W/2, 25) 							# ord
F.create_line(25, H/2, W-25, H/2) 							# abs
F.create_text(W/2 - 10, H/2 - 10, text='0') 				# cartesian origin
F.create_text(W/2, 10, text='y')							# y sur axe ord
F.create_text(W - 10, H/2, text='x')						# x sur axe abs
F.create_text(W - 20, H/2 + 20,text='+360°')				# +360° sur axe abscisse
F.create_text(20, H/2 + 20, text='-360°')					# -360° sur axe abscisse

for angle in xrange(-360,360, 1): 				
	x = angle + W/2								# calcul x + scaling
	y = (tan(radians(angle))*(10) + H/2)		# calcul y + scaling
	y = H - y									# inversion y
	pixel(F, x, y, 'red')						# tracé pixel
	
T.mainloop()

