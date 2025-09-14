# PREDICTIVE-ANALYSIS-USING-MACHINE-LEARNING

# **Bank Customer Churn Prediction**

## **Project Overview**
This project predicts whether a bank customer will **churn (leave the bank)** or **stay**, using machine learning. The dataset contains customer details, and a model is trained to generate predictions.

## **Dataset**
- The dataset used is **Bank_Churn.csv**.
- It includes customer information such as age, credit score, balance, and number of products used.
- The target variable is **Exited** (1 = Churn, 0 = Stay).

## **Steps Performed**

### **1. Data Loading and Exploration**
- Checked for missing values and data types.
- Identified key features and the target variable (**Exited**).

### **2. Data Preprocessing**
- **Dropped irrelevant columns:** "CustomerId" and "Surname".
- **Encoded categorical features:** "Geography" and "Gender" converted into numerical values.
- **Scaled numerical features** using StandardScaler.
- **Split dataset:** 80% training, 20% testing.

### **3. Model Training**
- Used a **Random Forest Classifier**.
- Trained on the preprocessed dataset.

### **4. Model Evaluation**
- Achieved an **accuracy of 86.4%**.
- Analyzed precision and recall:
  - **Class 0 (Stay):** High precision & recall.
  - **Class 1 (Churn):** Lower recall (misses some churn cases).

### **5. Generating Predictions**
- Added **"Predicted_Exited"** column:
  - `0` → Customer will **stay**.
  - `1` → Customer will **churn**.
- Saved results as **Bank_Churn_Predictions.csv**.

### **6. Restoring CustomerId for Lookup**
- Created **Bank_Churn_Predictions_Updated.csv** with **CustomerId** restored.

### **7. Customer Lookup Function**
- Function to check if a customer will churn by **CustomerId**:
```python
import pandas as pd

def check_customer_churn(customer_id):
    df = pd.read_csv("Bank_Churn_Predictions_Updated.csv")
    customer_data = df[df["CustomerId"] == customer_id]
    if customer_data.empty:
        return f"Customer ID {customer_id} not found."
    prediction = customer_data["Predicted_Exited"].values[0]
    return f"Customer ID {customer_id}: {'Will Churn' if prediction == 1 else 'Will Stay'}
    return f"Customer ID {customer_id}: {result}"

# Get customer ID from user input
customer_id = int(input("Enter Customer ID: "))

# Check churn prediction for the entered ID
print(check_customer_churn(customer_id))"
```

## **Results**
- **8133 customers** predicted to **stay**.
- **1867 customers** predicted to **churn**.

## **Generated Files**
1. 📂 **Bank_Churn_Predictions.csv** → Original data + churn predictions.
2. 📂 **Bank_Churn_Predictions_Updated.csv** → Includes **CustomerId** for lookup.

## **Next Steps**
- Improve model recall for churn cases (e.g., using Gradient Boosting).
- Create new features (e.g., customer engagement metrics).
- Deploy model as an API for real-time predictions.

## **Conclusion**

This project successfully predicts customer churn with an accuracy of 86.4%, providing valuable insights into customer behavior. While the model performs well, improving recall for churn cases will help capture more at-risk customers. Future improvements, such as advanced machine learning techniques and additional customer engagement features, can enhance accuracy and provide even better predictions. Implementing this model in a real-world banking environment can help banks take proactive measures to retain customers and reduce churn.
