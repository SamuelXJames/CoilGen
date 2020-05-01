# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:33:33 2020

@author: S
"""

import vtk
'''
Renders the actors



'''


class vtkRender:
    
    def __init__(self): 
        
        return
        
        
    def create_render(self,actors):
        actors = actors
        ren = vtk.vtkRenderer()
        renWin = vtk.vtkRenderWindow()
        renWin.AddRenderer(ren)
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(renWin)
        
        for actor in actors:
            ren.AddActor(actor)
        
        ren.SetBackground(0.1,0.2,0.4)
        renWin.SetSize(200,200)


        #Initialize Render Window
        iren.Initialize()

        
        iren.Start()
    
    def update(self,ren,remActor,addActor):
        ren.RemoveActor(remActor)
        ren.AddActor(addActor)
        renWin.Render()
        
        
        
        
        
        
        
        