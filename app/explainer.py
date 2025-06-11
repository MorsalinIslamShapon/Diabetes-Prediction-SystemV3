import streamlit as st
import shap
import time
from loader import model
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def create_gauge_chart(value, title, min_val, max_val, normal_range):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title},
        gauge = {
            'axis': {'range': [min_val, max_val]},
            'bar': {'color': "#ff4b4b"},
            'steps': [
                {'range': normal_range, 'color': "lightgreen"}
            ]
        }
    ))

    return fig
def app(input_data):
    sample_transformed = model.named_steps['feature_engineering'].transform(input_data)
    explainer = shap.TreeExplainer(model.named_steps['model'])
    shap_values_single = explainer.shap_values(sample_transformed)

    shap_values_class_1 = shap_values_single[0][:, 1]  
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)

    # Get values from input_data
    glucose = float(input_data.iloc[0]['Glucose'])
    bmi = float(input_data.iloc[0]['BMI'])
    blood_pressure = float(input_data.iloc[0]['Blood Pressure'])

    with col1:
        fig1 = create_gauge_chart(glucose, "Glucose", 0, 200, [70, 140])
        st.plotly_chart(fig1)

    with col2:
        fig2 = create_gauge_chart(bmi, "BMI", 0, 50, [18.5, 24.9])
        st.plotly_chart(fig2)

    with col3:
        fig3 = create_gauge_chart(blood_pressure, "Blood Pressure", 0, 122, [60, 80])
        st.plotly_chart(fig3)

    def stream_data():
        text = f"""
Your inputs:\n
`Pregnancies`: {int(input_data.iloc[0]['Pregnancies'])}\n
`Glucose`: {float(input_data.iloc[0]['Glucose'])}\n
`Blood\tPressure`: {float(input_data.iloc[0]['Blood Pressure'])}\n
`Skin\tThickness`: {float(input_data.iloc[0]['Skin Thickness'])}\n
`Insulin`: {float(input_data.iloc[0]['Insulin'])}\n
`BMI`: {float(input_data.iloc[0]['BMI'])}\n
`Diabetes\tPedigree\tFunction`: {float(input_data.iloc[0]['Diabetes Pedigree Function'])}\n
`Age`: {float(input_data.iloc[0]['Age'])}
                """
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)

    # Layout with two columns
    cols = st.columns(2)

    # Column 1: Stream user input
    with cols[0]:
        st.markdown("### Input Streaming")
        st.markdown("#### See your inputs in real-time below!")
     
            # Create columns for each input field
    input_cols = st.columns(8)
    
    with input_cols[0]:
        st.markdown("### Pregnancies")
        st.write(int(input_data.iloc[0]['Pregnancies']))
    
    with input_cols[1]:
        st.markdown("### Glucose")
        st.write(float(input_data.iloc[0]['Glucose']))
        
    with input_cols[2]:
        st.markdown("### Blood Pressure")
        st.write(float(input_data.iloc[0]['Blood Pressure']))
        
    with input_cols[3]:
        st.markdown("### Skin Thickness")
        st.write(float(input_data.iloc[0]['Skin Thickness']))
        
    with input_cols[4]:
        st.markdown("### Insulin")
        st.write(float(input_data.iloc[0]['Insulin']))
        
    with input_cols[5]:
        st.markdown("### BMI")
        st.write(float(input_data.iloc[0]['BMI']))
        
    with input_cols[6]:
        st.markdown("### DPF")
        st.write(float(input_data.iloc[0]['Diabetes Pedigree Function']))
        
    with input_cols[7]:
        st.markdown("### Age")
        st.write(float(input_data.iloc[0]['Age']))

   

    # SHAP Force Plot
    force_plot_html = shap.force_plot(
        base_value=explainer.expected_value[1],
        shap_values=shap_values_single[0][:, 1],
        features=sample_transformed.iloc[0],
        feature_names=sample_transformed.columns.tolist()
    )

    # Explanation column
    st.markdown(
        """
        ### Column Explanations
        - 🟡 **Input Streaming**: Displays user inputs dynamically in real-time.
        - 🟡 **SHAP Waterfall Plot**: Visualizes how each feature contributes to the model prediction.
        - 🟡 **SHAP Force Plot**: Interactive plot showing positive/negative feature contributions.
        \n\n\n\n""",
        unsafe_allow_html=True,
    )

    # Add SHAP JS visualization
    force_plot_html = f"<head>{shap.getjs()}</head><body>{force_plot_html.html()}</body>"
    st.markdown("### SHAP Waterfall Plot")
    st.components.v1.html(force_plot_html, height=400)

    