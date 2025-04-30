import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Page title
st.title("💪 BMI Calculator")

# User inputs
st.subheader("Enter your details:")
weight = st.number_input("Weight (in kilograms)", min_value=1.0, step=0.5)
height = st.number_input("Height (in meters)", min_value=0.1, step=0.01)

# Button to calculate
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.success(f"Your BMI is: {bmi:.2f}")

    # Interpretation
    st.subheader("Interpretation:")
    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
