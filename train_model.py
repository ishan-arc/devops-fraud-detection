
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("data/transactions.csv")

# Drop rows with missing values
df = df.dropna()

# Preprocessing (handle categorical features)
df = pd.get_dummies(df, columns=["location", "device_type"], drop_first=True)

# Define features and target
X = df.drop(["is_fraud", "transaction_id"], axis=1)
y = df["is_fraud"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Save the model
joblib.dump(model, "model/fraud_model.pkl")
