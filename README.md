# UPI-Fraud-Detection-System.
Machine Learning project to detect fraudulent financial transactions using Logistic Regression.
# 💳 Fraud Detection System

A Machine Learning project that detects whether a financial transaction is **fraudulent or legitimate** using classification algorithms.

---

## 📌 Overview

With the rapid growth of digital payments and UPI transactions, fraud detection has become a critical challenge.
This project aims to identify **fraudulent transactions** using machine learning techniques and help improve financial security.

---

## 🚀 Features

* 🔍 Classifies transactions as **Fraud** or **Legit**
* ⚡ Uses Logistic Regression for prediction
* 📊 Generates accuracy and classification report
* 🧪 Supports custom transaction testing

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* NumPy

---

## 📂 Dataset

* Source: Credit Card Fraud Detection Dataset (Kaggle)
* Contains real transaction data
* Target column:

  * `Class = 0` → Legit Transaction
  * `Class = 1` → Fraud Transaction

---

## ⚙️ How It Works

1. Data Loading and Preprocessing
2. Splitting dataset into training and testing
3. Model Training using Logistic Regression
4. Prediction and Evaluation
5. Fraud detection on new transactions

---

## ▶️ How to Run

1. Install dependencies:

   ```
   pip install pandas numpy scikit-learn
   ```
2. Place dataset (`creditcard.csv`) in project folder
3. Run the script:

   ```
   python model.py
   ```

---

## 📊 Model Performance

* Accuracy: ~99%
* Note: Dataset is highly imbalanced, so fraud detection requires further improvement.

---

## ⚠️ Limitations

* Dataset imbalance affects fraud detection accuracy
* Some fraud cases may not be detected

---

## 📈 Future Improvements

* Use Random Forest / XGBoost
* Apply SMOTE for data balancing
* Build a real-time fraud detection system
* Create a web interface (Streamlit)

---

## 🧪 Example

**Input:** Transaction data

**Output:**
❌ Fraud Transaction
or
✅ Legit Transaction

---

## 👨‍💻 Author

PRADEEP RATURI.

---

## ⭐ Contribution

Feel free to fork this repository and improve the project.

---

## 📜 License

This project is for educational purposes only.

