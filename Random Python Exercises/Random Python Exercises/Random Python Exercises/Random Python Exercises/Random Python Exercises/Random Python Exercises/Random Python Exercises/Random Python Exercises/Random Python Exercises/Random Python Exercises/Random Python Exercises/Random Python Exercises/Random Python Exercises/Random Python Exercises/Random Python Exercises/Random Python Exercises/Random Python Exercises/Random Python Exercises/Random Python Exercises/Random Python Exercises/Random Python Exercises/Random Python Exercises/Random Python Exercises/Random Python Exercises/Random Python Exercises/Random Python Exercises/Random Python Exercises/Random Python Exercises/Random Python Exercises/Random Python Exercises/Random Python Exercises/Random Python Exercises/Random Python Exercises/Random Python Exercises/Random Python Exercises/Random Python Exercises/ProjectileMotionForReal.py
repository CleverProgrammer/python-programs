# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:13:35 2015
Projectile Motion
@author: Rafeh
"""
from matplotlib import pyplot as plt
import math

def frange (start, final, increment):
    
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    
    return numbers
    
#frange (0, tflight, 0.001)
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    
def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8 #m/s^2
   
    #When final velocity = 0, that's your max peak.
    #Max Peak: vy = u*sin(theta) - g*t = 0 --> solve for t to get tpeak
    tpeak = (u * math.sin(theta))/g 
    
    #Max peak is half the time of total free fall time so...
    tflight = 2 * tpeak
    intervals = frange(0, tflight, 0.001)
   
   #list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    
    draw_graph(x, y)

if __name__ == '__main__':
    user = 0
    theta = 0
    u_list = []
    
    while user != -1:
        user = u_list.append(float(input('Enter initial velocity (m/s): ')))
        print (u_list)
        theta = float(input('Enter the angle of projection (degrees): '))
    
    for u in u_list:
        draw_trajectory(u,theta)
    
    plt.show()
        
        