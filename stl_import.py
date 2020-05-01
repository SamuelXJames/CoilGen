# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:40:38 2020

@author: S
"""

import vtk
import os
'''
Used to import STL files

'''

class import_stl:
    
    def __init__(self):
        
        return
    
    def readFile(self,filename):
        if os.path.isfile(filename) == False:
            raise FileNotFoundError
            
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        #polydata = reader.GetOutput()
        
        return reader
    
    def mapper(self,reader):
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())
        
        return mapper
    
    def actor(self,mapper):
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        
        return actor
    
    def getActor(self,filename):
        reader = self.readFile(filename)
        mapper = self.mapper(reader)
        actor = self.actor(mapper)
        actor.GetProperty().SetOpacity(0.5)
        
        return actor
        
        









