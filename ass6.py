
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
data=pd.read_csv("uber.csv",on_bad_lines="skip")

# Preprocessing
data = data.dropna()

# Remove outliers
data["fare_amount"]=pd.to_numeric(data["fare_amount"])
data=data[(data["fare_amount"])>0 & (data["fare_amount"]<100)]

# Select input and output
X = data[["pickup_longitude", "pickup_latitude",
          "dropoff_longitude", "dropoff_latitude",
          "passenger_count"]]

y = data["fare_amount"]

# Correlation
print(data.corr(numeric_only=True))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
p1 = lr.predict(X_test)

# Random Forest
rf = RandomForestRegressor(n_estimators=10, random_state=42)
rf.fit(X_train, y_train)
p2 = rf.predict(X_test)

# Compare models
print("Linear Regression R2:", r2_score(y_test, p1))
print("Linear Regression RMSE:", mean_squared_error(y_test, p1)**0.5)

print("Random Forest R2:", r2_score(y_test, p2))
print("Random Forest RMSE:", mean_squared_error(y_test, p2)**0.5)
