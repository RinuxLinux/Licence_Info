#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px24-3

from Tkinter import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ variables globales
second = False
L = []
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ animation
def position(click):
    afficheur ['text'] = "%s, %s" % (click.x, click.y)

def dessine(event, x, y, a, b):
    #x, y = event.x, event.y
    ew = event.widget
    ew.create_rectangle(x, y, a, b, fill='red', outline='red')

def record(event):
    global L
    if len(L) > 3: L = []
    x, y = event.x, event.y
    L.append(x)
    L.append(y)
    return L

def compte():
    global compteur
    compteur += 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ handlers
def manager(event):
    global second, L
    if second is False:
        position(event)
        record(event)
        second2 = True
    if second is True:
        position(event)
        record(event)
        dessine(event, L[0], L[1], L[2], L[3])
        second2 = False
    second = second2
    print L
        

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ widgets
top = Tk()
C = Canvas(top, width=400, height=400, bg="light yellow")
C.pack()
C.bind("<Button-1>", manager)
afficheur = Label(top)
afficheur.pack()
Button(top, text='Fermer', command=top.destroy).pack()
top.mainloop()