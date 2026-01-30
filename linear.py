import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 40 + 10* X + np.random.randn(100, 1)

model = LinearRegression()
model.fit(X, y)

print(f"Formula: y = {model.intercept_[0]:.2f} + {model.coef_[0][0]:.2f}*x")

X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

plt.scatter(X, y, alpha=0.5)
plt.plot(X_new, y_pred, 'r-', linewidth=3)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.grid(True)
plt.show()

test_value = np.array([[1.5]])
prediction = model.predict(test_value)
print(f"Prediction for x={test_value[0][0]}: {prediction[0][0]:.2f}")