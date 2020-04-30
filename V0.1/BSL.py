# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:42:20 2020

@author: S
"""

import numpy as np

'''
coil_points is a numpy array with shape [3,n] where n 
is the number of points. ie. it is the coulmn of all the x points
next to the coulm the y points and a coulmn of z points. 

ex: 
x = np.asarray([0,1,2])
y = np.asarray([0,0,0])
z = np.asarray([0,0,0])

coil_points = np.asarray([x,y,z]).T
or
[0,0,0]
[1,0,0]
[2,0,0]


The target points are a 2d array each with shape shape(n,1) and then
stacked:
    
px = np.asarray([0,1])
py = np.asarray([1,1])
pz = np.asarray([0,0])

target_points = np.asarray([px,py,pz])
or
[0,1]
[1,1]
[0,0]

'''



def BSL(I,coil_points,target_points):
    x = coil_points[:,0]
    y = coil_points[:,1]
    z = coil_points[:,2]
    
    px = np.asarray([target_points[0,:]]).T
    py = np.asarray([target_points[1,:]]).T
    pz = np.asarray([target_points[2,:]]).T
    
    c = 10**-7 # T*m/A 
    
    xm = ((x[0:len(x)-1]+(np.diff(x)/2))[np.newaxis])
    ym = (y[0:len(y)-1]+(np.diff(y)/2))[np.newaxis]
    zm = (z[0:len(z)-1]+(np.diff(z)/2))[np.newaxis]
    
    
    rhatx = px-xm
    rhaty = py-ym
    rhatz = pz-zm
    
    # r = [:,n,:] for n points
    r = np.asarray(np.sqrt((rhatx**2)+(rhaty**2)+(rhatz**2))).T
    r = np.reshape(r,(r.shape[0],r.shape[1],1))
    
    #rhat[:,n,:] for point n
    rhat = np.asarray([rhatx,rhaty,rhatz]).T
    
    
    dl = np.concatenate((np.asarray([np.diff(x)]).T,
                        np.asarray([np.diff(y)]).T,
                        np.asarray([np.diff(z)]).T),
                        axis = 1)
    
    
    dl = np.asarray([dl])
    dl = np.reshape(dl,(x.size-1,3,1))
    #dlxr = []:,n,:] for n points
    dlxr = np.cross(dl,rhat,axisa = 1)
    
    db = (c*I)*(dlxr/r)
    B_field = np.sum(db,axis = 0)
    
    return B_field

# x = np.asarray([0,1,2])
# y = np.asarray([0,0,0])
# z = np.asarray([0,0,0])

# px = np.asarray([[0, 1]]).T
# py = np.asarray([[1, 1]]).T
# pz = np.asarray([[0, 0]]).T

# I = 1

# B_field = BSL(I,x,y,z,px,py,pz)







