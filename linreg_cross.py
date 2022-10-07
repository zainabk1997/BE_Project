from sklearn.metrics import mean_squared_error
from pandas import DataFrame
import matplotlib.pyplot as plt
from math import sqrt
from sklearn import neighbors
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm
df = pd.read_csv('data_base.csv')

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

# only temp 
x_train = train[['tempval','const']]
y_train = train['waterval']
x_test = test[['tempval','const']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','const']]
y = df_new['waterval']

# only humidity
x_train = train[['humval','const']]
y_train = train['waterval']
x_test = test[['humval','const']]
y_test = test['waterval']
#all Data
X = df_new[['humval','const']]
y = df_new['waterval']

# only soil moisture 
x_train = train[['soilval','const']]
y_train = train['waterval']
x_test = test[['soilval','const']]
y_test = test['waterval']
#all Data
X = df_new[['soilval','const']]
y = df_new['waterval']

# only temp and humidity
x_train = train[['tempval','humval','const']]
y_train = train['waterval']
x_test = test[['tempval','humval','const']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','humval','const']]
y = df_new['waterval']

# only temp and soilmoisture
x_train = train[['tempval','soilval','const']]
y_train = train['waterval']
x_test = test[['tempval','soilval','const']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','soilval','const']]
y = df_new['waterval']

# only humidity and soilmoisture
x_train = train[['humval','soilval','const']]
y_train = train['waterval']
x_test = test[['humval','soilval','const']]
y_test = test['waterval']
#all Data
X = df_new[['humval','soilval','const']]
y = df_new['waterval']

# only temp and soilmoisture and humval
x_train = train[['tempval','soilval','const','humval']]
y_train = train['waterval']
x_test = test[['tempval','soilval','const','humval']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','soilval','const','humval']]
y = df_new['waterval']

# # only temp and soilmoisture and humval without const
x_train = train[['tempval','soilval','humval']]
y_train = train['waterval']
x_test = test[['tempval','soilval','humval']]
y_test = test['waterval']
#all Data
X = df_new[['tempval','soilval','humval']]
y = df_new['waterval']


regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)
print("The output waterlevel using linear regression is=",y_pred[-1]*100,"ml")
error = sqrt(mean_squared_error(y_test, y_pred))  # calculate rmse
print('RMSE value for linear regression is =', error*100)
model = sm.OLS(y,X).fit()
p= model.summary()
print(p)


