# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:17:17 2020

@author: S
"""

from stl import mesh
from is_inside_mesh import is_inside_turbo as is_inside
import numpy as np
import os


'''
Generate the Initial Coil for Optimization

The randomSamplingMethod picks points inside the env domain
while the corner method just picks points between the env's corners

'''


class coil0:
    
    def __init__(self):
        return None
    
    def insideDomain(self):
        
        return None
    
    def randomSamplingMethod(self,coil_length,vol):
        index = np.random.choice(vol.shape[0],1)
        point0 = vol[index,:]
        vol = np.delete(vol,index,0)
        coil_distance = 0
        points = point0
        length = 0
        while length<=coil_length:
            difference = points[len(points)-1,:]-vol
            distance = np.linalg.norm(difference,axis = 1)
            index = np.where(distance == min(distance))
            endpoint = vol[index]
            vol = np.delete(vol,index,0)
            length = np.linalg.norm(endpoint-point0)
            print(length)
            points = np.vstack((points,endpoint))
        
        return points
    
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
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    