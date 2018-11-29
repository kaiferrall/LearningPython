from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def setData(col):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlabel('Infectivity')
    ax.set_zlim(0, 1)
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


def setData_2D(col):
    fig = plt.figure()
    colors = ["#c62727" for i in range(0, 100)]
    xpos = pd.read_excel("agentPosition.xlsx", sheet_name="Sheet1",
                         usecols=[col], nrows=100)
    ypos = pd.read_excel("agentPosition.xlsx", sheet_name="Sheet1",
                         usecols=[col+1], nrows=100)
    area = pd.read_excel("agentData.xlsx", sheet_name="Sheet1",
                              usecols=[col], nrows=100)*800
    for i in range(0, 99):
        if area.at[i, 1] > 0.85:
            colors[i] = "#d11717"
        elif area.at[i, 1] > 0.5:
            colors[i] = "#d15b17"
        elif area.at[i, 1] > 0.4:
            colors[i] = "#c66627"
        elif area.at[i, 1] > 0.3:
            colors[i] = "#dfe22d"
        elif area.at[i, 1] > .15:
            colors[i] = "#17d1ab"
        else:
            colors[i] = "#17d158"

    plt.scatter(xpos, ypos, s=50, c=colors, alpha=0.65)
    plt.savefig("plot_" + str(col) + ".png")

for i in range(0, 50):
    #setData_2D(i)
    setData(i)
