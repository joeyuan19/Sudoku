#!/bin/sh

# sudoku3.py
# SudokuSolver
#
# Created by joe yuan on 3/6/11.
# Copyright 2011 __MyCompanyName__. All rights reserved.

import time
import sys

def rowbyrow():
    d = []
    for i in range(9):
        x = INPUT_PROCESS(i)
        d.append(x)
    for k,i in enumerate(d):
        for j,c in enumerate(i):
                d[k][j] = int(c)
    return d

def INPUT_PROCESS(i,u=False):
    while not u:
        x = INPUT(i)
        x, u = input_check(x,i)
    return x

def INPUT(i):
    x = list(raw_input("Row " + str(i+1) + ":\n"))
    if ''.join(p for p in x) in ["Q","quit","q","Quit","QUIT"]:
        sys.exit(1)
    print(x)
    return x

def input_check(x,i,u=False):
    while not u:
        x, u = entry_check(x,i)
    x, c = length_check(x,i)
    return x, u

def length_check(x,i):
    while len(x) != 9:
        print("Invalid entry. Please enter the 9 entries from the indicated row using zeroes for blank entries:")
        x = INPUT(i)
    x, c = input_error(x,i)
    return x, c

def entry_check(x,i,c = False,u = True):
    for p in x:
        try:
            h = int(p)
        except ValueError:
            print("Invalid entry. Each space must be an integer 0-9.")
            u = False
            return x,u
    return x, u

def input_error(x,i):
    c = raw_input("Is this correct? (y/n)\n")
    while c == "n":
        print("Please input the row again: ")
        x = INPUT(i)
        x,c = input_check(x,i)
    return x,c

def puzzprint(n):
    print '+ - - - + - - - + - - - +'
    for p in range(3):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(3,6):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'
    for p in range(6,9):
        print '|',
        for i in range(3):
            print n[p][i],
        print '|',
        for i in range(3,6):
            print n[p][i],
        print '|',
        for i in range(6,9):
            print n[p][i],
        print '|'
    print '+ - - - + - - - + - - - +'

### Transforms

def transpose(n):
    """Takes a list-style Matrix and gives back the transpose"""
    d = [[n[j][i] for j in range(len(n[0]))] for i in range(len(n))]
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

### useful functions

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
    # column then row
    for w in range(2):
        n = transpose(n)
        n = step(n)
    return n
    
def boxxy(n):
    # box
    n = box(n)
    n = step(n)
    n = box(box(n))
    return n
    
def solve(n):
    n = rc(n)
    n = boxxy(n)
    n = confirm(n)
    return n
    
def var(n,t=0):
    # Gives coordinates for spot with the least number of variables.
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
    # First Brute force, this method does not incude a backtracking 
    # function as it is the first place for a source of error.
    # Finds the variable with the lowest number of possiblities
    # cycles through the variables until the correct one has been found.
    m = var(n)
    for i in range(m[0]):
        n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
        u = False
        while not solved(n):
            n1 = n
            n = solve(n)
            if bfcondition(n):
                # Backtrack: error raised
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
    return n
    
def bruteforce2(n,xfs):
    # Finds the variable with the lowest number of possiblities
    # cycles through the variables until the correct one has been found.
    m = var(n)
    for i in range(m[0]):
        n[m[1][0]][m[1][1]] = n[m[1][0]][m[1][1]][i]
        u = False
        while not solved(n):
            n1 = n
            n = solve(n)
            if bfcondition(n):
                # backtrack: error raised
                n = xfs[-1]
                m = var(n)
                break
            elif n == n1:
                # New forced solution needed
                n2 = failsafe(n)
                xfs.append(n2)
                n, u = bruteforce2(n,xfs)
                if solved(n):
                    break
                elif bfcondition(n):
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
    # Recreates list from scratch so that the failsafe does not get redefined later.
    n1 = [i for i in n]
    return n1

def puzzle_setup(x):      
    xc = [i for i in range(1,10)]
    print "Here's your puzzle:\n"
    puzzprint(x)
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
    return xgrid
    
def solve_puzzle(xgrid):
    xgrid = puzzle_setup(xgrid)
    start = time.clock()
    t = 0
    while not solved(xgrid):
        xgrid1 = failsafe(xgrid)
        xgrid = solve(xgrid)
        if xgrid == xgrid1:
            xgrid2 = failsafe(xgrid)
            xfs = [xgrid2]
            xgrid = bruteforce1(xgrid,xfs)
    end = time.clock()
    t = end - start
    return t,xgrid

### RUNNING PORTION ###
print("Welcome!")
print("This program solves Sudoku problems: \n")
print("Enter the digits in your puzzle row by row.")
print("At anytime hitting enter is ok instead of typing yes(y).\n")
print("Typing quit during the input process will end the program.")
print("Type a digit for a digit and a 0 (zero) for a blank entry: ")

if __name__ == "__main__":
    exit = "y"
    while exit != "n":
        x = rowbyrow()
        t,xgrid = solve_puzzle(x)
        print "You're puzzle has been solved!\n"
        print "It took " + str(t) + " secs."
        puzzprint(xgrid)
        print '\n'
        
        exit = raw_input("Another puzzle? (y/n): ")
        
    
    
    
