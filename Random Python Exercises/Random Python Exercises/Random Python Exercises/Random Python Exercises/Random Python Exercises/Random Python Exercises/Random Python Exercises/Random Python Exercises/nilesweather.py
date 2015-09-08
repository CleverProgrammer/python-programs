# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:32:55 2015
Temperature varying during the day
@author: Rafeh
"""

import matplotlib.pyplot as plt

def draw_graph():
    time = [1,4,7,10,13,16,19,22]
    temperature = [73, 46, 44, 52, 53, 45, 42, 43]
    plt.xlabel('Time of Day')
    plt.ylabel('Temperature')
    plt.title('Temperature in Niles During The Day')
    plt.plot(time, temperature)
    

if __name__ == '__main__':
    #time = ['1 AM', '4 AM', '7 AM', '10 AM', '1 PM', '4 PM', '7 PM', '10 PM']
    draw_graph()
    plt.show()