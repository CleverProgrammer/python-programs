import matplotlib.pyplot as plt
import numpy as np


def loadfile(filename):
    """
    We want this function to return a tuple of 2 lists:
    one for high temperatures and one for low temperatures.
    """
    f = open(str(filename), 'r')
    highs = []
    lows = []
    for line in f:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        highs.append(fields[1])
        lows.append(fields[2])
    return lows, highs


def produce_plot(lowtemps, hightemps):
    """
    :param lowtemps: list
    :param hightemps: list
    """
    diff_temps = [int(high) - int(low) for low, high in zip(lowtemps, hightemps)]
    plt.figure(1)
    plt.plot(diff_temps)
    plt.title('Day by Day Ranges in Boston in July 2012')
    plt.xlabel('Days')
    plt.ylabel('Temperature Ranges')
    plt.savefig('Figure-TemperatureRangesinBoston.png')
    plt.show()

produce_plot(*loadfile('julyTemps.txt'))


def run_playground():
    plt.figure(1)
    low, high = loadfile('julyTemps.txt')
    plt.plot(low)
    plt.plot(high)
    plt.title('Boston July Temperatures')
    plt.xlabel('Day')
    plt.ylabel('Low/High')
    plt.savefig('Figure-BostonJulyTemperatures.png')
