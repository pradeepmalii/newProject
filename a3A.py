# linear house price

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Sample Data (Experience vs Salary)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20000, 25000, 30000, 35000, 40000])
# Create Model
model = LinearRegression()
# Train Model
model.fit(X, y)
# Prediction
predicted_price = model.predict([[6]])
print("Predicted price of house for 6 years:", predicted_price)
# Plot Graph
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Years")
plt.ylabel("Price")
plt.title("Linear Regression")
plt.show()




# 1. What is regression?
# Ans. Regression is a supervised machine learning technique used to predict a continuous output
# variable based on input variables.
# 2. Difference between linear & logistic regression?
# Ans. Linear Regression is used for predicting continuous values, while Logistic Regression is used for
# classification problems. In Linear Regression, the output is a numeric value such as salary or price,
# whereas in Logistic Regression, the output is a probability between 0 and 1.
# 3. What is sigmoid function?
# Ans. The sigmoid function is a mathematical function used in logistic regression to convert values into
# probabilities between 0 and 1. It helps in classification problems.
# Formula: 𝜎(𝑥)= 1 / (1+𝑒
# -x
# )
# 4. What is fit()?
# Ans. fit() is a method used to train the machine learning model using the given dataset.
# Example: model.fit(X, y)
# It learns the relationship between input (X) and output (y).

# 5. What is predict()?
# Ans. predict() is used to make predictions using the trained model.
# Example: model.predict([[6]])
# It predicts the output for new input data.