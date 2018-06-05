#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# test

# Handler ?
def position(click) : afficheur ['text'] = '%x, %x' % (click.x, click.y)

from Tkinter import *

# fenetre
top = Tk()

#zone
zone = Frame(top, width=300, height=250, bg="bisque")
zone.bind("<Button-1>", position)
zone.bind("<Button-3>", position)
zone.pack()

#afficheur
afficheur = Label(top)
afficheur.pack()

#Bouton Fermer
button = Button(top, text='Fermer', command=top.destroy)
button.pack()

top.mainloop()
