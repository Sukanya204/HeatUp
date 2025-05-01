import numpy as np
import pandas as pd
import streamlit as st
import pickle

calories = pickle.load(open('model.pkl', 'rb'))

def predict_calorie_loss(gender_value, age, height, heart_rate, body_temp):
    prediction = calories.predict([[gender_value, age, height, heart_rate, body_temp]])
    return prediction[0]  

def main():
    st.title('Calorie Burn Prediction')
    
    gender = st.radio("Select Gender:", ("Male", "Female"), index=None)
    age = st.number_input("Age", min_value=1, max_value=100, step=1, value=None)
    height = st.number_input("Height (in cm)", min_value=50.0, max_value=250.0, step=0.1, value=None)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, step=1, value=None)
    body_temp = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1, value=None)

    if st.button("Predict"):
        if None in (gender, age, height, heart_rate, body_temp):
            st.error("❌ Please fill in all fields before predicting!")
        else:
            gender_value = 1 if gender == "Female" else 0
            try:
                result = predict_calorie_loss(gender_value, age, height, heart_rate, body_temp)
                if result is not None:
                    st.success(f"🔥 Calories burnt: **{result:.2f} kcal**")  # Format to 2 decimal places
                else:
                    st.error("⚠️ Prediction failed. Please check inputs.")
            except Exception as e:
                st.error(f"🚨 Error in prediction: {str(e)}")


if __name__ == '__main__':
    main()