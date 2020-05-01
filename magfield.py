# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:52:42 2020

@author: S
"""

import numpy as np
from stl_boundaries import Boundaries
import vtk

'''
Defines the magnetic field domain

'''

class magfield:
    
    def __init__(self):
        
        return None
    
    def withinDomain(self,npoints,n,domain_file):
        
        
        bd = Boundaries()
        vectors = bd.readSTL(domain_file)
        x = vectors[:,:,0]
        y = vectors[:,:,1]
        z = vectors[:,:,2]

        xmax = np.amax(x)
        xmin = np.amin(x)
        xc = (xmax-xmin)/2

        ymax = np.amax(y)
        ymin = np.amin(y)
        yc = (ymax-ymin)/2

        zmax = np.amax(z)
        zmin = np.amin(z)
        zc = (zmax-zmin)/2

        lbx = xmin-np.abs((n*xc))
        ubx = xmax+np.abs((n*xc))
        lby = ymin-np.abs((n*yc))
        uby = ymax+np.abs((n*yc))
        lbz = xmin-np.abs((n*zc))
        ubz = xmax+np.abs((n*zc))

        xp = np.linspace(lbx,ubx,npoints)
        yp = np.linspace(lby,uby,npoints)
        zp = np.linspace(lbz,ubz,npoints)


        xp,yp,zp = np.meshgrid(xp,yp,zp)
        xp = np.ravel(xp)
        yp = np.ravel(yp)
        zp = np.ravel(zp)

        return np.vstack([xp,yp,zp])
    
    def withinDomain_mid(self,npoints,domain_file):
        
        
        bd = Boundaries()
        vectors = bd.readSTL(domain_file)
        min_corner = np.amin(np.amin(vectors, axis = 0), axis = 0)
        max_corner = np.amax(np.amax(vectors, axis = 0), axis = 0)
        midpoint = (max_corner - min_corner)/2
        xbound = max_corner[0]-midpoint[0]
        ybound = max_corner[1]-midpoint[1]
        zbound = max_corner[2]-midpoint[2]
        n = npoints
        xlb = midpoint[0]-xbound
        xub = midpoint[0]+xbound
        ylb = midpoint[1]-ybound
        yub = midpoint[1]+ybound
        zlb = midpoint[2]-zbound
        zub = midpoint[2]+zbound
        
        tolerance = 1.1
        density = .90
        n_inside = int(np.ceil(n*density))
        n_outside1 = int(np.ceil((n-n_inside)/2))
        n_outside2 = int(n-n_inside-n_outside1)
        
        xin = np.linspace(xlb,xub,n_inside)
        yin = np.linspace(ylb,yub,n_inside)
        zin = np.linspace(zlb,zub,n_inside)
        
        xlb2 = midpoint[0]-(tolerance*xbound)
        xub2 = midpoint[0]+(tolerance*xbound)
        ylb2 = midpoint[1]-(tolerance*ybound)
        yub2 = midpoint[1]+(tolerance*ybound)
        zlb2 = midpoint[2]-(tolerance*zbound)
        zub2 = midpoint[2]+(tolerance*zbound)
        
        xoutl = np.linspace(xlb2,xlb,n_outside1)
        xout2 = np.linspace(xub,xub2,n_outside2)
        youtl = np.linspace(ylb2,ylb,n_outside1)
        yout2 = np.linspace(yub,yub2,n_outside2)
        zoutl = np.linspace(zlb2,zlb,n_outside1)
        zout2 = np.linspace(zub,zub2,n_outside2)
        
        xp = np.concatenate((xoutl, xin, xout2))
        yp = np.concatenate((youtl, yin, yout2))
        zp = np.concatenate((zoutl, zin, zout2))
        
        xp,yp,zp = np.meshgrid(xp,yp,zp)
        xp = np.ravel(xp)
        yp = np.ravel(yp)
        zp = np.ravel(zp)
        
        return np.vstack([xp,yp,zp])
    
    
    def viewFieldPoints(self,p):
      
       
        colors = vtk.vtkNamedColors()
        Points = vtk.vtkPoints()
        Vertices = vtk.vtkCellArray()
        
        for i in range(len(p)):
            id = Points.InsertNextPoint(p[i][0],p[i][1],p[i][2])
            Vertices.InsertNextCell(1)
            Vertices.InsertCellPoint(id)
                
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(Points)
        polydata.SetVerts(Vertices)
        
       
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(polydata)
        
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
        actor.GetProperty().SetPointSize(4)

      
        return actor
    
    def viewMagfield(self,fieldpoints,Bfield):
        
        
        
        return None
    

    


    
    
    
    
    
    
    
    
    
    
    
    
    
        

