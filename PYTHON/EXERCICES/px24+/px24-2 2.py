#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px24-2

from Tkinter import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ variables globales
compteur = 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ animation
def position(click):
    afficheur ['text'] = "%s, %s" % (click.x, click.y)

def dessine(event):
    couleur = switch()
    x, y = event.x, event.y
    ew = event.widget
    r = 12.5
    ew.create_rectangle(x-r,y-r,x+r,y+r, fill=couleur, outline=couleur)

def switch():
    if compteur %2 == 0: return 'green'
    else: return 'red'

def compte():
    global compteur
    compteur += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ handlers
def manager(event):
    compteur = compte()
    position(event)
    dessine(event)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ widgets
top = Tk()
C = Canvas(top, width=400, height=400, bg="light yellow")
C.pack()
C.bind("<Button-1>", manager)
afficheur = Label(top)
afficheur.pack()
Button(top, text='Fermer', command=top.destroy).pack()
top.mainloop()


    




