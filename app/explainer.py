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

        # Column 1: Input Metrics
    st.markdown("### Input Parameters with Normal Ranges")
    
    # Create two rows of 4 columns each for better layout
    row1_cols = st.columns(4)
    row2_cols = st.columns(4)
    
    # First row of metrics
    with row1_cols[0]:
        fig1 = create_gauge_chart(int(input_data.iloc[0]['Pregnancies']), "Pregnancies", 0, 15, [0, 8])
        st.plotly_chart(fig1, use_container_width=True)
    
    with row1_cols[1]:
        fig2 = create_gauge_chart(float(input_data.iloc[0]['Glucose']), "Glucose", 0, 200, [70, 140])
        st.plotly_chart(fig2, use_container_width=True)
    
    with row1_cols[2]:
        fig3 = create_gauge_chart(float(input_data.iloc[0]['Blood Pressure']), "Blood Pressure", 0, 122, [60, 80])
        st.plotly_chart(fig3, use_container_width=True)
    
    with row1_cols[3]:
        fig4 = create_gauge_chart(float(input_data.iloc[0]['Skin Thickness']), "Skin Thickness", 0, 100, [10, 50])
        st.plotly_chart(fig4, use_container_width=True)
    
    # Second row of metrics
    with row2_cols[0]:
        fig5 = create_gauge_chart(float(input_data.iloc[0]['Insulin']), "Insulin", 0, 850, [16, 166])
        st.plotly_chart(fig5, use_container_width=True)
    
    with row2_cols[1]:
        fig6 = create_gauge_chart(float(input_data.iloc[0]['BMI']), "BMI", 0, 50, [18.5, 24.9])
        st.plotly_chart(fig6, use_container_width=True)
    
    with row2_cols[2]:
        fig7 = create_gauge_chart(float(input_data.iloc[0]['Diabetes Pedigree Function']), "DPF", 0, 2.5, [0.078, 2.42])
        st.plotly_chart(fig7, use_container_width=True)
    
    with row2_cols[3]:
        fig8 = create_gauge_chart(float(input_data.iloc[0]['Age']), "Age", 0, 100, [20, 80])
        st.plotly_chart(fig8, use_container_width=True)


   

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
    

    