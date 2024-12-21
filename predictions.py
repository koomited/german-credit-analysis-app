import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
import joblib
import numpy as np

st.markdown(
    "<h2 style='text-align: center;'>Model Predictions</h2>", 
    unsafe_allow_html=True
)

## Import scalerstreamlit-app/app.py streamlit-app/bivariate.py streamlit-app/model.py streamlit-app/predictions.py streamlit-app/univariate.py
scaler = joblib.load('scaler.pkl')
# Import model
model = joblib.load("best_rf.pkl")
    
    
# entry form

with st.form("my_form"):
 
    Age = st.slider("Age", 0, 100)
    Credit_amount= st.number_input("Credit amount")
    ## Purpose
    purpose_options = {'business': 0,
                       'car': 1, 
                       'domestic appliances': 2, 
                       'education': 3, 
                       'furniture/equipment': 4,
                       'radio/TV': 5, 
                       'repairs': 6,
                       'vacation/others': 7}
    Purpose= st.selectbox('Credit Purpose', 
                          options=purpose_options.keys())
    Duration= st.number_input('Credit Duration (months)', min_value=0)
    
    submitted = st.form_submit_button("Submit")
    
if submitted:
    Purpose = purpose_options[Purpose]
    inputs = np.array([Age, Credit_amount, Duration]).reshape(1,-1)
    inputs = pd.DataFrame(inputs, columns=["Age", "Credit amount", "Duration"])
    scaled_data = scaler.transform(inputs)
    model_data = np.array([
    scaled_data[0, 1], 
    scaled_data[0, 0],  
    scaled_data[0, 2],  
    Purpose             
]   ).reshape(1, -1)
    prediction_prob = model.predict_proba(model_data)[:,1]
    
    
    with st.container():
        if prediction_prob[0] < 0.5:
            # Green Box for Approved
            st.success("## Eligible for Credit ✅")
            
            
        else:
            # Red Box for Rejected
            st.error("## Not Eligible for Credit ❌")
            
            
        

    