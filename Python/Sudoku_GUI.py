#!/bin/sh

# GUI_1.py
# GUI 
#
# Created by joe yuan on 3/16/11.
# Copyright 2011 Classified. All rights reserved.

# Since last app:
# updated depth search

# Project ideas:
# (In order of dificulty)
# windows .exe version
# hint system (hover pop-up?)
# puzzle generator
# puzzle rating system?


import time
from random import *


try:
    import sys
    from Tkinter import *
except ImportError:
    print 'This Python program was written for python 2.6 using Tkinter.'
    print 'Unfortunately you do not have right packages to run this program.'
    print 'Please let me know about this error =)'
    sys.exit(1)


sys.setrecursionlimit(2000)

class GUI:
    def __init__(self,master):
        frame = Frame(master,width='478',height='328', bg='black')
        frame.grid(column=0,row=0,columnspan=100,rowspan=100)
        
        welcome = Message(root, text="Welcome to the Sudoku Solver!",foreground='green',background='black',justify=CENTER)
        instructions = Message(root, text="Fill in your puzzle here\nYou can hit Tab to navigate the puzzle\n",foreground='white',background='black',width=90,aspect=100)
        welcome.grid(row=0,column=0,columnspan=3,rowspan=4)
        instructions.grid(row=7,column=0,columnspan=3,rowspan=8)
        
        author = Label(root, text="Created by Joe Yuan (C) 2011",foreground='white',background='black',width='40')
        author.grid(row=10,column=0,columnspan=100)
        
        # Testing Menu function:
        #menubar = Menu(master)
        #def Pink(n='black'):
         #   color = 'pink'
        #def Blue(n='black'):
         #   color = 'blue'
        #def Black(n='black'):
         #   color = 'black'
        #File = Menu(menubar, tearoff=0)
        #menubar.add_command(label='Quit',command= lambda: frame.quit())
        #menubar.add_cascade(label="File", menu=File)
        
        c = Canvas(master,width=300,height=300,background='black')
        c.grid(row=1,column=4,rowspan=9,columnspan=9) 

        # vertical
        c.create_line(34,0,34,305,fill='grey50')
        c.create_line(68,0,68,305,fill='grey50')
        c.create_line(136,0,136,305,fill='grey50')
        
        c.create_line(170,0,170,305,fill='grey50')
        c.create_line(238,0,238,305,fill='grey50')
        c.create_line(272,0,272,305,fill='grey50')
        
        # horizontal
        c.create_line(0,34,305,34,fill='grey50')
        c.create_line(0,68,305,68,fill='grey50')
        c.create_line(0,136,305,136,fill='grey50')

        c.create_line(0,170,305,170,fill='grey50')
        c.create_line(0,238,305,238,fill='grey50')
        c.create_line(0,272,305,272,fill='grey50')

        c.create_line(102,0,102,305,fill='white',width=2.1)
        c.create_line(204,0,204,305,fill='white',width=2.1)
        c.create_line(0,102,305,102,fill='white',width=2.1)
        c.create_line(0,204,305,204,fill='white',width=2.1)
        
        # Example Puzzles
        global example_puzzles
        example_puzzles = [[[ '', '','3', '','2', '','6', '', ''], ['9', '', '','3', '','5', '', '','1'], [ '', '','1','8', '','6','4', '', ''], [ '', '','8','1', '','2','9', '', ''], ['7', '', '', '', '', '', '', '','8'], [ '', '','6','7', '','8','2', '', ''], [ '', '','2','6', '','9','5', '', ''], ['8', '', '','2', '','3', '', '','9'], [ '', '','5', '','1', '','3', '', '']],
                           [['2', '', '', '','8', '','3', '', ''], [ '','6', '', '','7', '', '','8','4'], [ '','3', '','5', '', '','2', '','9'], [ '', '', '','1', '','5','4', '','8'], [ '', '', '', '', '', '', '', '', ''], ['4', '','2','7', '','6', '', '', ''], ['3', '','1', '', '','7', '','4', ''], ['7','2', '', '','4', '', '','6', ''], [ '', '','4', '','1', '', '', '','3']], 
                           [[ '', '', '', '', '', '','9', '','7'], [ '', '', '','4','2', '','1','8', ''], [ '', '', '','7', '','5', '','2','6'], ['1', '', '','9', '','4', '', '', ''], [ '','5', '', '', '', '', '','4', ''], [ '', '', '','5', '','7', '', '','9'], ['9','2', '','1', '','8', '', '', ''], [ '','3','4', '','5','9', '', '', ''], ['5', '','7', '', '', '', '', '', '']], 
                           [[ '','3', '', '','5', '', '','4', ''], [ '', '','8', '','1', '','5', '', ''], ['4','6', '', '', '', '', '','1','2'], [ '','7', '','5', '','2', '','8', ''], [ '', '', '','6', '','3', '', '', ''], [ '','4', '','1', '','9', '','3', ''], ['2','5', '', '', '', '', '','9','8'], [ '', '','1', '','2', '','6', '', ''], [ '','8', '', '','6', '', '','2', '']],
                           [[ '','2', '','8','1', '','7','4', ''], ['7', '', '', '', '','3','1', '', ''], [ '','9', '', '', '','2','8', '','5'], [ '', '','9', '','4', '', '','8','7'], ['4', '', '','2', '','8', '', '','3'], ['1','6', '', '','3', '','2', '', ''], ['3', '','2','7', '', '', '','6', ''], [ '', '','5','6', '', '', '', '','8'], [ '','7','6', '','5','1', '','9', '']], 
                           [['1', '', '','9','2', '', '', '', ''], ['5','2','4', '','1', '', '', '', ''], [ '', '', '', '', '', '', '','7', ''], [ '','5', '', '', '','8','1', '','2'], [ '', '', '', '', '', '', '', '', ''], ['4', '','2','7', '', '', '','9', ''], [ '','6', '', '', '', '', '', '', ''], [ '', '', '', '','3', '','9','4','5'], [ '', '', '', '','7','1', '', '','6']],
                           [[ '','4','3', '','8', '','2','5', ''], ['6', '', '', '', '', '', '', '', ''], [ '', '', '', '', '','1', '','9','4'], ['9', '', '', '', '','4', '','7', ''], [ '', '', '','6', '','8', '', '', ''], [ '','1', '','2', '', '', '', '','3'], ['8','2', '','5', '', '', '', '', ''], [ '', '', '', '', '', '', '', '','5'], [ '','3','4', '','9', '','7','1', '']],
                           [['4','8', '', '', '','6','9', '','2'], [ '', '','2', '', '','8', '', '','1'], ['9', '', '','3','7', '', '','6', ''], ['8','4', '', '','1', '','2', '', ''], [ '', '','3','7', '','4','1', '', ''], [ '', '','1', '','6', '', '','4','9'], [ '','2', '', '','8','5', '', '','7'], ['7', '', '','9', '', '','6', '', ''], ['6', '','9','2', '', '', '','1','8']],
                           [[ '', '', '','9', '', '', '', '','2'], [ '','5', '','1','2','3','4', '', ''], [ '','3', '', '', '', '','1','6', ''], ['9', '','8', '', '', '', '', '', ''], [ '','7', '', '', '', '', '','9', ''], [ '', '', '', '', '', '','2', '','5'], [ '','9','1', '', '', '', '','5', ''], [ '', '','7','4','3','9', '','2', ''], ['4', '', '', '', '','7', '', '', '']],
                           [[ '', '','1','9', '', '', '', '','3'], ['9', '', '','7', '', '','1','6', ''], [ '','3', '', '', '','5', '', '','7'], [ '','5', '', '', '', '', '', '','9'], [ '', '','4','3', '','2','6', '', ''], ['2', '', '', '', '', '', '','7', ''], ['6', '', '','1', '', '', '','3', ''], [ '','4','2', '', '','7', '', '','6'], ['5', '', '', '', '','6','8', '', '']],
                           [[ '', '', '','1','2','5','4', '', ''], [ '', '','8','4', '', '', '', '', ''], ['4','2', '','8', '', '', '', '', ''], [ '','3', '', '', '', '', '','9','5'], [ '','6', '','9', '','2', '','1', ''], ['5','1', '', '', '', '', '','6', ''], [ '', '', '', '', '','3', '','4','9'], [ '', '', '', '', '','7','2', '', ''], [ '', '','1','2','9','8', '', '', '']],
                           [[ '','6','2','3','4', '','7','5', ''], ['1', '', '', '', '','5','6', '', ''], ['5','7', '', '', '', '', '','4', ''], [ '', '', '', '','9','4','8', '', ''], ['4', '', '', '', '', '', '', '','6'], [ '', '','5','8','3', '', '', '', ''], [ '','3', '', '', '', '', '','9','1'], [ '', '','6','4', '', '', '', '','7'], [ '','5','9', '','8','3','2','6', '']],
                           [['3', '', '', '', '', '', '', '', ''], [ '', '','5', '', '','9', '', '', ''], ['2', '', '','5', '','4', '', '', ''], [ '','2', '', '', '', '','7', '', ''], ['1','6', '', '', '', '', '','5','8'], ['7', '','4','3','1', '','6', '', ''], [ '', '', '','8','9', '','1', '', ''], [ '', '', '', '','6','7', '','8', ''], [ '', '', '', '', '','5','4','3','7']],
                           [['6','3', '', '', '', '', '', '', ''], [ '', '', '','5', '', '', '', '','8'], [ '', '','5','6','7','4', '', '', ''], [ '', '', '', '','2', '', '', '', ''], [ '', '','3','4', '','1', '','2', ''], [ '', '', '', '', '', '','3','4','5'], [ '', '', '', '', '','7', '', '','4'], [ '','8', '','3', '', '','9', '','2'], ['9','4','7','1', '', '', '','8', '']],
                           [[ '', '', '', '','2', '', '','4', ''], [ '', '','8', '','3','5', '', '', ''], [ '', '', '', '','7', '','6', '','2'], [ '','3','1', '','4','6','9','7', ''], ['2', '', '', '', '', '', '', '', ''], [ '', '', '','5', '','1','2', '','3'], [ '','4','9', '', '', '','7','3', ''], [ '', '', '', '', '', '', '','1', ''], ['8', '', '', '', '','4', '', '', '']],
                           [['3','6','1', '','2','5','9', '', ''], [ '','8', '','9','6', '', '','1', ''], ['4', '', '', '', '', '', '','5','7'], [ '', '','8', '', '', '','4','7','1'], [ '', '', '','6', '','3', '', '', ''], ['2','5','9', '', '', '','8', '', ''], ['7','4', '', '', '', '', '', '','5'], [ '','2', '', '','1','8', '','6', ''], [ '', '','5','4','7', '','3','2','9']],
                           [[ '','5', '','8', '','7', '','2', ''], ['6', '', '', '','1', '', '','9', ''], ['7', '','2','5','4', '', '', '','6'], [ '','7', '', '','2', '','3', '','1'], ['5', '','4', '', '', '','9', '','8'], ['1', '','3', '','8', '', '','7', ''], ['9', '', '', '','7','6','2', '','5'], [ '','6', '', '','9', '', '', '','3'], [ '','8', '','1', '','3', '','4', '']],
                           [[ '','8', '', '', '','5', '', '', ''], [ '', '', '', '', '','3','4','5','7'], [ '', '', '', '','7', '','8', '','9'], [ '','6', '','4', '', '','9', '','3'], [ '', '','7', '','1', '','5', '', ''], ['4', '','8', '', '','7', '','2', ''], ['9', '','1', '','2', '', '', '', ''], ['8','4','2','3', '', '', '', '', ''], [ '', '', '','1', '', '', '','8', '']],
                           [[ '', '','3','5', '','2','9', '', ''], [ '', '', '', '','4', '', '', '', ''], ['1', '','6', '', '', '','3', '','5'], ['9', '', '','2','5','1', '', '','8'], [ '','7', '','4', '','8', '','3', ''], ['8', '', '','7','6','3', '', '','1'], ['3', '','8', '', '', '','1', '','4'], [ '', '', '', '','2', '', '', '', ''], [ '', '','5','1', '','4','8', '', '']],
                           [[ '', '', '', '', '', '', '', '', ''], [ '', '','9','8', '','5','1', '', ''], [ '','5','1','9', '','7','4','2', ''], ['2','9', '','4', '','1', '','6','5'], [ '', '', '', '', '', '', '', '', ''], ['1','4', '','5', '','8', '','9','3'], [ '','2','6','7', '','9','5','8', ''], [ '', '','5','1', '','3','6', '', ''], [ '', '', '', '', '', '', '', '', '']],
                           [[ '','2', '', '','3', '', '','9', ''], [ '', '', '','9', '','7', '', '', ''], ['9', '', '','2', '','8', '', '','5'], [ '', '','4','8', '','6','5', '', ''], ['6', '','7', '', '', '','2', '','8'], [ '', '','3','1', '','2','9', '', ''], ['8', '', '','6', '','5', '', '','7'], [ '', '', '','3', '','9', '', '', ''], [ '','3', '', '','2', '', '','5', '']],
                           [[ '', '','5', '', '', '', '', '','6'], [ '','7', '', '', '','9', '','2', ''], [ '', '', '','5', '', '','1', '','7'], ['8', '','4','1','5', '', '', '', ''], [ '', '', '','8', '','3', '', '', ''], [ '', '', '', '','9','2','8', '','5'], ['9', '','7', '', '','6', '', '', ''], [ '','3', '','4', '', '', '','1', ''], ['2', '', '', '', '', '','6', '', '']],
                           [[ '','4', '', '', '', '', '','5', ''], [ '', '','1','9','4','3','6', '', ''], [ '', '','9', '', '', '','3', '', ''], ['6', '', '', '','5', '', '', '','2'], ['1', '','3', '', '', '','5', '','6'], ['8', '', '', '','2', '', '', '','7'], [ '', '','5', '', '', '','2', '', ''], [ '', '','2','4','3','6','7', '', ''], [ '','3', '', '', '', '', '','4', '']],
                           [[ '', '','4', '', '', '', '', '', ''], [ '', '', '', '','3', '', '', '','2'], ['3','9', '','7', '', '', '','8', ''], ['4', '', '', '', '','9', '', '','1'], ['2', '','9','8', '','1','3', '','7'], ['6', '', '','2', '', '', '', '','8'], [ '','1', '', '', '','8', '','5','3'], ['9', '', '', '','4', '', '', '', ''], [ '', '', '', '', '', '','8', '', '']],
                           [['3','6', '', '','2', '', '','8','9'], [ '', '', '','3','6','1', '', '', ''], [ '', '', '', '', '', '', '', '', ''], ['8', '','3', '', '', '','6', '','2'], ['4', '', '','6', '','3', '', '','7'], ['6', '','7', '', '', '','1', '','8'], [ '', '', '', '', '', '', '', '', ''], [ '', '', '','4','1','8', '', '', ''], ['9','7', '', '','3', '', '','1','4']],
                           [['5', '', '','4', '', '', '','6', ''], [ '', '','9', '', '', '','8', '', ''], ['6','4', '', '','2', '', '', '', ''], [ '', '', '', '', '','1', '', '','8'], ['2', '','8', '', '', '','5', '','1'], ['7', '', '','5', '', '', '', '', ''], [ '', '', '', '','9', '', '','8','4'], [ '', '','3', '', '', '','6', '', ''], [ '','6', '', '', '','3', '', '','2']],
                           [[ '', '','7','2','5','6','4', '', ''], ['4', '', '', '', '', '', '', '','5'], [ '','1', '', '','3', '', '','6', ''], [ '', '', '','5', '','8', '', '', ''], [ '', '','8', '','6', '','2', '', ''], [ '', '', '','1', '','7', '', '', ''], [ '','3', '', '','7', '', '','9', ''], ['2', '', '', '', '', '', '', '','4'], [ '', '','6','3','1','2','7', '', '']],
                           [[ '', '', '', '', '', '', '', '', ''], [ '','7','9', '','5', '','1','8', ''], ['8', '', '', '', '', '', '', '','7'], [ '', '','7','3', '','6','8', '', ''], ['4','5', '','7', '','8', '','9','6'], [ '', '','3','5', '','2','7', '', ''], ['7', '', '', '', '', '', '', '','5'], [ '','1','6', '','3', '','4','2', ''], [ '', '', '', '', '', '', '', '', '']],
                           [[ '','3', '', '', '', '', '','8', ''], [ '', '','9', '', '', '','5', '', ''], [ '', '','7','5', '','9','2', '', ''], ['7', '', '','1', '','5', '', '','8'], [ '','2', '', '','9', '', '','3', ''], ['9', '', '','4', '','2', '', '','1'], [ '', '','4','2', '','7','1', '', ''], [ '', '','2', '', '', '','8', '', ''], [ '','7', '', '', '', '', '','9', '']],
                           [['2', '', '','1','7', '','6', '','3'], [ '','5', '', '', '', '','1', '', ''], [ '', '', '', '', '','6', '','7','9'], [ '', '', '', '','4', '','7', '', ''], [ '', '', '','8', '','1', '', '', ''], [ '', '','9', '','5', '', '', '', ''], ['3','1', '','4', '', '', '', '', ''], [ '', '','5', '', '', '', '','6', ''], ['9', '','6', '','3','7', '', '','2']],
                           [[ '', '', '', '', '', '', '','8', ''], ['8', '', '','7', '','1', '','4', ''], [ '','4', '', '','2', '', '','3', ''], ['3','7','4', '', '', '','9', '', ''], [ '', '', '', '','3', '', '', '', ''], [ '', '','5', '', '', '','3','2','1'], [ '','1', '', '','6', '', '','5', ''], [ '','5', '','8', '','2', '', '','6'], [ '','8', '', '', '', '', '', '', '']],
                           [[ '', '', '', '', '', '', '','8','5'], [ '', '', '','2','1', '', '', '','9'], ['9','6', '', '','8', '','1', '', ''], ['5', '', '','8', '', '', '','1','6'], [ '', '', '', '', '', '', '', '', ''], ['8','9', '', '', '','6', '', '','7'], [ '', '','9', '','7', '', '','5','2'], ['3', '', '', '','5','4', '', '', ''], ['4','8', '', '', '', '', '', '', '']],
                           [['6', '','8', '','7', '','5', '','2'], [ '','5', '','6', '','8', '','7', ''], [ '', '','2', '', '', '','3', '', ''], ['5', '', '', '','9', '', '', '','6'], [ '','4', '','3', '','2', '','5', ''], ['8', '', '', '','5', '', '', '','3'], [ '', '','5', '', '', '','2', '', ''], [ '','1', '','7', '','4', '','9', ''], ['4', '','9', '','6', '','7', '','1']],
                           [[ '','5', '', '','1', '', '','4', ''], ['1', '','7', '', '', '','6', '','2'], [ '', '', '','9', '','5', '', '', ''], ['2', '','8', '','3', '','5', '','1'], [ '','4', '', '','7', '', '','2', ''], ['9', '','1', '','8', '','4', '','6'], [ '', '', '','4', '','1', '', '', ''], ['3', '','4', '', '', '','7', '','9'], [ '','2', '', '','6', '', '','1', '']],
                           [[ '','5','3', '', '', '','7','9', ''], [ '', '','9','7','5','3','4', '', ''], ['1', '', '', '', '', '', '', '','2'], [ '','9', '', '','8', '', '','1', ''], [ '', '', '','9', '','7', '', '', ''], [ '','8', '', '','3', '', '','7', ''], ['5', '', '', '', '', '', '', '','3'], [ '', '','7','6','4','1','2', '', ''], [ '','6','1', '', '', '','9','4', '']],
                           [[ '', '','6', '','8', '','3', '', ''], [ '','4','9', '','7', '','2','5', ''], [ '', '', '','4', '','5', '', '', ''], ['6', '', '','3','1','7', '', '','4'], [ '', '','7', '', '', '','8', '', ''], ['1', '', '','8','2','6', '', '','9'], [ '', '', '','7', '','2', '', '', ''], [ '','7','5', '','4', '','1','9', ''], [ '', '','3', '','9', '','6', '', '']],
                           [[ '', '','5', '','8', '','7', '', ''], ['7', '', '','2', '','4', '', '','5'], ['3','2', '', '', '', '', '','8','4'], [ '','6', '','1', '','5', '','4', ''], [ '', '','8', '', '', '','5', '', ''], [ '','7', '','8', '','3', '','1', ''], ['4','5', '', '', '', '', '','9','1'], ['6', '', '','5', '','8', '', '','7'], [ '', '','3', '','1', '','6', '', '']],
                           [[ '', '', '','9', '', '','8', '', ''], ['1','2','8', '', '','6','4', '', ''], [ '','7', '','8', '', '', '','6', ''], ['8', '', '','4','3', '', '', '','7'], ['5', '', '', '', '', '', '', '','9'], ['6', '', '', '','7','9', '', '','8'], [ '','9', '', '', '','4', '','1', ''], [ '', '','3','6', '', '','2','8','4'], [ '', '','1', '', '','7', '', '', '']],
                           [[ '', '', '', '','8', '', '', '', ''], ['2','7', '', '', '', '', '','5','4'], [ '','9','5', '', '', '','8','1', ''], [ '', '','9','8', '','6','4', '', ''], [ '','2', '','4', '','3', '','6', ''], [ '', '','6','9', '','5','1', '', ''], [ '','1','7', '', '', '','6','2', ''], ['4','6', '', '', '', '', '','3','8'], [ '', '', '', '','9', '', '', '', '']],
                           [[ '', '', '','6', '','2', '', '', ''], ['4', '', '', '','5', '', '', '','1'], [ '','8','5', '','1', '','6','2', ''], [ '','3','8','2', '','6','7','1', ''], [ '', '', '', '', '', '', '', '', ''], [ '','1','9','4', '','7','3','5', ''], [ '','2','6', '','4', '','5','3', ''], ['9', '', '', '','2', '', '', '','7'], [ '', '', '','8', '','9', '', '', '']],
                           [[ '', '', '','9', '', '', '', '','2'], [ '','5', '','1','2','3','4', '', ''], [ '','3', '', '', '', '','1','6', ''], ['9', '','8', '', '', '', '', '', ''], [ '','7', '', '', '', '', '','9', ''], [ '', '', '', '', '', '','2', '','5'], [ '','9','1', '', '', '', '','5', ''], [ '', '','7','4','3','9', '','2', ''], ['4', '', '', '', '','7', '', '', '']],
                           [['3','8', '', '', '', '', '', '', ''], [ '', '', '','4', '', '','7','8','5'], [ '', '','9', '','2', '','3', '', ''], [ '','6', '', '','9', '', '', '', ''], ['8', '', '','3', '','2', '', '','9'], [ '', '', '', '','4', '', '','7', ''], [ '', '','1', '','7', '','5', '', ''], ['4','9','5', '', '','6', '', '', ''], [ '', '', '', '', '', '', '','9','2']],
                           [[ '', '', '','1','5','8', '', '', ''], [ '', '','2', '','6', '','8', '', ''], [ '','3', '', '', '', '', '','4', ''], [ '','2','7', '','3', '','5','1', ''], [ '', '', '', '', '', '', '', '', ''], [ '','4','6', '','8', '','7','9', ''], [ '','5', '', '', '', '', '','8', ''], [ '', '','4', '','7', '','1', '', ''], [ '', '', '','3','2','5', '', '', '']],
                           [[ '','1', '','5', '', '','2', '', ''], ['9', '', '', '', '','1', '', '', ''], [ '', '','2', '', '','8', '','3', ''], ['5', '', '', '','3', '', '', '','7'], [ '', '','8', '', '', '','5', '', ''], ['6', '', '', '','8', '', '', '','4'], [ '','4', '','1', '', '','7', '', ''], [ '', '', '','7', '', '', '', '','6'], [ '', '','3', '', '','4', '','5', '']],
                           [[ '','8', '', '', '', '', '','4', ''], [ '', '', '','4','6','9', '', '', ''], ['4', '', '', '', '', '', '', '','7'], [ '', '','5','9', '','4','6', '', ''], [ '','7', '','6', '','8', '','3', ''], [ '', '','8','5', '','2','1', '', ''], ['9', '', '', '', '', '', '', '','5'], [ '', '', '','7','8','1', '', '', ''], [ '','6', '', '', '', '', '','1', '']],
                           [['9', '','4','2', '', '', '', '','7'], [ '','1', '', '', '', '', '', '', ''], [ '', '', '','7', '','6','5', '', ''], [ '', '', '','8', '', '', '','9', ''], [ '','2', '','9', '','4', '','6', ''], [ '','4', '', '', '','2', '', '', ''], [ '', '','1','6', '','7', '', '', ''], [ '', '', '', '', '', '', '','3', ''], ['3', '', '', '', '','5','7', '','2']],
                           [[ '', '', '','7', '', '','8', '', ''], [ '', '','6', '', '', '', '','3','1'], [ '','4', '', '', '','2', '', '', ''], [ '','2','4', '','7', '', '', '', ''], [ '','1', '', '','3', '', '','8', ''], [ '', '', '', '','6', '','2','9', ''], [ '', '', '','8', '', '', '','7', ''], ['8','6', '', '', '', '','5', '', ''], [ '', '','2', '', '','6', '', '', '']],
                           [[ '', '','1', '', '','7', '','9', ''], ['5','9', '', '','8', '', '', '','1'], [ '','3', '', '', '', '', '','8', ''], [ '', '', '', '', '','5','8', '', ''], [ '','5', '', '','6', '', '','2', ''], [ '', '','4','1', '', '', '', '', ''], [ '','8', '', '', '', '', '','3', ''], ['1', '', '', '','2', '', '','7','9'], [ '','2', '','7', '', '','4', '', '']],
                           [[ '', '', '', '', '','3', '','1','7'], [ '','1','5', '', '','9', '', '','8'], [ '','6', '', '', '', '', '', '', ''], ['1', '', '', '', '','7', '', '', ''], [ '', '','9', '', '', '','2', '', ''], [ '', '', '','5', '', '', '', '','4'], [ '', '', '', '', '', '', '','2', ''], ['5', '', '','6', '', '','3','4', ''], ['3','4', '','2', '', '', '', '', '']],
                           [['3', '', '','2', '', '', '', '', ''], [ '', '', '','1', '','7', '', '', ''], ['7', '','6', '','3', '','5', '', ''], [ '','7', '', '', '','9', '','8', ''], ['9', '', '', '','2', '', '', '','4'], [ '','1', '','8', '', '', '','5', ''], [ '', '','9', '','4', '','3', '','1'], [ '', '', '','7', '','2', '', '', ''], [ '', '', '', '', '','8', '', '','6']]]
                           
                           
        
        global empty_puzzle
        empty_puzzle = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        
        global a1, a2, a3, a4, a5, a6, a7, a8, a9, b1, b2, b3, b4, b5, b6, b7, b8, b9, c1, c2, c3, c4, c5, c6, c7, c8, c9, d1, d2, d3, d4, d5, d6, d7, d8, d9, e1, e2, e3, e4, e5, e6, e7, e8, e9, f1, f2, f3, f4, f5, f6, f7, f8, f9, g1, g2, g3, g4, g5, g6, g7, g8, g9, h1, h2, h3, h4, h5, h6, h7, h8, h9, i1, i2, i3, i4, i5, i6, i7, i8, i9 
        global A1, A2, A3, A4, A5, A6, A7, A8, A9, B1, B2, B3, B4, B5, B6, B7, B8, B9, C1, C2, C3, C4, C5, C6, C7, C8, C9, D1, D2, D3, D4, D5, D6, D7, D8, D9, E1, E2, E3, E4, E5, E6, E7, E8, E9, F1, F2, F3, F4, F5, F6, F7, F8, F9, G1, G2, G3, G4, G5, G6, G7, G8, G9, H1, H2, H3, H4, H5, H6, H7, H8, H9, I1, I2, I3, I4, I5, I6, I7, I8, I9
        
        a1 = StringVar()
        a2 = StringVar()
        a3 = StringVar()
        a4 = StringVar()
        a5 = StringVar()
        a6 = StringVar()
        a7 = StringVar()
        a8 = StringVar()
        a9 = StringVar()


        b1 = StringVar()
        b2 = StringVar()
        b3 = StringVar()
        b4 = StringVar()
        b5 = StringVar()
        b6 = StringVar()
        b7 = StringVar()
        b8 = StringVar()
        b9 = StringVar()


        c1 = StringVar()
        c2 = StringVar()
        c3 = StringVar()
        c4 = StringVar()
        c5 = StringVar()
        c6 = StringVar()
        c7 = StringVar()
        c8 = StringVar()
        c9 = StringVar()


        d1 = StringVar()
        d2 = StringVar()
        d3 = StringVar()
        d4 = StringVar()
        d5 = StringVar()
        d6 = StringVar()
        d7 = StringVar()
        d8 = StringVar()
        d9 = StringVar()


        e1 = StringVar()
        e2 = StringVar()
        e3 = StringVar()
        e4 = StringVar()
        e5 = StringVar()
        e6 = StringVar()
        e7 = StringVar()
        e8 = StringVar()
        e9 = StringVar()


        f1 = StringVar()
        f2 = StringVar()
        f3 = StringVar()
        f4 = StringVar()
        f5 = StringVar()
        f6 = StringVar()
        f7 = StringVar()
        f8 = StringVar()
        f9 = StringVar()


        g1 = StringVar()
        g2 = StringVar()
        g3 = StringVar()
        g4 = StringVar()
        g5 = StringVar()
        g6 = StringVar()
        g7 = StringVar()
        g8 = StringVar()
        g9 = StringVar()


        h1 = StringVar()
        h2 = StringVar()
        h3 = StringVar()
        h4 = StringVar()
        h5 = StringVar()
        h6 = StringVar()
        h7 = StringVar()
        h8 = StringVar()
        h9 = StringVar()


        i1 = StringVar()
        i2 = StringVar()
        i3 = StringVar()
        i4 = StringVar()
        i5 = StringVar()
        i6 = StringVar()
        i7 = StringVar()
        i8 = StringVar()
        i9 = StringVar()

        A1 = Entry(master, width=1,textvariable=a1,highlightbackground='black')
        A2 = Entry(master, width=1,textvariable=a2,highlightbackground='black')
        A3 = Entry(master, width=1,textvariable=a3,highlightbackground='black')
        A4 = Entry(master, width=1,textvariable=a4,highlightbackground='black')
        A5 = Entry(master, width=1,textvariable=a5,highlightbackground='black')
        A6 = Entry(master, width=1,textvariable=a6,highlightbackground='black')
        A7 = Entry(master, width=1,textvariable=a7,highlightbackground='black')
        A8 = Entry(master, width=1,textvariable=a8,highlightbackground='black')
        A9 = Entry(master, width=1,textvariable=a9,highlightbackground='black')
        
        B1 = Entry(master, width=1,textvariable=b1,highlightbackground='black')
        B2 = Entry(master, width=1,textvariable=b2,highlightbackground='black')
        B3 = Entry(master, width=1,textvariable=b3,highlightbackground='black')
        B4 = Entry(master, width=1,textvariable=b4,highlightbackground='black')
        B5 = Entry(master, width=1,textvariable=b5,highlightbackground='black')
        B6 = Entry(master, width=1,textvariable=b6,highlightbackground='black')
        B7 = Entry(master, width=1,textvariable=b7,highlightbackground='black')
        B8 = Entry(master, width=1,textvariable=b8,highlightbackground='black')
        B9 = Entry(master, width=1,textvariable=b9,highlightbackground='black')
        
        C1 = Entry(master, width=1,textvariable=c1,highlightbackground='black')
        C2 = Entry(master, width=1,textvariable=c2,highlightbackground='black')
        C3 = Entry(master, width=1,textvariable=c3,highlightbackground='black')
        C4 = Entry(master, width=1,textvariable=c4,highlightbackground='black')
        C5 = Entry(master, width=1,textvariable=c5,highlightbackground='black')
        C6 = Entry(master, width=1,textvariable=c6,highlightbackground='black')
        C7 = Entry(master, width=1,textvariable=c7,highlightbackground='black')
        C8 = Entry(master, width=1,textvariable=c8,highlightbackground='black')
        C9 = Entry(master, width=1,textvariable=c9,highlightbackground='black')
    
        D1 = Entry(master, width=1,textvariable=d1,highlightbackground='black')
        D2 = Entry(master, width=1,textvariable=d2,highlightbackground='black')
        D3 = Entry(master, width=1,textvariable=d3,highlightbackground='black')
        D4 = Entry(master, width=1,textvariable=d4,highlightbackground='black')
        D5 = Entry(master, width=1,textvariable=d5,highlightbackground='black')
        D6 = Entry(master, width=1,textvariable=d6,highlightbackground='black')
        D7 = Entry(master, width=1,textvariable=d7,highlightbackground='black')
        D8 = Entry(master, width=1,textvariable=d8,highlightbackground='black')
        D9 = Entry(master, width=1,textvariable=d9,highlightbackground='black')
        
        E1 = Entry(master, width=1,textvariable=e1,highlightbackground='black')
        E2 = Entry(master, width=1,textvariable=e2,highlightbackground='black')
        E3 = Entry(master, width=1,textvariable=e3,highlightbackground='black')
        E4 = Entry(master, width=1,textvariable=e4,highlightbackground='black')
        E5 = Entry(master, width=1,textvariable=e5,highlightbackground='black')
        E6 = Entry(master, width=1,textvariable=e6,highlightbackground='black')
        E7 = Entry(master, width=1,textvariable=e7,highlightbackground='black')
        E8 = Entry(master, width=1,textvariable=e8,highlightbackground='black')
        E9 = Entry(master, width=1,textvariable=e9,highlightbackground='black')
        
        F1 = Entry(master, width=1,textvariable=f1,highlightbackground='black')
        F2 = Entry(master, width=1,textvariable=f2,highlightbackground='black')
        F3 = Entry(master, width=1,textvariable=f3,highlightbackground='black')
        F4 = Entry(master, width=1,textvariable=f4,highlightbackground='black')
        F5 = Entry(master, width=1,textvariable=f5,highlightbackground='black')
        F6 = Entry(master, width=1,textvariable=f6,highlightbackground='black')
        F7 = Entry(master, width=1,textvariable=f7,highlightbackground='black')
        F8 = Entry(master, width=1,textvariable=f8,highlightbackground='black')
        F9 = Entry(master, width=1,textvariable=f9,highlightbackground='black')
        
        G1 = Entry(master, width=1,textvariable=g1,highlightbackground='black')
        G2 = Entry(master, width=1,textvariable=g2,highlightbackground='black')
        G3 = Entry(master, width=1,textvariable=g3,highlightbackground='black')
        G4 = Entry(master, width=1,textvariable=g4,highlightbackground='black')
        G5 = Entry(master, width=1,textvariable=g5,highlightbackground='black')
        G6 = Entry(master, width=1,textvariable=g6,highlightbackground='black')
        G7 = Entry(master, width=1,textvariable=g7,highlightbackground='black')
        G8 = Entry(master, width=1,textvariable=g8,highlightbackground='black')
        G9 = Entry(master, width=1,textvariable=g9,highlightbackground='black')

        H1 = Entry(master, width=1,textvariable=h1,highlightbackground='black')
        H2 = Entry(master, width=1,textvariable=h2,highlightbackground='black')
        H3 = Entry(master, width=1,textvariable=h3,highlightbackground='black')
        H4 = Entry(master, width=1,textvariable=h4,highlightbackground='black')
        H5 = Entry(master, width=1,textvariable=h5,highlightbackground='black')
        H6 = Entry(master, width=1,textvariable=h6,highlightbackground='black')
        H7 = Entry(master, width=1,textvariable=h7,highlightbackground='black')
        H8 = Entry(master, width=1,textvariable=h8,highlightbackground='black')
        H9 = Entry(master, width=1,textvariable=h9,highlightbackground='black')
    
        I1 = Entry(master, width=1,textvariable=i1,highlightbackground='black')
        I2 = Entry(master, width=1,textvariable=i2,highlightbackground='black')
        I3 = Entry(master, width=1,textvariable=i3,highlightbackground='black')
        I4 = Entry(master, width=1,textvariable=i4,highlightbackground='black')
        I5 = Entry(master, width=1,textvariable=i5,highlightbackground='black')
        I6 = Entry(master, width=1,textvariable=i6,highlightbackground='black')
        I7 = Entry(master, width=1,textvariable=i7,highlightbackground='black')
        I8 = Entry(master, width=1,textvariable=i8,highlightbackground='black')
        I9 = Entry(master, width=1,textvariable=i9,highlightbackground='black')
        
        global Entry_Fields, Entry_Variables         
        Entry_Fields = [[A1,A2,A3,A4,A5,A6,A7,A8,A9],[B1,B2,B3,B4,B5,B6,B7,B8,B9],[C1,C2,C3,C4,C5,C6,C7,C8,C9],[D1,D2,D3,D4,D5,D6,D7,D8,D9],[E1,E2,E3,E4,E5,E6,E7,E8,E9],[F1,F2,F3,F4,F5,F6,F7,F8,F9],[G1,G2,G3,G4,G5,G6,G7,G8,G9],[H1,H2,H3,H4,H5,H6,H7,H8,H9],[I1,I2,I3,I4,I5,I6,I7,I8,I9]]
        Entry_Variables = [[a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9],[c1,c2,c3,c4,c5,c6,c7,c8,c9],[d1,d2,d3,d4,d5,d6,d7,d8,d9],[e1,e2,e3,e4,e5,e6,e7,e8,e9],[f1,f2,f3,f4,f5,f6,f7,f8,f9],[g1,g2,g3,g4,g5,g6,g7,g8,g9],[h1,h2,h3,h4,h5,h6,h7,h8,h9],[i1,i2,i3,i4,i5,i6,i7,i8,i9]]
        
        ################################################################################
        
        # Places entry fields on grid
        for j,i in enumerate(Entry_Fields):
            for k,l in enumerate(i):
                l.grid(row = j + 1,column = k + 4)

        #######################################################################

        def Solve(CLEAR=FALSE,CHECK=FALSE,SMILE=FALSE,EXAMPLE=FALSE):
            global t    
            t = 0.0
            # Transforms
            def transpose(n):
                # Takes a square list-'Matrix' and gives back the transpose
                d = [[n[j][i] for j in range(len(n))] for i in range(len(n))]
                return d

            def box(n):
                d = [[] for i in range(len(n))]
                m = 0
                for Q in range(len(n)):
                    if 18 <= m < 27:
                        if 24 <= m < 27:
                            for i in range(6,9):
                                m = m + 1
                                for c in range(6,9):
                                    d[Q].append(n[i][c])
                        elif 21 <= m < 24:
                            for i in range(3,6):
                                m = m + 1
                                for c in range(6,9):
                                    d[Q].append(n[i][c])
                        elif 18 <= m < 21:
                            for i in range(3):
                                m = m + 1 
                                for c in range(6,9):
                                    d[Q].append(n[i][c])
                    elif 9 <= m < 18:
                        if 15 <= m < 18:
                            for i in range(6,9):
                                m = m + 1
                                for c in range(3,6):
                                    d[Q].append(n[i][c])        
                        elif 12 <= m < 15:
                            for i in range(3,6):
                                m = m + 1
                                for c in range(3,6):
                                    d[Q].append(n[i][c])
                        elif 9 <= m < 12:
                            for i in range(3):
                                m = m + 1
                                for c in range(3,6):
                                    d[Q].append(n[i][c])
                    elif m < 9:
                        if 6 <= m < 9:
                            for i in range(6,9):
                                m = m + 1
                                for c in range(3):
                                    d[Q].append(n[i][c])
                        elif 3 <= m < 6:
                            for i in range(3,6):
                                m = m + 1
                                for c in range(3):
                                    d[Q].append(n[i][c])
                        elif m < 3:
                            for i in range(3):
                                m = m + 1
                                for c in range(3):
                                    d[Q].append(n[i][c])
                                
                return d
            
            def check():
                # checks if it is a valid puzzle 
                # not neccessaarily a single solution sudoku or a viable sudoku i.e. 
                # has a solution. just that the user input does not break any rules
                x = []
                for c in Entry_Fields:
                    d = []
                    for i in c:
                        if i.get() == '':
                            d.append(0)
                            i.config(foreground='red2')
                        else:
                            d.append(int(i.get()[-1]))
                    x.append(d)
                
                def ERR_CK(n):
                    for k,i in enumerate(n):
                        for j in i:
                            if i.count(j) > 1 and j != 0:
                                return False, k, j
                    return True, '', ''
                def box_index(x):
                    if x == 0:
                        return ' top left box.'
                    elif x == 1:
                        return ' center left box.'
                    elif x == 2:
                        return ' bottom left box.'
                    elif x == 3:
                        return ' top center box.'
                    elif x == 4:
                        return ' middle box.'
                    elif x == 5:
                        return ' bottom center box.'
                    elif x == 6:
                        return ' top right box.'
                    elif x == 7:
                        return ' center right box.' 
                    elif x == 8:
                        return ' bottom right box.'
                        
                def complete_check(n):
                    u, c, y =  ERR_CK(n)
                    if u:
                        pass
                    else:
                        return u,c+1,x,' row ',y
                    u, c, y =  ERR_CK(transpose(n))
                    if u:
                        pass
                    else:
                        return u,c+1,x, ' column ', y
                    u, c, y =  ERR_CK(box(n))
                    if u:
                        pass
                    else:
                        return u,box_index(c),x, ' the ',y
                    return True, '', x,'',''
                return complete_check(x)
                
            if SMILE:
                for i in Entry_Variables:
                    for p in i:
                        p.set('')
                for i in Entry_Fields:
                    for p in i:
                        p.config(background='yellow')
                        
                A1.config(background='white')
                A2.config(background='white')
                B1.config(background='white')
                A8.config(background='white')
                A9.config(background='white')
                B9.config(background='white')
                H1.config(background='white')
                I1.config(background='white')
                I2.config(background='white')
                H9.config(background='white')
                I8.config(background='white')
                I9.config(background='white')
                
                C4.config(background='black')
                C6.config(background='black')
                D4.config(background='black')
                D6.config(background='black')
                C3.config(background='black')
                D3.config(background='black')
                C7.config(background='black')
                D7.config(background='black')
                G3.config(background='black')
                G7.config(background='black')
                H4.config(background='black')
                H5.config(background='black')
                H6.config(background='black')
            
            elif EXAMPLE:
                random_index = randint(0,len(example_puzzles)-1)
                random_puzzle = example_puzzles[random_index]
                for j,i in enumerate(Entry_Variables):
                    for k,p in enumerate(i):
                        p.set(random_puzzle[j][k])
                for i in Entry_Fields:
                    for p in i:
                        p.config(background='white')
                        p.config(foreground='black')
            else:
                try:
                    if not CLEAR:
                        q,c,x,typ,y = check()
                        for i in Entry_Fields:
                            for p in i:
                                p.config(background='white')
                    
                    
                    if CLEAR:
                        for i in Entry_Variables:
                            for c in i:
                                c.set('')
                        for i in Entry_Fields:
                            for p in i:
                                p.config(background='white')
                                p.config(foreground='black')
                    
                    elif CHECK:
                        q,c,x,typ,y = check()
                        if not q:
                            error_message = 'There seems to be a repeated number ' + str(y) + ' in' + typ + str(c)
                            for i in Entry_Fields:
                                for p in i:
                                    p.config(background='white')
                                    p.config(foreground='black')
                        elif x == empty_puzzle:
                            error_message = "You haven't entered anything in yet!"
                            for i in Entry_Fields:
                                for p in i:
                                    p.config(background='white')
                                    p.config(foreground='black')
                        else:
                            error_message = "Everything looks OK!"
                            for i in Entry_Fields:
                                for p in i:
                                    p.config(background='white')
                                    p.config(foreground='black')
                        err = Toplevel(master,background='black')
                        err.title("Check")
                        err.wm_grid()
                        
                        err.resizable(FALSE,FALSE)
                        
                        msg = Message(err,text=error_message,foreground='white',background='black',justify='center')
                        msg.pack()

                            
                        exit_button = Button(err,text='OK',command=err.destroy,highlightbackground='black')
                        exit_button.pack()
                    
                    elif not q:
                        q,c,x,typ,y = check()
                        for i in Entry_Fields:
                            for p in i:
                                p.config(background='white')
                                p.config(foreground='black')
                        err = Toplevel(master,background='black')
                        err.title("Error")
                        
                        err.resizable(FALSE,FALSE)
                        
                        msg = Message(err,text='There seems to be a repeated number ' + str(y) + ' in' + typ + str(c),foreground='white',background='black',justify='center')
                        msg.pack()

                        
                        exit_button = Button(err,text='OK',command=err.destroy,highlightbackground='black')
                        exit_button.pack()

                    
                    else:
                        if x == empty_puzzle:
                            for i in Entry_Fields:
                                for p in i:
                                    p.config(foreground='RoyalBlue1')
                            a4.set('Y')
                            a5.set('O')
                            a6.set('U')
                            b2.set('D')
                            b3.set('I')
                            b4.set('D')
                            b6.set('N')
                            b7.set('O')
                            b8.set('T')
                            d3.set('E')
                            d4.set('N')
                            d5.set('T')
                            d6.set('E')
                            d7.set('R')
                            e5.set('A')
                            f3.set('P')
                            f4.set('U')
                            f5.set('Z')
                            f6.set('Z')
                            f7.set('L')
                            f8.set('E')
                            h4.set('Y')
                            h5.set('E')
                            h6.set('T')
                            h7.set('!')
                            
                        else:
                            def ld(x, y):
                                pos = [i for i in x if i not in y]
                                return pos
                                
                            def solved(n):
                                # Checks if each position has been made into an integer
                                d = 0
                                for i in n:
                                    for c in i:
                                        if not type(c) == int:
                                            d = d + 1
                                if d == 0:
                                    return True
                                else:
                                    return False
                                
                            def linecheck(n):
                                for k,i in enumerate(n):
                                    for j,c in enumerate(i):
                                        if type(c) == list:
                                            n[k][j] = ld(c,i)
                                return n

                            def single(puzzle):
                                # Goes line by line finding variables then tests each possibility in a
                                # list of variables then takes each possibility and checks to see
                                # if that is the only variable spot in which that possibility appears.
                                for line_index, line in enumerate(puzzle):
                                    for variable_index, variable1 in enumerate(line):
                                        if type(variable1) == list:
                                            for possibility in variable1:
                                                count = 0
                                                for variable2 in line:
                                                    if type(variable2) == list:
                                                        if possibility in variable2:
                                                            count = count + 1
                                                            if count > 1: break
                                                if count == 1:
                                                    puzzle[line_index][variable_index] = possibility
                                                    break
                                return puzzle

                            def confirm(n):
                                # replaces the variables that have been knocked down to one possibility
                                for k,i in enumerate(n):
                                    for j,c in enumerate(i):
                                        if type(c) == list:
                                            if len(c) == 1:
                                                n[k][j] = int(c[0])
                                return n

                            def step(n):
                                # checks lines, eliminating variables and singularities
                                n = linecheck(n)
                                n = single(n)
                                n = confirm(n)
                                return n
                                
                            def rc(n):
                                # checks columns, then rows
                                for w in range(2):
                                    n = transpose(n)
                                    n = step(n)
                                return n
                                
                            def boxxy(n):
                                # checks boxes
                                n = box(n)
                                n = step(n)
                                n = box(box(n))
                                return n
                                
                            def solve(n):
                                # Eliminates variables from rows and columns
                                # that are not possible candidates for the position.
                                n = rc(n)
                                n = boxxy(n)
                                n = confirm(n)
                                return n
                                
                            def var(n,t=0):
                                # Gives coordinates for spot with the
                                # least number of variables.
                                vc = []
                                v = []
                                for x1,line in enumerate(n):
                                    for x2,nums in enumerate(line):
                                        if type(nums) == list:
                                            vc.append([len(nums),[x1,x2]])
                                            if len(nums) == 2:
                                                return [len(nums),[x1,x2]] 
                                vc.sort()
                                m = vc[t]
                                return m
                                    
                            def bruteforce1(n,xfs):
                                # finds the variable with the lowest number of possiblities
                                # cycles through the variables until the correct one has been found.
                                m = var(n)
                                for i in range(m[0]):
                                    n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
                                    u = False
                                    while not solved(n):
                                        n1 = n
                                        n = solve(n)
                                        if bfcondition(n):
                                            n = xfs[-1]
                                            m = var(n)
                                            break
                                        if n == n1:
                                            n2 = failsafe(n)
                                            xfs.append(n2)
                                            n, u = bruteforce2(n,xfs)
                                            if solved(n):
                                                break
                                            m = var(n)
                                    if solved(n):
                                        break
                                while not solved(n):
                                    if not bfcondition(n) or solved(n):
                                        break
                                    n1 = n
                                    n = solve(n)
                                    if n == n1:
                                        n2 = failsafe(n)
                                        xfs.append(n2)
                                        n = bruteforce1(n,xfs)
                                return n
                                
                            def bruteforce2(n,xfs):
                                # finds the variable with the lowest number of possiblities
                                # cycles through the variables until the correct one has been found.
                                m = var(n)
                                for i in range(m[0]):
                                    n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
                                    u = False
                                    while not solved(n):
                                        n1 = n
                                        n = solve(n)
                                        if bfcondition(n):
                                            n = xfs[-1]
                                            m = var(n)
                                            break
                                        if n == n1:
                                            n2 = failsafe(n)
                                            xfs.append(n2)
                                            n, u = bruteforce2(n,xfs)
                                            if solved(n):
                                                break
                                        if bfcondition(n):
                                            n = xfs[-1]
                                            m = var(n)
                                            break
                                        if u:
                                            break
                                    if solved(n):
                                        break

                                if solved(n):
                                    return n, True
                                elif not bfcondition(n):
                                    f = xfs[-1]
                                    xfs.pop()
                                    return f, False
                                else:
                                    return n, True
                                    
                            def bfcondition(n):
                                for i in n:
                                    for c in i:
                                        if c == []:
                                            return True
                                for i in n:
                                    for c in i:
                                        if type(c) == int:
                                            if i.count(c) > 1:
                                                return True
                                for i in box(n):
                                    for c in i:
                                        if type(c) == int:
                                            if i.count(c) > 1:
                                                return True
                                for i in transpose(n):
                                    for c in i:
                                        if type(c) == int:
                                            if i.count(c) > 1:
                                                return True
                                return False

                            def failsafe(n):
                                n1 = []
                                for i in n:
                                    d = []
                                    for c in i:
                                        if type(c) == list:
                                            f = []
                                            for h in c:
                                                f.append(h)
                                        else:
                                            f = c
                                        d.append(f)
                                    n1.append(d)
                                return n1

                            ### RUNNING  ###
                            xc = [i for i in range(1,10)]
                            xgrid = []
                            for i in range(9):
                                dc = []
                                for i in range(9):
                                    dc.append(xc)
                                xgrid.append(dc)
                            for i in range(9):
                                for p,c in enumerate(x[i]):
                                    if c != 0:
                                        xgrid[i][p] = c
                                        
                            global start, end
                            start = time.clock()
                            
                            while not solved(xgrid):
                                xgrid1 = xgrid
                                xgrid = solve(xgrid)
                                if xgrid == xgrid1:
                                    xgrid2 = failsafe(xgrid)
                                    xfs = [xgrid2]
                                    xgrid = bruteforce1(xgrid,xfs)
                            end = time.clock()
                            t = end-start
                            for j,i in enumerate(Entry_Variables):
                                for k,p in enumerate(i):
                                    p.set(str(xgrid[j][k]))
                except ValueError:
                    err = Toplevel(master,background='black')
                    err.title("Error")
                    
                    err.resizable(FALSE,FALSE)
                    
                    msg = Message(err,text='Theres a non-digit in your puzzle.',foreground='white',background='black',justify='center')
                    msg.pack()
                        
                    exit_button = Button(err,text='OK',command=err.destroy,highlightbackground='black')
                    exit_button.pack()
            if t == 0.0:
                time_text = '               \n               \n               \n               \n               \n'
            else:
                time_text = 'Your puzzle took ' + str(t) + ' secs to solve.'                    
            
            timer = Message(master,text=time_text,background='black',foreground='white',width=70)
            timer.grid(column=0,row=3,rowspan=5,columnspan=2)
            
        chk = Button(master, text="Check",command = lambda: Solve(CHECK=TRUE),highlightbackground='black',activeforeground='blue',width='5')
        chk.grid(column=16,row=1,rowspan=3)
        slv = Button(master, text="Solve",command = lambda: Solve(),highlightbackground='black',activeforeground='blue')
        slv.grid(column=16,row=2,rowspan=3)
        sml = Button(master, text="Smile",command = lambda: Solve(SMILE=TRUE),highlightbackground='black',activeforeground='blue',)
        sml.grid(column=16,row=3,rowspan=3)
        clr = Button(master, text = "Clear",command = lambda: Solve(CLEAR=TRUE), highlightbackground='black',activeforeground='blue')
        clr.grid(column=16,row=4,rowspan=3)
        ex = Button(master, text = "Example",command = lambda: Solve(EXAMPLE=TRUE), highlightbackground='black',activeforeground='blue')
        ex.grid(column=16,row=5,rowspan=3)
        qt = Button(master, text = "Quit",command = lambda: frame.quit(), highlightbackground = 'black',activeforeground='red')
        qt.grid(column=16,row=9,rowspan=3) 
        



        
root = Tk()

root.resizable(FALSE,FALSE)
root.title("Sudoku Solver V.6.1")

app = GUI(root)

root.mainloop()

