from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load iris dataset
X, y = load_iris(return_X_y=True)

# Create ML model
model = RandomForestClassifier()

# Train the model
model.fit(X, y)

# Save trained model to file
joblib.dump(model, "model.pkl")

print("Model trained successfully")
