import pickle
import numpy as np
import pandas as pd
import streamlit as st

# Add custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .stNumberInput input {
        border-radius: 10px;
        padding: 10px;
    }
    .prediction {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .non-smoker {
        color: green;
    }
    .smoker {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Smoking Binary Prediction')

# Input fields
age = st.number_input('Enter Age', min_value=0, max_value=100, value=0)
height = st.number_input('Enter Height(cm)', min_value=0, max_value=300, value=0)
weight = st.number_input('Enter Weight(kg)', min_value=0, max_value=300, value=0)
waist = st.number_input('Enter Waist(cm)', min_value=0, max_value=300, value=0)
eyesight_left = st.number_input('Enter Eyesight(left)', min_value=0, max_value=10, value=0)
eyesight_right = st.number_input('Enter Eyesight(right)', min_value=0, max_value=10, value=0)
hearing_left = st.number_input('Enter Hearing(left)', min_value=0, max_value=100, value=0)
hearing_right = st.number_input('Enter Hearing(right)', min_value=0, max_value=100, value=0)
systolic = st.number_input('Enter Systolic', min_value=0, max_value=300, value=0)
relaxation = st.number_input('Enter Relaxation', min_value=0, max_value=300, value=0)
fasting_blood_sugar = st.number_input('Enter Fasting Blood Sugar', min_value=0, max_value=300, value=0)
Cholesterol = st.number_input('Enter Cholesterol', min_value=0, max_value=300, value=0)
triglyceride = st.number_input('Enter Triglyceride', min_value=0, max_value=300, value=0)
HDL = st.number_input('Enter HDL', min_value=0, max_value=300, value=0)
LDL = st.number_input('Enter LDL', min_value=0, max_value=300, value=0)
hemoglobin = st.number_input('Enter Hemoglobin', min_value=0, max_value=300, value=0)
Urine_protein = st.number_input('Enter Urine Protein', min_value=0, max_value=300, value=0)
serum_creatinine = st.number_input('Enter Serum Creatinine', min_value=0, max_value=300, value=0)
AST = st.number_input('Enter AST', min_value=0, max_value=300, value=0)
ALT = st.number_input('Enter ALT', min_value=0, max_value=300, value=0)
Gtp = st.number_input('Enter Gtp', min_value=0, max_value=300, value=0)
dental_caries = st.number_input('Enter Dental Caries', min_value=0, max_value=300, value=0)

# Load the model from disk
model = pickle.load(open('model.pkl', 'rb'))

if st.button('Predict'):
    input_data = np.array([[age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation, fasting_blood_sugar, Cholesterol, triglyceride, HDL, LDL, hemoglobin, Urine_protein, serum_creatinine, AST, ALT, Gtp, dental_caries]])
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.markdown('<div class="prediction non-smoker">The person is a non-smoker</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="prediction smoker">The person is a smoker</div>', unsafe_allow_html=True)
