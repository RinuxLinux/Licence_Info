#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px26-1
# jouer avec X, Y, pas d'angle (1-10), create_text() pour ajouter +1/-1 sur axe ord

from Tkinter import *
from math import *

def pixel(w, x, y, c):								# width, abs, ord, couleur
	w.create_rectangle(x, y, x, y, fill=c, outline=c)

def scale(val): return round(val * H/3, 2) 			# scaling

T = Tk()											# set up master widget
T.title('y = sin(x)')
W = 300
H = 300
F = Canvas(T, width=W, height=H, bg='light yellow')
F.pack()
Button(T, text='Fermer', command=T.destroy).pack()

X = W / 6												# horizontal offset
Y = H / 2												# vertical offset
F.create_line(X/2, Y, W-X, Y) 							# x axis
F.create_line(X, X, X, H - 20) 							# y axis
F.create_text(X/2 + 10, Y - 10, text='0') 				# cartesian origin
F.create_text(X-10, X, text='+1')						# +1 sur axe ord
F.create_text(X-10, H-20, text='-1')					# -1 sur axe ord

for angle in xrange(0, int(radians(360) * 100), 5): 		# complete revolution
	x = angle / 100. 									# yields abscissa
	y = scale(sin(x)) + Y 								# and ordinate
	x = x * 20 + X 										# scaling
	pixel(F, x, y, 'red') 								# plot point

T.mainloop()

# scaling : zoomer y x100 x (hauteur fenetre)/3. Arrondir a 2 decimale pres.
# offsetting : decaler y de sorte qu'il se trouve a mi-hauteur de la fenetre ; d'ou : +H/2
