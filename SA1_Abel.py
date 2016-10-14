

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq as br

#Definitely not the most efficient code, but it works

def f1(theta):          #Function for first problem. I copied this function multiple times rather than
    l1 = 2.0            #accepting other variables for ease of presentation
    l2 = np.sqrt(2)  #set lengths for problem
    l3 = l2
    p1 = np.sqrt(5)
    p2 = p1 #saving calculations, though in a silly place
    p3 = p1
    p1s = 5 #set to 5 rather than squaring the sqrt(5)
    p2s = 5
    p3s = 5
    gamma = (np.pi)/2
    
    x1 = 4.0
    y1 = 0.0
    x2 = 0
    y2 = 4.0
    
    A2 = l3*np.cos(theta) - x1  #using this format is way more spread out than it needs to be
    B2 = l3*np.sin(theta) - y1  #but it helped keep track of things, and saved on some calculations by storing values
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
    
    
def f4(theta): #mostly copied from f1(theta), but with changed default values to fit problem 4
    l1 = 3.0
    l2 = 3*2**(1.0/2)
    l3 = l1
    p1 = 5.0
    p2 = p1 #saving calculations
    p3 = 3.0
    p1s = p1**2 
    p2s = p2**2
    p3s = p3**2
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
    

def graph2(): #plots first function using pyplot
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f1(th))
    plt.axis([-3.2,3.2,-500,33250]) #set bounds for better graph visual
    plt.title('Problem 2 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True)#helps identify zeros
    plt.show()
    
    
    

def graph4(): #plots function for fourth problem for visual verification of roots
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f4(th))
    plt.axis([-3.2,3.2,-500,33250]) #retains the same bounds.. but still shows 0's
    plt.title('Problem 4 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True) #helps identify zeros
    plt.show()
    

    
    
    
def plot3_1():  #plots figure 1.15(a). I implemented a more versatile plot function later
    b1 = [0,0]  #but already had this set up.
    b2 = [4,0]  #values represent x and y coordinates of the bases and vertices
    b3 = [0,4]
    v1 = [1,2]
    v2 = [2,1]
    v3 = [2,3]
    
    #x = [b1[0],b2[0],b3[0],v1[0],v2[0],v3[0]]
    #y = [b1[1],b2[1],b3[1],v1[1],v2[1],v3[1]]
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2) #plots lines between vertices
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'b',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'b',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2 )#plots lines between vertices and given bases
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo') #plots points of bases and vertices. could have found a better way to implement
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([0,4,0,4]) #limits graph so trianles look better
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
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'b',lw=2)#again, plots lines between vertices
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'b',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'b',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)#lines between bases and their vertices
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo') #plots vertices and bases
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([0,4,0,4])
    plt.show()
    
    
    
def plot4(r): #finds the root at given r=1,2,3,4 (roots 1 through 4). this is also copied and used later
    lBounds = [-1,-.5,1,2] #stores the left and right bounds for calculation of roots
    rBounds = [-.5,0,1.5,2.5]
    
        
    
    #this set of if/else statements defines theta based on which
    #r is input. This allows this function to plot multiple positions with 1 function
    if r==1:
        theta = br(f4,lBounds[0],rBounds[0])#uses brents method to calculate the roots. chosen due to ease of input
        
    elif r==2:
        theta = br(f4,lBounds[1],rBounds[1])
        
    elif r==3:
        theta = br(f4,lBounds[2],rBounds[2])
        
    elif r==4:
        theta = br(f4,lBounds[3],rBounds[3])
    else:
        print 'that was not a valid choice'
        return 0
        
    print theta

    l1 = 3.0            #sets values from problem 4. I really need to understand how python 
    l2 = 3*2**(1.0/2)   #handles scope better. I wish it was object oriented.. this would all 
    l3 = l1             #have looked so much better
    p1 = 5.0
    p2 = p1 #saving calculations
    p3 = 3.0
    p1s = p1**2 
    p2s = p2**2
    p3s = p3**2
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
    
    Nx = B3*ppab2-B2*ppab3 #this function does not need squared elements
    Ny = A2*ppab3-A3*ppab2  
    
    D = 2*(A2*B3-A3*B2) 
    
    vx1 = Nx/D #calculates coordinates for vertice 1
    vy1 = Ny/D
    
    vx2 = (vx1 + l3*np.cos(theta)) #calculates coordinates for vertice 2
    vy2 = (vy1 + l3*np.sin(theta))
    
    vx3 = (vx1 + l2*np.cos(theta+gamma)) #calculates coordinates for vertice 3
    vy3 = (vy1 + l2*np.sin(theta+gamma))
    
    b1 = [0,0] #sets the vectors for each base and vertice to be passed to plotany() function
    b2 = [x1,y1]
    b3 = [x2,y2]
    v1 = [vx1,vy1]
    v2 = [vx2,vy2]
    v3 = [vx3,vy3]
    
    
    print 'p1:'#tests the line lengths at each root for verification
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
    
    plotany(b1,b2,b3,v1,v2,v3) #finally plot problem 4 at given root r
    
    
def plotany(b1,b2,b3,v1,v2,v3): #plots stewart platform given all points, takes in vectors of each point
#    b1 = [0,0]
#    b2 = [4,0]
#    b3 = [0,4]
#    v1 = [x1,y1]
#    v2 = [x2,y2]
#    v3 = [x3,y3]
    
    #x = [b1[0],b2[0],b3[0],v1[0],v2[0],v3[0]]
    #y = [b1[1],b2[1],b3[1],v1[1],v2[1],v3[1]]
    
    plt.plot([v1[0],v2[0]],[v1[1],v2[1]],'r',lw=2) #same code as other plot fnctions
    plt.plot([v2[0],v3[0]],[v2[1],v3[1]],'r',lw=2)
    plt.plot([v3[0],v1[0]],[v3[1],v1[1]],'r',lw=2)
    
    plt.plot([b1[0],v1[0]],[b1[1],v1[1]],'b',lw=2)
    plt.plot([b2[0],v2[0]],[b2[1],v2[1]],'b',lw=2)
    plt.plot([b3[0],v3[0]],[b3[1],v3[1]],'b',lw=2)
    
    plt.plot(b1[0],b1[1],'bo')
    plt.plot(b2[0],b2[1],'bo')
    plt.plot(b3[0],b3[1],'bo')
    plt.plot(v1[0],v1[1],'bo')
    plt.plot(v2[0],v2[1],'bo')
    plt.plot(v3[0],v3[1],'bo')
    
    plt.axis([-7,7,0,14])
    plt.grid(True)
    plt.show()
    
    
    
def linLen(p1,p2): #calculates distance between two points for testing. just uses pythagorean theorem
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    
    

def f5(theta): #function for 5th problem, just changes one value from function f4()
    l1 = 3.0
    l2 = 3*(2**(1.0/2))
    l3 = l1
    p1 = 5.0
    p2 = 7.0 #saving calculations
    p3 = 3.0
    p1s = p1**2 
    p2s = p2**2
    p3s = p3**2
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
 
def graph5(): #plots function for 5th problem for visual verification of roots
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f5(th))
    plt.axis([-2,3,-1000,3000])
    plt.title('Problem 5 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True)
    plt.show()    
    
def plot5(r): #operates the same way as plot4(r), but adds 2 cases for the extra roots... 
    lBounds = [-1,-.5,-.25,.25,.75,2.25] #left and right bounds for brents method of finding zeros
    rBounds = [-.5,-.25,.25,.75,1.25,2.75]
    
        
    
    #this set of if/else statements defines theta based on which
    #r is input. This allows this function to plot multiple positions
    if r==1:#case 1 gives strange lengths needs further investigation!!!
        theta = br(f4,lBounds[0],rBounds[0]) #uses brents method to calculate the roots. chosen due to ease of input
        #print root
    elif r==2:
        theta = br(f5,lBounds[1],rBounds[1])
        #print root
    elif r==3:
        theta = br(f5,lBounds[2],rBounds[2])
        #print root
    elif r==4:
        theta = br(f5,lBounds[3],rBounds[3])
    elif r==5:
        theta = br(f5,lBounds[4],rBounds[4])
    elif r==6:
        theta = br(f5,lBounds[5],rBounds[5])
        
    else:
        print 'that was not a valid choice'
        return 0

    print theta
    
    l1 = 3.0 #set default values
    l2 = 3*(2**(1.0/2))
    l3 = l1
    p1 = 5.0
    p2 = 7.0 #saving calculations
    p3 = 3.0
    p1s = p1**2 
    p2s = p2**2
    p3s = p3**2
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
    
    b1 = [0,0] #sets vectors for passing into plotany function
    b2 = [x1,y1]
    b3 = [x2,y2]
    v1 = [vx1,vy1]
    v2 = [vx2,vy2]
    v3 = [vx3,vy3]
    
    
    print 'p1:' #double checks lengths of lines
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
    
    plotany(b1,b2,b3,v1,v2,v3)    #plots stewart platform for problem 5
    
    
    
#LIAM ATTEMPT AT NUMBER 6 (needed modification I think.. or at least finishing)
def f6(theta):  #function for sixth problem.... we don't really need this do we? oh well. helps visualize 
    l1 = 3.0    #number of roots at each location. helped us pick the length for problem 6
    l2 = 3*2**(1.0/2)
    l3 = l1
    p1 = 5.0
    p2 = 9.0 #saving calculations
    p3 = 3.0
    p1s = 25.0 #square root of 5 squared is 5.. no need to calculate this 12 times
    p2s = 81.0
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

def graph6(): #plots function for fourth problem for visual verification of roots
    th = np.arange(-np.pi,np.pi,.01)
    plt.plot(th,f6(th))
    plt.axis([-3.2,3.2,-500,33250])
    plt.title('Problem 6 Graph')
    plt.xlabel('Theta')
    plt.ylabel('Function Value')
    plt.grid(True)
    plt.show()
    
    
def f7(theta, p2): #changed the function slightly to take p2 as a variable
    l1 = 3.0
    l2 = 3*2**(1.0/2)
    l3 = l1
    p1 = 5.0
    #p2 = 5.0 #saving calculations
    p3 = 3.0
    p1s = p1**2 
    p2s = p2**2
    p3s = p3**2
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
    answer = N1s + N2s -p1s*Ds     
    return answer

def counter(length2):#counts the number of roots by counting the number of sign changes. 
    oldx = (-1)*np.pi
    x = oldx+.01
    counter = 0
    while x<np.pi:
        if f7(x,length2)*f7(oldx, length2) < 0: #case counts for sign change
            counter = counter + 1
        oldx = x 
        x = x + .001 #resolution for checking number of roots.. could be insufficient, but it should get us close enough
    return counter
    
def vis7(): #used to visualize problem 7. plots number of roots at 
    p2 = 0.0 
    while p2<12:     
        plt.plot(p2,counter(p2),'b.') #plots the p2 lengths on the x axis, and the corrosponding number of roots on the y axis
        p2 = p2 + .1 #change this to change number of samples\points on graph
    
#    plt.plot(bisect7(3.65,3.75),1,'r*')#added these to help visualize when exactly the number of roots change
#    plt.plot(bisect7(4.8,4.9),3,'r*')
#    plt.plot(bisect7(6.9,7),5,'r*')
#    plt.plot(bisect7(7,7.05),5,'r*')
#    plt.plot(bisect7(7.8,7.9),3,'r*')
#    plt.plot(bisect7(9.2,9.3),1,'r*')
    plt.axis([0,12,0,7])
    plt.show()
    
def bisect7(left,right):#determine the length at which the number of roots changes between two points
    left = float(left) #set bounds
    right = float(right)
    cl = counter(left) #determine number of roots at each bound
    cr = counter(right)
    
    while np.abs(left-right) > .0001:   #use bisection to find when root changes within a tolerance
        middle = (left+right)/2         #moves bounds if middle has the same number of roots as bounds
        #print middle
        cm = counter(middle)
        #print cm
        if cl == cm:
            left = middle
            cl = cm
        elif cr == cm:
            right = middle
            cr = cm
        else:
            print "error for some reason? check counter function?"
    return (left+right)/2

def interval7():
    #find the 6 places the number of roots changes given leg l2
    t1 = bisect7(3.65,3.75) #I chose these numbers after looking at the graph of vis7(), and refining my results
    t2 = bisect7(4.8,4.9)   #after the first run of interval7()
    t3 = bisect7(6.9,7)
    t4 = bisect7(7,7.05)
    t5 = bisect7(7.8,7.9)
    t6 = bisect7(9.2,9.3)
    
    #output results to terminal
    print "There are 0 poses on the intervals (0,{0:.3f})U({1:.3f},infinity)".format(t1,t6)
    print "There are 2 poses on the intervals ({0:.3f},{1:.3f})U({2:.3f},{3:.3f})".format(t1,t2,t5,t6)
    print "There are 4 poses on the intervals ({0:.3f},{1:.3f})U({2:.3f},{3:.3f})".format(t2,t3,t4,t5)
    print "There are 6 poses on the interval ({0:.3f},{1:.3f})".format(t3,t4)
    
    
 #inverse kinematic function built using the following:   
#ANALYSIS AND IMPLEMENTATION OF A 6 DOF
#STEWART PLATFORM-BASED ROBOTIC WRIST
#CHARLES C. NGUYEN, 1 SAMI C. ANTRAZI, l ZHEN-LEI ZHOU l and
#CHARLES E. CAMPBELL Jr 2
def invk(alpha,beta,gamma,x,y,z): #tested using x=0,y=0,z=0. was not able to verify, but much of this seems to work correctly
    #(17) from article. This finds orientation between the base and payload given pitch, yaw, and rotation
    R = np.matrix([[np.cos(alpha)*np.cos(beta), np.cos(alpha)*np.sin(beta)*np.sin(gamma)-np.sin(alpha)*np.cos(gamma),
                    np.cos(alpha)*np.sin(beta)*np.cos(gamma)+np.sin(alpha)*np.sin(gamma)],
                           [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma)+np.cos(alpha)*np.cos(gamma),
                            np.sin(alpha)*np.sin(beta)*np.cos(gamma)-np.cos(alpha)*np.sin(gamma)],[-np.sin(beta),
                            np.cos(beta)*np.sin(gamma),np.cos(beta)*np.cos(gamma)]])
    
    #initialize variables.. not sure of this is necessary in python, but I wanted vectors to be of certain size
    l = [0,0,0,0,0,0]
    thB = np.pi/18.0 #angle between closer vertices on base platform
    thP = np.pi/3.0  #andgle between vertices on payload platform
    A = [0,0,0,0,0,0]
    Le = [0,0,0,0,0,0]
    bix = [0,0,0,0,0,0]
    biy = [0,0,0,0,0,0]
    biz = [0,0,0,0,0,0]
    pix = [0,0,0,0,0,0]
    piy = [0,0,0,0,0,0]
    piz = [0,0,0,0,0,0]
    for i in range(0,6,2): #set odd hex ends for top and base. (1) from article for angles
        A[i]=(np.pi/3.0)*(i+1)-thB/2
        l[i]=(np.pi/3.0)*(i+1)-thP/2
        
    for i in range(1,6,2): #set even hex ends for top and base (2) from article
        A[i]=A[i-1]+thB
        l[i]=l[i-1]+thP
        
    for i in range(0,6,1):
        bix[i] = np.cos(A[i]) #bix, biy, and biz represent (4) from article 
        biy[i] = np.sin(A[i])   #calculate x y and z coordinates of base vertices in terms of base coordinate system
        biz[i] = 0
        pix[i] = np.cos(l[i]) #pix, piy, and piz prepresent (3) from article
        piy[i] = np.sin(l[i]) #calculate x y and z coordinates of payload vertices in terms of payload coordinate system
        piz[i] = 0
         #16 from article. calculates length of each leg.
        Le[i] = np.sqrt(x**2+y**2+z**2 + 2   +2*((R[0,0])*pix[i]+(R[0,1])*piy[i])*(x-bix[i])  
                                            +2*((R[1,0])*pix[i]+(R[1,1])*piy[i])*(y-biy[i])
                                            +2*((R[2,0])*pix[i]+(R[2,1])*piy[i])*z + 2*(x*bix[i]+y*biy[i]))
        
    
        print "length of leg {0:}: {1:.3f}".format(i+1,Le[i])
    #print R
    #print R
    sum1 = 0
    sum2 = 0
    sum3 = 0    
    #
    for i in range(0,3,1): #from (14) in article.
        sum1 = sum1 + R[i,0]**2
        sum2 = sum2 + R[i,1]**2
        sum3 = sum3 + R[i,2]**2
    
    print sum1  #these three sums should = 1
    print sum2
    print sum3
    
    
    
    