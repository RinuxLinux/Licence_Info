#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px19-3

from Tkinter import *

top = Tk()
texte = "Ceci est un test.\nJe sais que:\n-les commandes Tkinter sont CASE SENSITIVE\n-les accents sont gérés\n-les nouveaux messages s'affichent dans la même fenêtre tant qu'on ne quitte pas la fenêtre ou Tkinter (?)\n-fg = foreground, plusieurs couleurs au choix\n-si top est clair, bottom ne marche pas (bah oui... cf début de code)"

message = Label(top, text=texte, fg='blue')
message.pack()

# fonction dans python
# pourquoi fenêtre ne s'affiche pas en executable?

top.mainloop()

