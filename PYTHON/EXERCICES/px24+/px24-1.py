#! /usr/bin/env python
#-*-coding: utf-8 -*-
# px24-1

def manager(event):
    position(event)
    dessine(event)

def position(click):
    afficheur ['text'] = "%s, %s" % (click.x, click.y)

def dessine(event):
    x, y = event.x, event.y
    ew = event.widget
    r = 12.5
    ew.create_rectangle(x-r,y-r,x+r,y+r, fill="yellow", outline="red")

from Tkinter import *

top = Tk()
C = Canvas(top, width=400, height=400, bg="light yellow")
C.pack()
C.bind("<Button-1>", manager)
afficheur = Label(top)
afficheur.pack()
top.mainloop()
