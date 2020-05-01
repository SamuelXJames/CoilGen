# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:34:57 2020

@author: S
"""

'''
Convert coil to an image. Default shape is (30,30)



'''
import numpy as np
from PIL import Image

def coil_to_image(coil,shape = (30,30)):

points = np.reshape(points,shape)
img = Image.fromarray(points, 'L')
img.save('my.png')
img.show()

return img