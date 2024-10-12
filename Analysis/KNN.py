from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import json

# Dataset

with open('average_rssi.json','r') as file:
   data = json.load(file)

print(len(data))
# Convert the dataset into feature (RSSI values) and target (X, Y coordinates) arrays
X = [[sample["RCV1"], sample["RCV2"], sample["RCV3"], sample["RCV4"]] for sample in data]
y = [[sample["X"], sample["Y"]] for sample in data]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the KNN regression model
k = 4  # Number of neighbors
knn_regressor = KNeighborsRegressor(n_neighbors=k)
knn_regressor.fit(X_train, y_train)

# Predict the coordinates for the test data
y_pred = knn_regressor.predict(X_test)

# Evaluate the model's performance using mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Example of using the trained model to predict coordinates for a new sample
new_sample = [[-68, -56, -67, -60]]  # RSSI values for a new sample
predicted_coordinates = knn_regressor.predict(new_sample)
print(f"Predicted Coordinates: {predicted_coordinates}")
