# script for deploying the churn model
import streamlit as st
import numpy as np

# set page title
st.title('Churn Prediction Model')

# collect user input
gender = st.radio("Select gender:", ('Female', 'Male'))
seniorcitizen = st.radio("Is the customer a senior citizen?", ('Yes', 'No'))
partner = st.radio("Is the customer married?", ('Yes', 'No'))
dependents = st.radio("Does the customer have dependents?", ('Yes', 'No'))
tenure = st.number_input("Number of months you've been using the service", min_value=0, max_value=100, value=0)
phoneservice = st.radio("Does the customer have a phone service?", ('Yes', 'No'))
multiplelines = st.radio("Does the customer have multiple lines?", ('Yes', 'No'))
internetservice = st.radio("Type of internet service", ('DSL', 'Fiber optic', 'No'))
onlinesecurity = st.radio("Does the customer have online security?", ('Yes', 'No'))
onlinebackup = st.radio("Does the customer have online backup?", ('Yes', 'No'))
deviceprotection = st.radio("Does the customer have device protection?", ('Yes', 'No'))
techsupport = st.radio("Does the customer have tech support?", ('Yes', 'No'))
streamingtv = st.radio("Does the customer have streaming TV?", ('Yes', 'No'))
streamingmovies = st.radio("Does the customer have streaming movies?", ('Yes', 'No'))
contract = st.radio("Type of contract", ('Month-to-month', 'One year', 'Two year'))
paperlessbilling = st.radio("Does the customer have paperless billing?", ('Yes', 'No'))
paymentmethod = st.radio("Payment method", ('Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'))
monthlycharges = st.number_input("Monthly charges", min_value=0, max_value=200, value=0)
totalcharges = st.number_input("Total charges", min_value=0, max_value=10000, value=0)

