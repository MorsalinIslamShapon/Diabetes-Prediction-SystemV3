import streamlit as st
import pandas as pd


def app():
    st.sidebar.header("Input Parameters")

    # Pregnancies
    pregnancies_value = st.sidebar.number_input(
        'Enter value for `Pregnancies`',
        min_value=0,
        max_value=20,
        value=1
    )

    # Glucose
    glucose_value = st.sidebar.number_input(
        'Enter value for `Glucose`',
        min_value=0,
        max_value=250,
        value=100
    )

     # BloodPressure
    bloodpressure_value = st.sidebar.number_input(
        'Enter value for `Blood Pressure`',
        min_value=0,
        max_value=200,
        value=1
    )
    # SkinThickness
    skinthickness_value = st.sidebar.number_input(
        'Enter value for `Skin Thickness`',
        min_value=0,
        max_value=100,
        value=1
    )

    # Insulin
    insulin_value = st.sidebar.number_input(
        'Enter value for `Insulin`',
        min_value=0,
        max_value=1000,
        value=100
    )

    # BMI
    bmi_value = st.sidebar.number_input(
        'Enter value for `BMI`',
        min_value=0.0,
        max_value=100.0,
        value=37.0,
        format="%.1f"
    )
    # DiabetesPedigreeFunction
    diabetespedigreefunction_value = st.sidebar.number_input(
        'Enter value for `Diabetes Pedigree Function`',
        min_value=0.08,
        max_value=2.42,
        value=0.09,
        format="%.1f"
    )

    # Age
    age_value = st.sidebar.number_input(
        'Enter value for `Age`',
        min_value=0,
        max_value=100,
        value=25
    )

    st.sidebar.markdown('---')
    return pd.DataFrame([[pregnancies_value, glucose_value,bloodpressure_value,skinthickness_value,insulin_value,bmi_value,diabetespedigreefunction_value, age_value]], 
                        columns=['Pregnancies', 'Glucose','Blood Pressure','Skin Thickness','Insulin','BMI','Diabetes Pedigree Function','Age'])    