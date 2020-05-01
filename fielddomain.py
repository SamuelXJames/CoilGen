# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:56:34 2020

@author: S
"""

import numpy as np
import stl_import
import vtkObject
import os
from stl import mesh
from magfield import magfield
from is_inside_mesh import is_inside_turbo as is_inside
'''
Defines the environment (env) domain


'''


class fieldDomain:
    
    
    def __init__(self):
        return
    
    def stlDomain(self,folder):
        filenames = [os.path.join(folder,file) for 
                     file in os.listdir(folder)]
        
        actors = []
        stl = stl_import.import_stl()
        for filename in filenames:
            actors.append(stl.getActor(filename))
            
        return actors
    
    def volApprox(self,file):
        mf = magfield()
        stlmesh = mesh.Mesh.from_file(file)
        vectors = stlmesh.vectors
        npoints = 15 #Should be Adaptable 
        points = mf.withinDomain_mid(npoints,file)
        points = points.T
        check = (is_inside(vectors, points))
        vol = points[check==True]
        
        return vol
    
    def udfDomain(self,data):
        actors = []
        obj_class = vtkObject()
        for domain in data:
            actors.append(obj_class.getActor(domain))
        
        return actors
        
            
            
        
        
                
















            