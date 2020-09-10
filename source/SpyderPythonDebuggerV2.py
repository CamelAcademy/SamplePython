#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Python Debugger: module to help us debug Python code
The most simplest debugger is print statement but Python Debugger is better than it for sure as we can:
set breakpoint, examine variables, execuite line by line, step into function, complete to end and lot more 

Debugger will help us to figure out when when we do not wrong results.

set_trace() is the 1st break point then we can use below command line operations in pdb command prompt:
help - type help <topic>
n - execute next line
s - step into function call
p - print variable value p(n) or just variable name
b - show all breakpoints
b # - set a breakpoint with line number 
l - list 3 lines above and below current line
cl - clear all breakpoints
cl # - clear breakpoint on line number
c - complete to end or continue to next breakpoint """

#import pdb
import math

def triangle_area(b,h):
    return b*h/2

def circle_area(r):
    return math.pi*(r**2)

b1 = 4
h1 = 5
print("T1 Area ==>", triangle_area(b1,h1))

b2 = 5
h2 = 4
print("T2 Area ==>", triangle_area(b2,h2))

b3 = 10
h3 = 2
print("T3 Area ==>", triangle_area(b3,h3))

#pdb.set_trace()

r1 = 1
print("C1 Area ==>", circle_area(r1))

r2 = 2
print("C2 Area ==>", circle_area(r2))

r3 = 3
print("C3 Area ==>", circle_area(r3))

ratio21 = circle_area(r2)/circle_area(r1)
print("R21 Ratio ==>", ratio21)

ratio31 = circle_area(r3)/circle_area(r1)
print("R31 Ratio ==>", ratio31)