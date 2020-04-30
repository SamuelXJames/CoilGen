# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:17:17 2020

@author: S
"""

import sys
path = 'D:\Documents\GaTech\Masters\EE 8803\Final Project\Code\inside-3d-mesh'
sys.path.append(path) 

from stl import mesh
from is_inside_mesh import is_inside_turbo as is_inside
import numpy as np
import os


'''
Some things that will need to evetnuall by fixed:
    a lot of redudancis when importing the mesh - maybe 
    remove it from the folder.
    
    Also the lenght of the coil is pretty much arbiatry.
    Not all points are in space. Do these things matter?



'''


class coil0:
    
    def __init__(self):
        return None
    
    def insideDomain(self):
        
        return None
    
    def randomSamplingMethod(self,numPoints,file):
        stlmesh = mesh.Mesh.from_file(file)
        vectors = stlmesh.vectors
        
        min_corner = np.amin(np.amin(vectors, axis = 0), axis = 0)
        max_corner = np.amax(np.amax(vectors, axis = 0), axis = 0)
        P = (max_corner - min_corner) * np.random.random((4096, 3)) + min_corner
        check = (is_inside(vectors, P))
        P = P[(check ==True),:]
        dist = np.linalg.norm(P[0]-P,axis = 1)


        order = np.argsort(dist)
        P = P[order]
        P = P[0:numPoints]
        
        return P
    
    def cornerMethod(self,numPoints,file):
        stlmesh = mesh.Mesh.from_file(file)
        vectors = stlmesh.vectors
        min_corner = np.amin(np.amin(vectors, axis = 0), axis = 0)
        max_corner = np.amax(np.amax(vectors, axis = 0), axis = 0)
        dv = (max_corner-min_corner)
        dv = dv/dv[0]
        x = np.linspace(min_corner[0],max_corner[0],numPoints)
        y = dv[1]*x
        z = dv[2]*x
        
        P = np.asarray([x,y,z]).T
        
        return P
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    