# Using base install of anaconda
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def examplePlot():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )

    plt.ylim(-2,2)
    plt.show()

def straightLinePlot():
    # interpreted as 3 seperate integers (nrows, ncols, index) of figure
    plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = 30 + (0.5 * t)
    line, = plt.plot(t, s, lw=2) #lw = line width in points

    plt.show()

def quadraticPlot():
    plt.subplot(111)

    x = np.arange(10.00, 41.00, 1.0)
    y = np.power(x - 25, 2) + 20
    line, = plt.plot(x, y, lw=2)

    plt.show()

def logPlot():
    plt.subplot(1,1,1)

    x1 = np.linspace(-1.0, 5.0, 100)
    x2 = np.linspace(-5.0, 1.0, 100)

    y1 =  - np.log(x1)
    y2 = - np.log(1-x2)
    line1, line2 = plt.plot(x1, y1, lw=2), plt.plot(x2, y2, lw=2)

    plt.show()

def sigmoidPlot():
    plt.subplot(111)

    x = np.arange(-10, 10, .5)
    z = 1/(1 + np.exp(-x))
    line, = plt.plot(x, z, lw=2)

    plt.show()

logPlot()
