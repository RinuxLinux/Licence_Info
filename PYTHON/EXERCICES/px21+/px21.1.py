#! /usr/bin/env python
#-*-coding: utf-8 -*-
# Renaud Lizot
# 14509956
# px21.1

def valeur(event): val.configure(text=str(eval(express.get())))

from math import *
from Tkinter import *
top = Tk()
express = Entry(top)
express.bind("<KP_Enter>", valeur)
express.bind("<Return>", valeur)
express.pack()
val = Label(top)
val.pack()
top.mainloop()


# key binding: <KP_Enter> keypad enter (numpad)
# key binding: <Return> Entrée
