# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:37:08 2020

@author: S
"""


import os
import vtk
import numpy as np
from fielddomain import fieldDomain
from render import vtkRender
from vtkObject import vtkObject


#initialize classes
fd = fieldDomain()
ren = vtkRender()
obj = vtkObject()

folder = 'D:\Documents\GaTech\Masters\EE 8803\Final Project\STL'
filename = 'cube.STL' 
file = os.path.join(folder,filename)

stl_actor = fd.stlDomain([file])
stl_actor = stl_actor[0]
stl_actor.GetProperty().SetOpacity(0.5)


#
colors = vtk.vtkNamedColors()
x = y = z = np.linspace(0,100,100)
path = np.asarray([x,y,z]).T
objActor = obj.getActor(path,path3d=True)
objActor.GetProperty().SetDiffuseColor([255,0,0])

actors = [stl_actor,objActor]
ren.create_render(actors)














