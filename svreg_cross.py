import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, cross_val_predict
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt
# Importing the dataset
df = pd.read_csv('data_base.csv')

# df.drop(['sr_no'], axis=1, inplace=True)
# df = pd.get_dummies(df)
train, test = train_test_split(df, test_size=0.3)

x_train = train.drop('water', axis=1)
y_train = train['water']

x_test = test.drop('water', axis=1)
y_test = test['water']
   
#all Data
X = df.drop('water', axis = 1)
y = df['water']

plt.scatter(df['soil_moisture'], df['temperature'])
plt.show()
from sklearn.svm import SVR
regressor1 = SVR(kernel='rbf', gamma='auto', epsilon=0.02)
regressor2 = SVR(kernel='linear', gamma='auto')
regressor3 = SVR(kernel='poly', gamma='auto', degree=2, epsilon=0.3,
               coef0=1)

regressor1.fit(x_train, y_train)
regressor2.fit(x_train, y_train)
regressor3.fit(x_train, y_train)

# Predicting a new result
y_rbf = regressor1.predict(x_test)
y_lin = regressor2.predict(x_test)
y_poly = regressor3.predict(x_test)

print("The predicted output waterlevel using rbf kernel is=",y_rbf[-1], "ml")
print("The predicted output waterlevel using linear kernel is=",y_lin[-1], "ml")
print("The predicted output waterlevel using polynomial kernel is=",y_poly[-1], "ml")

error = sqrt(mean_squared_error(y_test, y_rbf))  # calculate rmse
print('RMSE value for rbf kernel', error)

error1 = sqrt(mean_squared_error(y_test, y_lin))  # calculate rmse
print('RMSE value for linear kernel', error1)

error2 = sqrt(mean_squared_error(y_test, y_poly))  # calculate rmse
print('RMSE value for polynomial kernel', error2)

from sklearn.metrics import r2_score
print(r2_score(y_test,y_rbf))
print(r2_score(y_test,y_lin))
print(r2_score(y_test,y_poly))



#################################################
# Cross Validation

# #Simple 3 way crossvalidation
# scores = cross_val_score(regressor1, X, y, cv=3)
# print("Cross validation scores for rbf = ", scores)

# scores = cross_val_score(regressor2, X, y, cv=3)
# print("Cross validation scores for Linear kernel = ", scores)

# scores = cross_val_score(regressor3, X, y, cv=3)
# print("Cross validation scores for polynomial kernel = ", scores)

# #crossval predict
# y_coss_predic = cross_val_predict(regressor1, X, y, cv=3)
# print("Cross validation prediction of water level for rbf", y_coss_predic[-1], "ml")

# y_coss_predic = cross_val_predict(regressor2, X, y, cv=3)
# print("Cross validation prediction of water level for linear kernel", y_coss_predic[-1], "ml")

# y_coss_predic = cross_val_predict(regressor3, X, y, cv=3)
# print("Cross validation prediction of water level for polynomial kernel", y_coss_predic[-1], "ml")


# #cross validation plotting
# fig, ax = plt.subplots()
# ax.scatter(y, y_coss_predic, edgecolors=(0, 0, 0))
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
# ax.set_title('Cross Validation in SVR')
# ax.set_xlabel('Measured value of y')
# ax.set_ylabel('Predicted value of y')
# plt.show()


