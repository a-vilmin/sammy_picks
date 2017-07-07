#!/usr/bin/python
'''
Simplest OpenOpt KSP example;
requires FuncDesigner installed.
For some solvers limitations on time, cputime, "enough" value,
basic GUI features are available.
See http://openopt.org/KSP for more details
'''
from openopt import *
from numpy import sin, cos

N = 150

items = [
         {
             'name': 'item %d' % i,
             'cost': 1.5*(cos(i)+1)**2,
             'volume': 2*sin(i) + 3,
             'mass': 4*cos(i)+5,
             'n':  1 if i < N/3 else 2 if i < 2*N/3 else 3
         } 
         for i in range(N)
         ]
constraints = lambda values: (
                              values['volume'] < 10, 
                              values['mass'] < 100,
                              values['nItems'] <= 10, 
                              values['nItems'] >= 5
                              # we could use lambda-func, e,g.
                              # values['mass'] + 4*values['volume'] < 100
                              )
objective = 'cost'
p = KSP(objective, items, goal='max', constraints=constraints)
r = p.solve('glpk', iprint=0)
