# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:56:34 2020

@author: S
"""

import numpy as np
import stl_import
import vtkObject


'''


SHould it be such that if you wish to define multiple 
domains you are able to upload all files from a folder
and maybe udf files are read as txt tiles.
    - I dont't think it is necessar to have a params
    just call the correct function

currently stlDomain takes the filenames
and udfDoman takes in raw data - although this is not properly 
setup to take data



'''


class fieldDomain:
    
    
    def __init__(self):
        return
    
    def stlDomain(self,filenames):
        
        actors = []
        stl = stl_import.import_stl()
        for filename in filenames:
            actors.append(stl.getActor(filename))
            
        return actors
    
    def udfDomain(self,data):
        actors = []
        obj_class = vtkObject()
        for domain in data:
            actors.append(obj_class.getActor(domain))
        
        return actors
        
            
            
        
        
                
















            