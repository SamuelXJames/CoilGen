# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:34:57 2020

@author: S
"""

import numpy as np
from PIL import Image
x = np.linspace(0,100,300)
y = x
z = x

points = np.asarray([x,y,z]).T
points = np.reshape(points,(30,30))
img = Image.fromarray(points, 'L')
img.save('my.png')
img.show()