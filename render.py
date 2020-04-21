# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:33:33 2020

@author: S
"""

import vtk
'''
Notes:
How do I update actors?
It is possible to create a new window each time
-Although not convienant

Example
ren = render.vtk_render()
ren.create_render([actors])



'''


class vtkRender:
    
    def __init__(self): 
        
        return
        
        
    def create_render(self,actors):
        self.actors = actors
        self.ren = vtk.vtkRenderer()
        self.renWin = vtk.vtkRenderWindow()
        self.renWin.AddRenderer(self.ren)
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(self.renWin)
        
        for actor in self.actors:
            self.ren.AddActor(actor)
        
        self.ren.SetBackground(0.1,0.2,0.4)
        self.renWin.SetSize(200,200)


        #Initialize Render Window
        iren.Initialize()

        self.ren.ResetCamera()
        self.ren.GetActiveCamera().Zoom(1.0)
        self.renWin.Render()

        iren.Start()
    
    def update(self,remActor,addActor):
        self.ren.RemoveActor(remActor)
        self.ren.AddActor(addActor)
        self.renWin.Render()
        
        
        
        
        
        
        
        