# UPI / Transaction Fraud Detection

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("creditcard.csv")

# Features and target
X = df.drop("Class", axis=1)
y = df["Class"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Detailed report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Custom Prediction (Example)
def predict_transaction(data):
    prediction = model.predict([data])
    
    if prediction[0] == 1:
        print("❌ Fraud Transaction")
    else:
        print("✅ Legit Transaction")

# Example (random values, replace with real data)
sample = X.iloc[0].values
predict_transaction(sample)
