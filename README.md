# **CHURN DATASET**

## **INTRODUCTION**

The dataset contains information about seven thousand forty-three(7,043) customers and twenty-one(21) features describing themselves and the service the telecom company provided them.

The dataset in this notebook includes information about
- Customers who left the last month - the column is called Churn.
- Services that each customer has signed up for - phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.
- Customer account information - how long they've been a customer, contract, payment method, paperless billing, monthly charges, and total charges.
- Demographic info about customers - gender and if they have partners and dependents.

___

## **DATA DICTIONARY/INFORMATION ON EACH COLUMN**

- Gender - whether the customer is a male or a female.
- SeniorCitizen - whether the customer is a senior citizen or not.
- Partner - whether the customer has a partner or not.
- Dependents - whether the customer has dependents or not.
- tenure - number of months the customer has stayed with the company
- PhoneService - whether the customer has a phone service or not.
- MultipleLines - whether the customer has multiple lines or not.
- InternetService - customer's internet service provider(DSL, Fiber optic, No).
- OnlineSecurity - whether the customer has online security or not (Yes, No, No internet service).
- OnlineBackup - whether the customer has online backup or not (Yes, No, No Internet service).
- DeviceProtection - whether the customer has device protection or not (Yes, No, No Internet Service).
- TechSupport - whether the customer has tech support or not (Yes, No, No internet service).
- StreamingTV - whether the customer has streaming TV or not (Yes, No, No internet service).
- StreamingMovies - whether the customer has streaming movies or not (Yes, No, No Internet Service).
- Contract - The contract term of the customer (Month-to-month, One year, Two years).
- PaperlessBilling - whether the customer has paperless billing or not (Yes, No).
- PaymentMethod - the customer's payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
- MonthlyCharges - the amount charged to the customer monthly.
- TotalCharges - the total amount charged to the customer.
- Churn - whether the customer churned or not (Yes, No).

This repo contains my solution to the `Churn` data project, the repo contains dataset for the project, and also my solution notebook. In the notebook, I wrangled my data, did data cleaning, showed some visualization, and also built a model to predict whether the customer 'Churn' or not.

The algorithm used to build my model is the LogisticRegression algorithm. With this algorithm, I was able to achieve the following metrics:
- Accuracy: 77%
- Precision: 89%
- Recall: 79%
- F1_score: 84%


This ends my model building on this project maybe for now, I move to learning how to deploy my models.