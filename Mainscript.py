from backend import *
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt
from sklearn import neighbors
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
 
#Data Reading from CSV

df = getdbdata()
X = df[['constant','soil_moisture','temperature','humidity']]
Y = df['water']

soilval = df['soil_moisture'].values.tolist()
tempval = df['temperature'].values.tolist()
humval = df['humidity'].values.tolist()
waterval = df['water'].values.tolist()
const = df['constant'].values.tolist()

# normalization

smin =  min(soilval)
smax = max(soilval)
k= 0
for i in soilval:
    soilval[k] = (i - smin)/(smax-smin)
    k = k+1

tmin =  min(tempval)
tmax = max(tempval)
k= 0
for i in tempval:
    tempval[k] = (i - tmin)/(tmax-tmin)
    k = k+1

hmin =  min(humval)
hmax = max(humval)
k= 0
for i in humval:
    humval[k] = (i - hmin)/(hmax-hmin)
    k = k+1


wmin =  min(waterval)
wmax = max(waterval)
k= 0
for i in waterval:
    waterval[k] = (i - wmin)/(wmax-wmin)
    k = k+1

d = {'const':const,'soilval':soilval,'tempval':tempval,'humval':humval,'waterval':waterval}
df_new = pd.DataFrame(d)

# # Plotting normalized values

plt.scatter(soilval,tempval,c='g',marker='o')
plt.title('Scatter plot ')
plt.xlabel('Soil moisture')
plt.ylabel('Temperature')
plt.show()
plt.scatter(soilval,humval,c='y',marker='o')
plt.title('Scatter plot ')
plt.xlabel('Soil Moisture')
plt.ylabel('Humidity')
plt.show()
plt.scatter(soilval,waterval,c='c',marker='o')
plt.title('Scatter plot ')
plt.xlabel('Soil Moisture')
plt.ylabel('Water level')
plt.show()
plt.scatter(tempval,waterval,c='r',marker='o')
plt.title('Scatter plot ')
plt.xlabel('Temperature')
plt.ylabel('Water Level')
plt.show()
plt.scatter(humval,waterval,c='b',marker='o')
plt.title('Scatter plot ')
plt.xlabel('Humidity')
plt.ylabel('water level')
plt.show()

train, test = train_test_split(df_new, test_size=0.4)

# temp and soilmoisture and humval with constant
x_train = train[['tempval','soilval','const','humval']]
y_train = train['waterval']
x_test = test[['tempval','soilval','const','humval']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','soilval','const','humval']]
y = df_new['waterval']

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)

finalwater= y_pred[-1]*100

finalwaterlvl = int(finalwater)
print("The output waterlevel using linear regression is=",finalwaterlvl,"ml")
error = sqrt(mean_squared_error(y_test, y_pred))  # calculate rmse
print('RMSE value for linear regression is =', error*100)
model = sm.OLS(y,X).fit()
p= model.summary()
print(p)


# #soilmoisture value from sensor
# sensorvalue = int(getmoisinfo())
# print("actual soil moisture value")
# print(sensorvalue)

# #Sending data to arduino
# sendwater(finalwaterlvl)


# #adding data to the database for more accuracy
# temp1,humid1 = getweatherdata()

# adddata(sensorvalue,temp1,humid1,finalwaterlvl)

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="safety",
#   database="plantdb"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO plantdb1 (wateradded, waterlevel) VALUES (%s, %s)"
# val = (finalwaterlvl, waterlevel)
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")