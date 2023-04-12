# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
# Import machine learning regression models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

# Import dataset and setting variables for features and targets
X = np.loadtxt('x2000_data_after_PCA.txt')


y = np.loadtxt('new_labels.txt')


# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Instantiate regression models
lr = LinearRegression()
dt = DecisionTreeRegressor()
rf = RandomForestRegressor(n_estimators = 10, random_state = 0)
svr = SVR(kernel = 'rbf')

# Train and fit models
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)
svr.fit(X_train, y_train)

# Predict using trained models
y_pred_lr_train = lr.predict(X_train)
y_pred_lr = lr.predict(X_test)
y_pred_dt = dt.predict(X_test)
y_pred_dt_train = dt.predict(X_train)
y_pred_rf = rf.predict(X_test)
y_pred_rf_train = rf.predict(X_train)
y_pred_svr = svr.predict(X_test)
y_pred_svr_train = svr.predict(X_train)

# Evaluate model performance using R-squared metric
from sklearn.metrics import r2_score
print("Linear Regression R-squared: ", r2_score(y_train, y_pred_lr_train))
print("Linear Regression R-squared: ", r2_score(y_test, y_pred_lr))
print("Decision Tree Regression R-squared: ", r2_score(y_train, y_pred_dt_train))
print("Decision Tree Regression R-squared: ", r2_score(y_test, y_pred_dt))
print("Random Forest Regression R-squared: ", r2_score(y_test, y_pred_rf))
print("Support Vector Regression R-squared: ", r2_score(y_test, y_pred_svr))

# plt.scatter(y_train, y_pred_lr_train)
# plt.plot((-230,-130),(-230,-130),'r')


# plt.show()

mape_lr = mean_absolute_percentage_error(y_train, y_pred_lr_train)
mape_svr = mean_absolute_percentage_error(y_train, y_pred_svr_train)
mape_dt = mean_absolute_percentage_error(y_train, y_pred_dt_train)
mape_rf = mean_absolute_percentage_error(y_train, y_pred_rf_train)
print("Mean Absolute Error lr:", mape_lr)
print("Mean Absolute Error:", mape_svr)
print("Mean Absolute Error:", mape_dt)
print("Mean Absolute Error:", mape_rf)