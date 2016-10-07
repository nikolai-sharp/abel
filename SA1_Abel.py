# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:38:08 2016

@author: Liam
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq as br



def f1(theta): #Function for first problem
    #l1 = 2.0
    l2 = 2**(1.0/2)
    l3 = l2
    p1 = 5**(1.0/2)
    p2 = p1 #saving calculations
    p3 = p1
    p1s = 5.0 #square root of 5 squared is 5.. no need to calculate this 12 times
    p2s = 5.0
    p3s = 5.0
    gamma = (np.pi)/2
    
    x1 = 4.0
    y1 = 0.0
    x2 = 0
    y2 = 4.0
    
    A2 = l3*np.cos(theta) - x1
    B2 = l3*np.sin(theta) - y1
    A3 = l2*(np.cos(theta)*np.cos(gamma)-np.sin(theta)*np.sin(gamma)) - x2
    B3 = l2*(np.cos(theta)*np.sin(gamma)+np.sin(theta)*np.cos(gamma)) - y2
    A2s = A2**2
    B2s = B2**2
    A3s = A3**2
    B3s = B3**2
    ppab2 = p2s-p1s-A2s-B2s
    ppab3 = p3s-p1s-A3s-B3s
    
    N1s = (B3*ppab2-B2*ppab3)**2
    N2s = (A2*ppab3-A3*ppab2)**2  #I swapped the order so the negatives would match
    
    Ds = 4*(A2*B3-A3*B2)**2
    
    return N1s + N2s -p1s*Ds
    
def f4(theta): #function for fourth problem
    l1 = 3.0
    l2 = 3*2**(1.0/2)
    l3 = l1
    p1 = 5.0
    p2 = p1 #saving calculations
    p3 = 3.0
    p1s = 25.0 #square root of 5 squared is 5.. no need to calculate this 12 times
    p2s = 25.0
    p3s = 9.0
    gamma = (np.pi)/4
    
    x1 = 5.0
    y1 = 0.0
    x2 = 0
    y2 = 6.0
    
    A2 = l3*np.cos(theta) - x1
    B2 = l3*np.sin(theta) - y1
    A3 = l2*(np.cos(theta)*np.cos(gamma)-np.sin(theta)*np.sin(gamma)) - x2
    B3 = l2*(np.cos(theta)*np.sin(gamma)+np.sin(theta)*np.cos(gamma)) - y2
    A2s = A2**2
    B2s = B2**2
    A3s = A3**2
    B3s = B3**2
    ppab2 = p2s-p1s-A2s-B2s
    ppab3 = p3s-p1s-A3s-B3s
    
    N1s = (B3*ppab2-B2*ppab3)**2
    N2s = (A2*ppab3-A3*ppab2)**2  #I swapped the order so the negatives would match
    
    Ds = 4*(A2*B3-A3*B2)**2
    
    return N1s + N2s -p1s*Ds    
    

def graph2(): #plots first function
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f1(th))
    plt.axis([-3.2,3.2,-500,33250])
    plt.title('Problem 2 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True)
    plt.show()
    
    
    

def graph4(): #plots function for fourth problem for visual verification of roots
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f4(th))
    plt.axis([-3.2,3.2,-500,33250])
    plt.title('Problem 4 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True)
    plt.show()
    
    
def plot3_1(): #plots figure 1.15(a)
    b0 = [0,0]
    b1 = [4,0]
    b2 = [0,4]
    v0 = [1,2]
    v1 = [2,1]
    v2 = [2,3]
    
    #x = [b0[0],b1[0],b2[0],v0[0],v1[0],v2[0]]
    #y = [b0[1],b1[1],b2[1],v0[1],v1[1],v2[1]]
    
    plt.plot([v0[0],v1[0]],[v0[1],v1[1]],'b',lw=2)
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)
    plt.plot([v2[0],v0[0]],[v2[1],v0[1]],'b',lw=2)
    
    plt.plot([b0[0],v0[0]],[b0[1],v0[1]],'b',lw=2)
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    
    plt.plot(b0[0],b0[1],'bo')
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(v0[0],v0[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    
    plt.axis([0,4,0,4])
    plt.show()
    
    
def plot3_2(): #plots figure 1.15(b)
    b0 = [0,0]
    b1 = [4,0]
    b2 = [0,4]
    v0 = [2,1]
    v1 = [3,2]
    v2 = [1,2]
    
    #x = [b0[0],b1[0],b2[0],v0[0],v1[0],v2[0]]
    #y = [b0[1],b1[1],b2[1],v0[1],v1[1],v2[1]]
    
    plt.plot([v0[0],v1[0]],[v0[1],v1[1]],'b',lw=2)
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)
    plt.plot([v2[0],v0[0]],[v2[1],v0[1]],'b',lw=2)
    
    plt.plot([b0[0],v0[0]],[b0[1],v0[1]],'b',lw=2)
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    
    plt.plot(b0[0],b0[1],'bo')
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(v0[0],v0[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    
    plt.axis([0,4,0,4])
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    