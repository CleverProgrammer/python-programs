# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 01:15:50 2015

@author: Rafeh
"""
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Quadratic Visualization')
    plt.plot(x, y)

def a_quadratic():
    x_values = [-1, 1, 2, 3, 4, 5, 8, 9, 15, 30, 100]
    y_values = []
    
    for x in x_values:
        y = x**2 + 2*x + 1
        print ('x = {0} y = {1}'.format(x, y))
        y_values.append(y)
    
    draw_graph(x_values, y_values)
    plt.show()

if __name__ == '__main__':
    a_quadratic()
    