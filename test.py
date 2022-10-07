import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import pandas as pd
import seaborn as sns
 
prevsoil = [67, 70, 72.6, 65.6, 67, 68.6, 66.6, 69.6, 66, 65.6, 63, 65, 64.6, 65.3, 58.6, 65,
            64, 64, 67, 59.6, 61.6, 54.6, 62, 60, 64.3, 64, 63, 60.66, 65.3, 61, 64, 59, 61, 65, 67]
water = [120, 70, 30, 0, 75, 55, 100, 65, 25, 80, 50, 90, 50, 50, 50, 100, 45,
         55, 55, 40, 90, 80, 120, 75, 90, 55, 60, 60, 90, 45, 90, 50, 100, 90, 50]
currtemp = [30, 25, 25, 25, 26, 27, 28, 26, 26, 25, 26, 27, 26, 27, 28, 28,
            27, 26, 26, 28, 29, 31, 28, 28, 29, 29, 29, 28, 27, 28, 29, 28, 28, 29, 29]
currhumid = [26, 72, 63, 62, 62, 56, 45, 69, 62, 65, 59, 40, 57, 57, 45, 51,
             57, 69, 64, 54, 49, 45, 72, 72, 63, 68, 72, 65, 71, 71, 70, 80, 74, 66, 63]
z = np.corrcoef(prevsoil,currtemp)
x = np.corrcoef(currhumid,prevsoil)
y = np.corrcoef(currtemp,currhumid)
w = np.corrcoef(currtemp,water)
m= np.corrcoef(water,currhumid)
n= np.corrcoef(prevsoil,water)
print(" Temperature and soil moisture correlation \n",z)
print(" humidity and soil moisture correlation \n",x)
print(" Temperature and humidity correlation \n",y)
print(" Temperature and water correlation \n",w)
print(" Humidity and water correlation \n",m)
print(" Soil Moisture and water correlation \n",n)



data= pd.read_csv ('data_base.csv')
data.drop(['constant'], axis=1, inplace=True)

corr= data.corr()

fig = plt.figure()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(10, 10, as_cmap=True),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=15,
    horizontalalignment='right'
)
plt.show()




# plt.scatter(x)
# plt.show()
