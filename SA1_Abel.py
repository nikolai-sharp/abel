# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:38:08 2016

@author: Liam
"""

from numpy import math
from sympy.solvers import solve
from sympy import Symbol

l1 = 2
l2 = 2**(1/2)
l3 = 2**(1/2)
gamma = math.pi/2

def findxy(p1,p2,p3,gamma,theta):
#give the function the gamm and theta of pi/4
#should return the x and y
#set up a solver to find x and y.    



def kinematics(p1, p2, p3, gamma):
    from mpmath import *
    mp.dps = 25; mp.pretty = True
    z = Symbol('z')
    a2 = l3*mpmath.cospi(z)-x1
    b2 = l3*mpmath.sinpi(z)
    a3 = l2*mpmath.cospi(z+gamma)-x2
    b3 = l2*mpmath.sinpi(z+gamma)-y2
    n1 = b3*(p2**2-p1**2-a2**2-b2**2)-b2*(p3**2-p1**2-a3**2-b3**2)
    n2 = -a3*(p2**2-p1**2-a2**2-b2**2)-a2*(p3**2-p1**2-a3**2-b3**2)
    d = 2*(a2*b3-b2*a3)
    x = n1/d
    y = n2/d
    func= n1**2+n2**2-p1**2*d**2
    solve(func, z)
    return z
    print z    

kinematics(5.**(1/2),5.**(1/2),5.**(1/2), (1/2))
    
    
    
    