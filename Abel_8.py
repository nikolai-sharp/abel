# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:03:44 2016

@author: Liam
"""

import numpy as np
def stewart(a, alpha, beta, gamma, pix, piy, piz, bix,biy,biz,x,y,z, li, tol):
    Rrpy = np.matrix([[np.cos(alpha)*np.cos(beta), 
                       np.cos(alpha)*np.sin(beta)*np.sin(gamma)-np.sin(alpha)*np.cos(gamma),
                        np.cos(alpha)*np.sin(beta)*np.cos(gamma)+sin(alpha)*sin(beta)],
                        [np.sin(alpha)*np.cos(beta), np.sin(alpha)*np.sin(beta)*np.sin(gamma)+
                        np.cos(alpa)*np.cos(gamma), np.sin(alpha)*np.sin(beta)*np.cos(y)-
                        np.cos(alpha)*np.sin(gamma)], [-np.sin(beta), np.cos(beta)*sin(gamma),
                        np.cos(beta)*np.cos(gamma)]])
    xibar = x -bix 
    yibar = y -biy
    zibar = z - biz
    UWV = Rrpy*np.matrix([[pix,piy,piz]])
    f = (xibar + ui)**2 + (yibar +vi)**2 + (zibar + wi)**2 - li**2
    # i need ui vi wi to come from the UWV matrix results. Not sure how to do that.    
    Bi = -f(a)
        while abs(bi)<tol:
            #have it eval f at various fvalues. return a if tol is met
        return Bi
    #NEED TO PUT THE DERIVATIVE IN WHEREVER THAT GOES
        