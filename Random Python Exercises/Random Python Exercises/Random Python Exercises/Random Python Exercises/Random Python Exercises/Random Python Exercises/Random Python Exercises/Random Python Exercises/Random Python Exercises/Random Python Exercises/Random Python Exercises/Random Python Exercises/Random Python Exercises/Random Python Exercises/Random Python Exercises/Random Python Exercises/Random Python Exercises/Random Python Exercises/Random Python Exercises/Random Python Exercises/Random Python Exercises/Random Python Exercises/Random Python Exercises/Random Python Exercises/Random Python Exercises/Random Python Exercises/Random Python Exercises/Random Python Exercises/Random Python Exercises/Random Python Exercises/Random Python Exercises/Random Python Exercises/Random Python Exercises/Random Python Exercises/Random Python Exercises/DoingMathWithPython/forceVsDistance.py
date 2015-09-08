# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 03:01:14 2015
Relationship between gravitational force and
distance between two bodies
@author: Rafeh
"""

#Knowns
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def generate_F_r():
    m1 = 0.5
    m2 = 1.5
    G = 6.674*(10**-11)
    r = range(100, 1001, 50)
    F = []

    for dist in r:
        force = (G*m1*m2)/(dist**2)
        F.append(force)

    draw_graph(r, F)

if __name__ == '__main__':
    generate_F_r()

