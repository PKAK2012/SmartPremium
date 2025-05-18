

#streamlit run SmartPermium/SmartPerm.py --theme.base "light" --theme.backgroundColor "#E6E6FA" --theme.textColor "#4B0082" --theme.secondaryBackgroundColor "#D8BFD8"


import streamlit as st
import numpy as np
import pickle

# Load the model
with open(r"C:\Users\engga\OneDrive\Documents\Porkodi_guvi\Guvi_project\Streamlit\SmartPermium\SPM.pkl", "rb") as file:
    brain = pickle.load(file)

st.title("Insurance Premium Prediction App")

def show_range_info(field_name, min_val, max_val):
    st.info(f"{field_name} Range: {min_val} - {max_val}")

def extract_numeric(option_str):
    return int(option_str.split('(')[-1].replace(')', '').strip())

# Inputs
with st.expander("Personal Details"):
    age = st.text_input("Enter Age", placeholder="Between 18 and 64")
    gender = extract_numeric(st.radio("Select Gender", ["Female (0)", "Male (1)"]))
    marital_status = extract_numeric(st.radio("Marital Status", ["Married (1)", "Divorced (0)", "Single (2)"]))
    dependents = int(st.selectbox("Number of Dependents", [0, 1, 2, 3, 4]))

with st.expander("Education & Occupation"):
    education = extract_numeric(st.selectbox("Education Level", ["Bachelor's (0)", "High School (1)", "Master's (2)", "PhD (3)"]))
    occupation = extract_numeric(st.radio("Occupation", ["Employed (1)", "Self-Employed (0)", "Unemployed (2)"]))

with st.expander("Financial Information"):
    annual_income = st.text_input("Annual Income", placeholder="e.g., 10000 to 150000")
    #show_range_info("Annual Income", 10000, 150000)
    
    credit_score = st.text_input("Credit Score", placeholder="Between 300 and 850")
    #show_range_info("Credit Score", 300, 850)

with st.expander("Insurance Details"):
    health_score = st.text_input("Health Score", placeholder="Between 2 and 58")
    #show_range_info("Health Score", 2, 58)

    location = extract_numeric(st.selectbox("Location", ["Rural (0)", "Suburban (1)", "Urban (2)"]))
    policy_type = extract_numeric(st.selectbox("Policy Type", ["Basic (0)", "Comprehensive (1)", "Premium (2)"]))

    previous_claims = int(st.selectbox("Number of Previous Claims", list(range(0, 10))))
    vehicle_age = int(st.selectbox("Vehicle Age", list(range(0, 20))))

with st.expander("Lifestyle Details"):
    customer_feedback = extract_numeric(st.radio("Customer Feedback", ["Poor (0)", "Average (1)", "Good (2)"]))
    smoking_status = extract_numeric(st.radio("Smoking Status", ["No (0)", "Yes (1)"]))
    exercise_frequency = extract_numeric(st.selectbox("Exercise Frequency", ["Daily (0)", "Weekly (1)", "Monthly (2)", "Rarely (3)"]))
    property_type = extract_numeric(st.selectbox("Property Type", ["Apartment (0)", "Condo (1)", "House (2)"]))

insurance_duration = int(st.selectbox("Insurance Duration (Years)", [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Prediction
if st.button("Predict Premium"):
    try:
        input_data = np.array([[int(age), gender, float(annual_income), marital_status, dependents,
                                education, occupation, float(health_score), location, policy_type,
                                previous_claims, vehicle_age, float(credit_score), insurance_duration,
                                customer_feedback, smoking_status, exercise_frequency, property_type]])
        
        prediction = brain.predict(input_data)
        st.success(f"Predicted Premium: ₹{prediction[0]:,.2f} 💰📈")
    except ValueError:
            st.error("Please enter valid numeric values for Age, Annual Income, Credit Score, and Health Score.")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
