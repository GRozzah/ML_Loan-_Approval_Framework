import streamlit as st
import numpy as np
import joblib
import os
import plotly.express as px
import pandas as pd

# Import the styling
import style  # Import the customization from the style.py file

# --- Apply the custom style ---
style.set_background()  # This will apply the custom  theme

# --- Load resources ---
model_folder = 'model_files'  # The folder where models, encoders, and scaler are saved

# Load the models from the 'model_files' folder
xgboost_model = joblib.load(os.path.join(model_folder, 'xgboost_model.pkl'))
random_forest_model = joblib.load(os.path.join(model_folder, 'random_forest_model.pkl'))
logistic_regression_model = joblib.load(os.path.join(model_folder, 'logistic_regression_model.pkl'))

# Load the label encoders (this is a dictionary of encoders)
label_encoders = joblib.load(os.path.join(model_folder, 'label_encoders.pkl'))

# Load the scaler
scaler = joblib.load(os.path.join(model_folder, 'scaler.pkl'))

# --- Sidebar Visualizations ---
st.sidebar.header("Model Feature Importance")
   

# --- Feature Importance Visualization ---
if st.sidebar.checkbox("Show Feature Importance"):
    model_name = st.sidebar.selectbox("Select a Machine Learning Model to view features:", ["Logistic Regression", "Random Forest", "XGBoost"], key="model_selectbox")

    if model_name in ["Random Forest", "XGBoost"]:
        # For RandomForest and XGBoost, we extract feature importance
        if model_name == "Random Forest":
            feature_importance = random_forest_model.feature_importances_
            feature_names = random_forest_model.feature_names_in_
        elif model_name == "XGBoost":
            feature_importance = xgboost_model.feature_importances_
            feature_names = xgboost_model.feature_names_in_

        # Create a DataFrame for feature importance
        feature_importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': feature_importance
        }).sort_values(by='Importance', ascending=False)

        # Create a bar chart for feature importance
        fig = px.bar(feature_importance_df, x='Feature', y='Importance', title=f"{model_name} Feature Importance")
        st.sidebar.plotly_chart(fig)

    elif model_name == "Logistic Regression":
        # For Logistic Regression, use coefficients as feature importance
        feature_importance = np.abs(logistic_regression_model.coef_[0])
        feature_names = logistic_regression_model.feature_names_in_

        # Create a DataFrame for feature importance
        feature_importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': feature_importance
        }).sort_values(by='Importance', ascending=False)

        # Create a bar chart for feature importance
        fig = px.bar(feature_importance_df, x='Feature', y='Importance', title=f"{model_name} Feature Importance")
        st.sidebar.plotly_chart(fig)

# --- Header ---

st.markdown("<h1 style='text-align: center;'>🔍 ML-Powered Loan Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Assess the risk level of loan applicants with confidence.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Model selection ---
model_name = st.selectbox("🧠 Choose a Machine Learning Model:", ["Logistic Regression", "Random Forest", "XGBoost"], key="model_selection")

if model_name == "Logistic Regression":
    model = logistic_regression_model
elif model_name == "Random Forest":
    model = random_forest_model
else:
    model = xgboost_model

# --- Input section ---
st.markdown("### 📝 Applicant Details")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input("💰 Income", min_value=0, key="income")
    age = st.number_input("🎂 Age", min_value=18, max_value=100, key="age")
    experience = st.number_input("📊 Experience (Years)", min_value=0, key="experience")
    marital_status = st.selectbox("💍 Marital Status", label_encoders['Married/Single'].classes_, key="marital_status")

with col2:
    job_years = st.number_input("💼 Years in Current Job", min_value=0, key="job_years")
    house_years = st.number_input("🏠 Years at Current Residence", min_value=0, key="house_years")
    house_own = st.selectbox("🏘️ House Ownership", label_encoders['House_Ownership'].classes_, key="house_own")
    car_own = st.selectbox("🚗 Car Ownership", label_encoders['Car_Ownership'].classes_, key="car_own")
    profession = st.selectbox("👨‍🔧 Profession", label_encoders['Profession'].classes_, key="profession")

# --- Preprocess input ---
encoded_marital = label_encoders['Married/Single'].transform([marital_status])[0]
encoded_house = label_encoders['House_Ownership'].transform([house_own])[0]
encoded_car = label_encoders['Car_Ownership'].transform([car_own])[0]
encoded_prof = label_encoders['Profession'].transform([profession])[0]

# Make sure to include all required features in the input
# Ensure the correct feature order as per training data
input_data = np.array([[income, age, experience, job_years, house_years]])

# Apply scaling to numeric features
scaled_numeric = scaler.transform(input_data)

# Concatenate the scaled features with the encoded categorical features
input_vector = np.concatenate(
    [scaled_numeric[0], [encoded_marital, encoded_house, encoded_car, encoded_prof]]
).reshape(1, -1)

# --- Predict ---
if st.button("🔎 Predict Risk"):
    prediction = model.predict(input_vector)
    st.markdown("---")
    st.markdown("### 🧾 Prediction Result:")

    if prediction[0] == 0:
        st.success("✅ This applicant is predicted to be **Safe**.")
        st.balloons()
    else:
        st.error("❌ This applicant is predicted to be **Risky**.")
        st.markdown("🔔 **Please proceed with caution.**")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Running prediction</p>", unsafe_allow_html=True)
