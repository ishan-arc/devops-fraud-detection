
# AI + DevOps Enabled Real-Time Fraud Detection System

## Overview

This project is a real-time fraud detection system for the banking industry. It uses a machine learning model to predict fraudulent transactions and exposes the model via a REST API. The project is containerized using Docker and has a CI/CD pipeline set up with GitHub Actions.

## Tech Stack

* **Programming Language:** Python
* **Frameworks:** Flask, Scikit-learn, Joblib
* **DevOps Tools:** Docker, GitHub Actions

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-devops-fraud-detection.git
   cd ai-devops-fraud-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model:**
   ```bash
   python train_model.py
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```

## How to Build Docker Image

```bash
docker build -t fraud-detector .
```

## How to Run Container

```bash
docker run -p 5000:5000 fraud-detector
```

## How to Test API

### Using cURL

```bash
curl -X POST -H "Content-Type: application/json" -d '{"amount": 9000}' http://localhost:5000/predict
```

### Using Postman

* **URL:** `http://localhost:5000/predict`
* **Method:** `POST`
* **Body:** `raw`, `JSON`
  ```json
  {
      "amount": 9000
  }
  ```

### Expected Output

```json
{
    "fraud": true
}
```
###
