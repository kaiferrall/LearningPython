from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def setData(col):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlabel('Infectivity')
    ax.set_xlabel('X-Position')
    ax.set_ylabel('Y-Position')

    xpos = pd.read_excel("agentPosition.xlsx", sheet_name="Sheet1",
                         usecols=[col], nrows=100)
    ypos = pd.read_excel("agentPosition.xlsx", sheet_name="Sheet1",
                         usecols=[col+1], nrows=100)
    infectivity = pd.read_excel("agentData.xlsx", sheet_name="Sheet1",
                                usecols=[col], nrows=100)

    ax.scatter(xpos, ypos, infectivity, c='b', marker='.')
    plt.savefig("plot_" + str(col) + ".png")


for i in range(0, 49):
    if i % 2 == 0:
        setData(i)

plt.show()
