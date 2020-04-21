# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:12:53 2020

@author: S
"""




import sys
path = 'inside-3d-mesh'
sys.path.append(path) 

from stl import mesh
from is_inside_mesh import is_inside_turbo as is_inside

'''
The folder containing the stl_mesh check needs to be included in the
folder path. I am not sure if it currently is.

readSTL outputs a np array of size (n,3,3) where n is the number
of triangls. Each row in th 3x3 array is the [x,y,z] coordinates
for each vertice of the triangle.

The points for is_inside_stl need to be a 2d numpy array or
(n,3) for n points which can be done as np.asarray([[1,2,3]]) for one
point





'''


class Boundaries:
    
    def __init__(self):
        return None
    
    def readSTL(self,filename):
        stlmesh = mesh.Mesh.from_file(filename)
        vectors = stlmesh.vectors
        
        return vectors
    
    def is_inside_stl(self,vectors,points):
        P_inside_mesh = is_inside(vectors, points)
        
        return P_inside_mesh