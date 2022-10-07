from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('data_base.csv')
df.head()

# 


train, test = train_test_split(df, test_size=0.4)

x_train = train.drop('water', axis=1)
y_train = train['water']

x_test = test.drop('water', axis=1)
y_test = test['water']


# rmse_val = []  # to store rmse values for different k
# for K in range(8):
#     K = K+1
#     model = neighbors.KNeighborsRegressor(n_neighbors=K)
#     model.fit(x_train, y_train)  # fit the model
#     pred = model.predict(x_test)  # make prediction on test set
    
#     error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
#     rmse_val.append(error)  # store rmse values
#     print('RMSE value for k= ', K, 'is:', error)
    



# # plotting the rmse values against k values
# print("The predicted water level is ",pred[-1], "ml")
# curve = pd.DataFrame(rmse_val)  # elbow curve
# curve.plot()
# plt.show()

from sklearn.model_selection import GridSearchCV
params = {'n_neighbors':[2,3,4,5,6,7,8,9]}

knn = neighbors.KNeighborsRegressor()

model = GridSearchCV(knn, params, iid = 'warn' ,cv=5)
model.fit(x_train,y_train)
model.best_params_
print("The best value of K is= \n")
print(model.best_params_)
y_pred = model.predict(x_test)

print("The predicted water level is ",y_pred[-1], "ml")
error = sqrt(mean_squared_error(y_test, y_pred))
print("The RMSE value for the KNN regressor is", error)