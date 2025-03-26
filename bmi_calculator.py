import streamlit as st
import pandas as pd

def feet_inches_to_cm(feet, inches):
    return (feet * 30.48) + (inches * 2.54)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100 
    if height_m <= 0:
        return None
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "\U0001F535"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "\U0001F7E2"
    elif 25 <= bmi < 29.9:
        return "Overweight", "\U0001F7E0"
    else: 
        return "Obese", "\U0001F534"

# Streamlit UI
st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%2f")

height_format = st.radio("Select Height Input Format:", ("Centimeters (cm)", "Feet & Inches"))

if height_format == "Centimeters (cm)":
    height_cm = st.number_input("Enter your height (cm):", min_value=1.0, format="%.2f")
else:
    feet = st.number_input("Feet:", min_value=0, step=1)
    inches = st.number_input("Inches:", min_value=0, max_value=11, step=1)
    height_cm = feet_inches_to_cm(feet, inches)

if st.button("Calculate BMI"):
    if weight > 0 and height_cm > 0:
        bmi = calculate_bmi(weight, height_cm)
        category, emoji = bmi_category(bmi)

        st.subheader(f"Your BMI: {bmi} {emoji}")
        st.write(f"**Category:** {category}")

        data = {
            "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30+"],
            "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
            "Indicator": ["\U0001F535", "\U0001F7E2", "\U0001F7E0", "\U0001F534"]
        }
        df = pd.DataFrame(data)
        st.table(df)

    else:
        st.error("Please enter valid weight and height.")
