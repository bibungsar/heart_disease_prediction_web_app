# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:40:23 2024

@author: bibun
"""
import numpy as np
import pickle
import streamlit as st



heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


st.title('Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)
  
with col1: 
    age = st.text_input("Age of the Patient")

with col2:
    sex = st.text_input("Sex of the Patient")
    
with col3:  
    cp = st.text_input("Chest Pain Type")
    
with col1:
    trtbps = st.text_input("Resting Blood Pressure")

with col2:
    chol = st.text_input("Serum Cholestoral in mg/dl")

with col3:
    fbs = st.text_input("Fasting Blood Sugar in mg/dl")

with col1:
    restecg = st.text_input("Resting Electrocardiographic Results")

with col2:
    thalachh = st.text_input("Maximum Heart Rate Achieved")

with col3:
    exng = st.text_input("Exercise Induced Angina")

with col1:
    oldpeak = st.text_input("Oldpeak = ST depression induced by exercise relative to rest")

with col2:
    slp = st.text_input("the slope of the peak exercise ST segment")

with col3:
    caa = st.text_input("number of major vessels (0-3) colored by flourosopy")

with col1:
    thall = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")
    

# Convert input data to numeric values
input_data = np.array([float(age) if age else 0,    # Use 0 as default if age is empty
                       float(sex) if sex else 0,    # Use 0 as default if sex is empty
                       float(cp) if cp else 0,      # Use 0 as default if cp is empty
                       float(trtbps) if trtbps else 0,  # Use 0 as default if trtbps is empty
                       float(chol) if chol else 0,
                       float(fbs) if fbs else 0,
                       float(restecg) if restecg else 0,
                       float(thalachh) if thalachh else 0,
                       float(exng) if exng else 0,
                       float(oldpeak) if oldpeak else 0,
                       float(slp) if slp else 0,
                       float(caa) if caa else 0,
                       float(thall) if thall else 0])


heart_disease_diagnosis = ''

if st.button("Heart Disease Test Result"):
    heart_disease_prediction = heart_disease_model.predict(input_data.reshape(1, -1))
    
    
    if(heart_disease_prediction[0] == 1):
        heart_disease_diagnosis = 'The Person has heart disease'
    else:
        heart_disease_diagnosis = 'The Person doesnot have heart disease'
    
st.success(heart_disease_diagnosis)
    
    
    
    
    
    