# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:37:08 2020

@author: S
"""
import pandas as pd
import os
import vtk
import numpy as np
from fielddomain import fieldDomain
from render import vtkRender
from vtkObject import vtkObject
from coil0 import coil0
from magfield import magfield
from BSL import BSL as bsl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from stl import mesh
from is_inside_mesh import is_inside_turbo as is_inside
#initialize classes
fd = fieldDomain()
ren = vtkRender()
obj = vtkObject()
c0 = coil0()
mf = magfield()

coil_length = 100 #Length of the coil
npoints = 10 #num points to sample the environment (and sorrounding) domain

#Folder containig only the STL Files
folder = 'D:/Documents/GaTech/Masters/EE 8803/Final Project/STL/test'
env = fd.stlDomain(folder)

filenames = [os.path.join(folder,file) for 
             file in os.listdir(folder)]

coil_domain = filenames[0]
vol = fd.volApprox(coil_domain)
init_coil = c0.randomSamplingMethod(coil_length,vol)
init_coil_actor = obj.getActor(init_coil)

bs_domain = mf.withinDomain_mid(npoints,coil_domain)

B = bsl(1,init_coil,bs_domain)
B_mag = np.sum(B**2,1)**0.5
pd.DataFrame(B).to_csv('B_field.csv')
pd.DataFrame(B_mag).to_csv('B_field_mag.csv')

actors = env.append(init_coil_actor)
#Coil_optimized = DCGAN(coil,field)

ren.create_render(env)







