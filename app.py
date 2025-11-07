
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/fraud_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the request
    data = request.get_json()
    amount = data.get("amount", 0)

    # Create a dummy dataframe for prediction
    # The model expects the same columns as the training data
    # We can create a dataframe with all columns and fill the amount
    # The other columns are not used in this simple example, but are needed for the model
    
    # Create a single row of data for prediction
    # The columns must match the columns used during training
    # We can create a dummy dataframe with the expected columns
    # and then fill in the 'amount' value from the request.
    
    # Create a dictionary with all the features the model was trained on
    # Set all to 0 initially
    features = {
        'amount': amount,
        'location_UK': 0,
        'location_USA': 0,
        'device_type_Mobile': 0,
        'device_type_Tablet': 0
    }
    
    # Create a dataframe from the dictionary
    df = pd.DataFrame([features])

    # Make prediction
    prediction = model.predict(df)[0]
    is_fraud = bool(prediction)

    # Return the result
    return jsonify({"fraud": is_fraud})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
