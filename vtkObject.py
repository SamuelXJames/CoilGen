# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:48:00 2020

@author: S
"""
import numpy as np
import vtk
import pathmate
import render
'''
coil_class = vtkCoil.Coil()
actor = coil_class.getActor(path,path3d=False,r=0.25)
where path = np.asarray([x,y,z]).T
or the form 
[x1,y1,z1]
[x2,y2,z2]
...ect

-Renaming this to be more generic with geometry and 
not just coils
'''

class vtkObject:
    
    def __init__(self):
        return None
      
        
    def path3d(self,path,r):
        coil3d = pathmate.path_mate(path.T,r)
        x = coil3d[0].flatten('C')
        y = coil3d[1].flatten('C')
        z = coil3d[2].flatten('C')
                   
        return np.asarray([x,y,z])
                
    def polygon(self,coil_points):
        x = coil_points[:,0]
        y = coil_points[:,1]
        z = coil_points[:,2]
        
        points = vtk.vtkPoints()
        lines = vtk.vtkCellArray()
        coil = vtk.vtkPolyData()
        
        npoints = len(x)
        points.SetNumberOfPoints(npoints)
        lines.InsertNextCell(npoints)
        for i in range(npoints):
            points.SetPoint(i, x[i], y[i], z[i])
            lines.InsertCellPoint(i)
        
        coil.SetPoints(points)
        coil.SetLines(lines)
        
        return coil
    
        
    def mapper(self,coil):
        coilMap = vtk.vtkPolyDataMapper()
        coilMap.SetInputData(coil)
        coilMap.Update()
        
        return coilMap
    
    def actor(self,coilMap):
        coilActor = vtk.vtkActor()
        coilActor.SetMapper(coilMap)
        
        return coilActor
    
    def getActor(self,path,path3d=False,r=0.25):
        if path3d:
            path = self.path3d(path,r=0.25)
            path = path.T
        coil = self.polygon(path)
        coilMap = self.mapper(coil)
        actor = self.actor(coilMap)
        
        return actor
            
            
# theta = np.linspace(0,2*np.pi,100)
# x = np.cos(theta)
# y = np.sin(theta)
# z = np.ones(100)

# r = 0.25
# path = np.asarray([x,y,z]).T   
         
# coil3d = pathmate.path_mate(path,r)
# x = coil3d[0].flatten('C')
# y = coil3d[1].flatten('C')
# z = coil3d[2].flatten('C')

# c = Coil()
# actor = c.getActor(path,path3d=False)
        



# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)

# ren.AddActor(actor)

# ren.SetBackground(0.1,0.2,0.4)
# renWin.SetSize(200,200)


# #Initialize Render Window
# iren.Initialize()

# ren.ResetCamera()
# ren.GetActiveCamera().Zoom(1.0)
# renWin.Render()

# iren.Start()