#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Debugger
@author: Camel Academy
"""

import pdb
import math

def triangle_area(b,h):
    return b*h/2

def circle_area(r):
    rsq = r**2
    return math.pi*rsq

b1 = 4
h1 = 5
print("T1 Area ==>", triangle_area(b1,h1))

b2 = 5
h2 = 4
print("T2 Area ==>", triangle_area(b2,h2))

b3 = 10
h3 = 2
print("T3 Area ==>", triangle_area(b3,h3))

pdb.set_trace()

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