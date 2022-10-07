import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
import seaborn as sns

prevsoil = [67, 70, 72.6, 65.6, 67, 68.6, 66.6, 69.6, 66, 65.6, 63, 65, 64.6, 65.3, 58.6, 65,
            64, 64, 67, 59.6, 61.6, 54.6, 62, 60, 64.3, 64, 63, 60.66, 65.3, 61, 64, 59, 61, 65, 67]
water = [120, 70, 30, 0, 75, 55, 100, 65, 25, 80, 50, 90, 50, 50, 50, 100, 45,
         55, 55, 40, 90, 80, 120, 75, 90, 55, 60, 60, 90, 45, 90, 50, 100, 90, 50]
currtemp = [30, 25, 25, 25, 26, 27, 28, 26, 26, 25, 26, 27, 26, 27, 28, 28,
            27, 26, 26, 28, 29, 31, 28, 28, 29, 29, 29, 28, 27, 28, 29, 28, 28, 29, 29]
currhumid = [26, 72, 63, 62, 62, 56, 45, 69, 62, 65, 59, 40, 57, 57, 45, 51,
             57, 69, 64, 54, 49, 45, 72, 72, 63, 68, 72, 65, 71, 71, 70, 80, 74, 66, 63]

plt.scatter(prevsoil,water,c='g',marker='o')
plt.scatter(currtemp,water,c='r',marker='o')
plt.scatter(currhumid,water,c='b',marker='o')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(311, projection='3d')
ax.scatter(prevsoil, currtemp, water, c='r', marker='o')
ax.set_xlabel('Soil Moisture')
ax.set_ylabel('Temperature')
ax.set_zlabel('water amount output (ml)')
ax = fig.add_subplot(312, projection='3d')
ax.scatter(currhumid, currtemp, water, c='r', marker='o')
ax.set_xlabel('Humidity')
ax.set_ylabel('Temperature')
ax.set_zlabel('water amount output (ml)')
ax = fig.add_subplot(313, projection='3d')
ax.scatter(prevsoil, currhumid, water, c='r', marker='o')
ax.set_xlabel('Soil Moisture')
ax.set_ylabel('Humidty')
ax.set_zlabel('water amount output (ml)')
plt.show()


m1 = plt.hist(prevsoil, facecolor='red')
m2 = plt.hist(currhumid, facecolor='green')
m3 = plt.hist(currtemp, facecolor='yellow')
m3 = plt.hist(currtemp, facecolor='yellow')
plt.show()

