# script for deploying the churn model
import streamlit as st
import pickle
import numpy as np

# load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

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

# Convert inputs to model format
gender = 1 if gender == 'Male' else 0
seniorcitizen = 1 if seniorcitizen == 'Yes' else 0
partner = 1 if partner == 'Yes' else 0
dependents = 1 if dependents == 'Yes' else 0
phoneservice = 1 if phoneservice == 'Yes' else 0
multiplelines = 1 if multiplelines == 'Yes' else 0
internetservice = 1 if internetservice == 'Fiber optic' else 0
onlinesecurity = 1 if onlinesecurity == 'Yes' else 0
onlinebackup = 1 if onlinebackup == 'Yes' else 0
deviceprotection = 1 if deviceprotection == 'Yes' else 0
techsupport = 1 if techsupport == 'Yes' else 0
streamingtv = 1 if streamingtv == 'Yes' else 0
streamingmovies = 1 if streamingmovies == 'Yes' else 0
contract = 2 if contract == 'Two year' else 1 if contract == 'One year' else 0
paperlessbilling = 1 if paperlessbilling == 'Yes' else 0
paymentmethod = 3 if paymentmethod == 'Mailed check' else 2 if paymentmethod == 'Electronic check' else 1 if paymentmethod == 'Credit card (automatic)' else 0

# Create input array for the model
input_data = np.array([[gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, internetservice, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]])

