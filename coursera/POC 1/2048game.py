# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:12:45 2015
2048grid
@author: Rafeh
"""

grid = []
for col in [0, 1, 2, 3, 4, 5]:
    temp = []
    for row in [0, 1, 2, 3]:
        temp.append(row)
    grid.append(temp)
