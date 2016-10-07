

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
    b1 = [0,0]
    b2 = [4,0]
    b3 = [0,4]
    v1 = [1,2]
    v2 = [2,1]
    v3 = [2,3]
    
    #x = [b1[0],b2[0],b3[0],v1[0],v2[0],v3[0]]
    #y = [b1[1],b2[1],b3[1],v1[1],v2[1],v3[1]]
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'b',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'b',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([0,4,0,4])
    plt.show()
    
    
def plot3_2(): #plots figure 1.15(b)
    b1 = [0,0]
    b2 = [4,0]
    b3 = [0,4]
    v1 = [2,1]
    v2 = [3,2]
    v3 = [1,2]
    
    #x = [b1[0],b2[0],b3[0],v1[0],v2[0],v3[0]]
    #y = [b1[1],b2[1],b3[1],v1[1],v2[1],v3[1]]
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'b',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'b',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([0,4,0,4])
    plt.show()
    
    
    
def plot4(r):
    lBounds = [-1,-.5,1,2]
    rBounds = [-.5,0,1.5,2.5]
    
        
    
    #this set of if/else statements defines theta based on which
    #r is input. This allows this function to plot multiple positions
    if r==1:
        theta = br(f4,lBounds[0],rBounds[0])
        #print root
    elif r==2:
        theta = br(f4,lBounds[1],rBounds[1])
        #print root
    elif r==3:
        theta = br(f4,lBounds[2],rBounds[2])
        #print root
    elif r==4:
        theta = br(f4,lBounds[3],rBounds[3])
        #print root
    else:
        print 'that was not a valid choice'
        return 0

    l1 = 3.0
    l2 = 3*2**(1.0/2)
    l3 = l1
    p1 = 5.0
    p2 = p1 
    p3 = 3.0
    p1s = 25.0
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
    
    Nx = B3*ppab2-B2*ppab3
    Ny = A2*ppab3-A3*ppab2  #I swapped the order so the negatives would match
    
    D = 2*(A2*B3-A3*B2)
    
    vx1 = Nx/D
    vy1 = Ny/D
    
    vx2 = (vx1 + l3*np.cos(theta))
    vy2 = (vy1 + l3*np.sin(theta))
    
    vx3 = (vx1 + l2*np.cos(theta+gamma))
    vy3 = (vy1 + l2*np.sin(theta+gamma))
    
    b1 = [0,0]
    b2 = [x1,y1]
    b3 = [x2,y2]
    v1 = [vx1,vy1]
    v2 = [vx2,vy2]
    v3 = [vx3,vy3]
    
    
    print 'p1:'
    print linLen(v1,b1)
    print 'p2:'
    print linLen(v2,b2)
    print 'p3:'
    print linLen(v3,b3)
    
    print 'l1:'
    print linLen(v2,v3)
    print 'l2:'
    print linLen(v1,v3)
    print 'l3:'
    print linLen(v1,v2)
    
    plotany(b1,b2,b3,v1,v2,v3)
    
    
def plotany(b1,b2,b3,v1,v2,v3): #plots stewart platform given all points
#    b1 = [0,0]
#    b2 = [4,0]
#    b3 = [0,4]
#    v1 = [x1,y1]
#    v2 = [x2,y2]
#    v3 = [x3,y3]
    
    #x = [b1[0],b2[0],b3[0],v1[0],v2[0],v3[0]]
    #y = [b1[1],b2[1],b3[1],v1[1],v2[1],v3[1]]
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'b',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'b',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([-2,7,0,9])
    plt.show()
    
    
    
def linLen(p1,p2): #calculates distance between two points for testing
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    
    