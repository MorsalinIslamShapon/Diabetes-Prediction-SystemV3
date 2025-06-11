# Imports
from function.function import *
import streamlit as st
from loader import page_icon

st.set_page_config(
    page_title="Diabetes Prediction with AI",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="auto",  # Changes to auto for better mobile experience
    menu_items={
        'Get Help': 'https://github.com/Shankhadweep/Diabetes-Prediction-SystemV2',
        'Report a bug': 'https://github.com/Shankhadweep/Diabetes-Prediction-SystemV2/issues',
        'About': "# Diabetes Prediction App\nThis app predicts diabetes using machine learning."
    }
)

# Custom CSS for responsive design
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem 0.5rem;
        }
        .stButton>button {
            width: 100%;
        }
        .st-emotion-cache-16txtl3 {
            padding: 1rem 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)



# Container for better spacing and mobile responsiveness
with st.container():
    # Header
    from app.header import app
    app()

    # Inputs
    from app.input import app
    input_data = app()

    # Prediction
    from app.predict import app
    app(input_data)

    # Explain
    from app.explainer import app
    app(input_data)

    # Model performance
    from app.performance import app
    app()

    # perm_importance
    from app.perm_importance import app
    app()

    # About
    from app.about import app
    app()
