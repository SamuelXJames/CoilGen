# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:37:08 2020

@author: S
"""
import sys
sys.path.append('D:\Documents\GaTech\Masters\EE 8803\Final Project\Code\BiotS')
path2 = 'D:\Documents\GaTech\Masters\EE 8803\Final Project\Code\inside-3d-mesh'
sys.path.append(path2) 
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
fig = plt.figure()
ax = plt.axes(projection='3d')
#initialize classes
fd = fieldDomain()
ren = vtkRender()
obj = vtkObject()
c0 = coil0()
mf = magfield()


folder = 'D:\Documents\GaTech\Masters\EE 8803\Final Project\STL'
filename = 'cube.STL' 
file = os.path.join(folder,filename)
stlmesh = mesh.Mesh.from_file(file)
stl_actor = fd.stlDomain([file])
stl_actor = stl_actor[0]
stl_actor.GetProperty().SetOpacity(0.5)
vectors = stlmesh.vectors
numPoints = 300
path = c0.cornerMethod(numPoints,file)
#path2 = path.reshape(30,30)
#path3 = path2.reshape(300,3)
# objActor = obj.getActor(path,path3d=False)
# objActor.GetProperty().SetDiffuseColor([255,0,0])

# npoints = 10
# nspacing = 1
# bs_domain = mf.withinDomain_mid(npoints,nspacing,file)

# B = bsl(1,path,bs_domain)
# bs_domain = bs_domain.T

# bs_domain_pd = pd.DataFrame(bs_domain).to_csv('bs_domain.csv')
# B_pd = pd.DataFrame(B).to_csv('B.csv')
# check = (is_inside(vectors, bs_domain))
# ideal_domain = np.zeros([B.shape[0],1])
# ideal_domain[np.where(check==True)[0]]=1
# ideal_domain_pd = pd.DataFrame(ideal_domain).to_csv('ideal_domain.csv')
path_pd = pd.DataFrame(path).to_csv('path.csv')
# # actors = [stl_actor, objActor]
# # ren.create_render(actors)



