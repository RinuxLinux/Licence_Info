#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# test

def position(click) : afficheur ['text'] = '%s, %s' % (click.x, click.y)

from Tkinter import *

# fenetre
top = Tk()

#zone
zone = Frame(top, width=300, height=250, bg="bisque")
zone.bind("<Button-2>", position)
zone.pack()

#afficheur
afficheur = Label(top)
afficheur.pack()

#Bouton Fermer
button = Button(top, text='Fermer', command=top.destroy)
button.pack()

top.mainloop()
