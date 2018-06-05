#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px24-2

from Tkinter import *



def manager(event):
    compteur = False
    position(event)
    dessine(event, compteur)
    
def position(click):
    afficheur ['text'] = "%s, %s" % (click.x, click.y)

def test(compteur):
    print '1 ', compteur
    if compteur is False: 
        print compteur
        compteur = True
        print compteur
        return 'red'
    if compteur is True:
        print compteur
        compteur = False
        print compteur
        return 'green'
    
def dessine(event, compteur):
    couleur = test(compteur)
    x, y = event.x, event.y
    ew = event.widget
    r = 12.5
    ew.create_rectangle(x-r,y-r,x+r,y+r, fill=couleur, outline="red")


top = Tk()
C = Canvas(top, width=400, height=400, bg="light yellow")
C.pack()
C.bind("<Button-1>", manager)
afficheur = Label(top)
afficheur.pack()
Button(top, text='Fermer', command=top.destroy).pack()
top.mainloop()
