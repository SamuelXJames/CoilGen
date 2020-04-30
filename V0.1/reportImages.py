# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:11:51 2020

@author: S
"""
import sys
sys.path.append('D:\Documents\GaTech\Masters\EE 8803\Final Project\Code\BiotS')
from stl_boundaries import Boundaries
from fielddomain import fieldDomain
from stl import mesh
from is_inside_mesh import is_inside_turbo as is_inside
import os
import vtk
from vtkObject import vtkObject
from render import vtkRender
from magfield import magfield
import numpy as np
mg = magfield()
ob = vtkObject()
fd = fieldDomain()
folder = 'D:\Documents\GaTech\Masters\EE 8803\Final Project\STL'
#folder = 'D:\Downloads'
filename = 'cube.STL'
filename = 'torroid.STL' 
#filename = 'amforma_132.stl'
#filename = 'hex.STL'
file = os.path.join(folder,filename)
file2 = os.path.join(folder,'coil_loc.STL')
colors = vtk.vtkNamedColors()

npoints = 15
points = mg.withinDomain_mid(npoints,file)
points = points.T
point_actor = mg.viewFieldPoints(points)
stlmesh = mesh.Mesh.from_file(file)
vectors = stlmesh.vectors
check = (is_inside(vectors, points))
ideal_points = points[check==True]
index = np.random.choice(ideal_points.shape[0],1)
point0 = ideal_points[index,:]
ideal_points = np.delete(ideal_points,index,0)
coil_distance = 0
points = point0
length = 0
while length<=100:
    difference = points[len(points)-1,:]-ideal_points
    distance = np.linalg.norm(difference,axis = 1)
    index = np.where(distance == min(distance))
    endpoint = ideal_points[index]
    ideal_points = np.delete(ideal_points,index,0)
    length = np.linalg.norm(endpoint-point0)
    print(length)
    points = np.vstack((points,endpoint))
x = np.linspace(0,100,300)
y = x
z = x
points = np.asarray([x,y,z]).T
coil_actor = ob.getActor(points)
stl_actor = fd.stlDomain([file])
# point_actor = mg.viewFieldPoints(ideal_points)
actor = stl_actor[0]
actor.GetProperty().SetOpacity(0.3)
# coil_actor = stl_actor[1]
coil_actor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
ren = vtkRender()
ren.create_render([coil_actor])
