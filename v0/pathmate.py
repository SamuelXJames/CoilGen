#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.preprocessing import normalize

#path = np.asarray([x,y,z])

def path_mate(path,r=0.25):
    #What should r be?
    #Last Point is Missing
    
    
    vdiff = np.asarray([np.diff(path[0]),
                        np.diff(path[1]),
                        np.diff(path[2])])
    
    #Check nvec is not in vdiff
    nvect1 = np.asarray([1,0,0])
    v1 = np.cross(nvect1,np.transpose(vdiff))
    v1 = normalize(v1)
    v2 = np.cross(v1,np.transpose(vdiff))
    v2 = normalize(v2)
        
    # #For now use the same size for theta and path/v1/v2
    # #Future pad the arrays? Set sizes for theta and path?
    theta = np.linspace(0,2*np.pi,np.size(vdiff[1,:]))
    
    # #Last Value Issue!
    endpoint = len(path[0])-1
    v1x = (v1[:,0][np.newaxis]).T
    v1y = (v1[:,1][np.newaxis]).T
    v1z = (v1[:,2][np.newaxis]).T
    
    v2x = (v2[:,0][np.newaxis]).T
    v2y = (v2[:,1][np.newaxis]).T
    v2z = (v2[:,2][np.newaxis]).T
    
     
      
    
    # Include more than length of Vdiff Points
    theta1 = np.cos(theta)[np.newaxis]
    theta2 = np.sin(theta)[np.newaxis]
    xc =  np.reshape(path[0][0:endpoint],(endpoint,1)) + -1*(r*np.dot(v1x,theta1) + r*np.dot(v2x,theta2))
    yc =  np.reshape(path[1][0:endpoint],(endpoint,1)) + -1*(r*np.dot(v1y,theta1) + r*np.dot(v2y,theta2)) 
    zc =  np.reshape(path[2][0:endpoint],(endpoint,1)) + -1*(r*np.dot(v1z,theta1) + r*np.dot(v2z,theta2))
    
    return ([xc,yc,zc])
    
    
    
