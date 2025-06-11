import time
import streamlit as st
from loader import model, accuracy_result
from data.config import thresholds
from function.function import make_donut
from data.base import mrk

# Add custom CSS for mobile responsiveness
st.markdown("""
<style>
@media (max-width: 768px) {
    .prediction-container {
        text-align: center !important;
        margin: auto !important;
    }
    .stMarkdown, .stText {
        text-align: center !important;
    }
    [data-testid="column"] {
        width: 100% !important;
        margin: auto !important;
        padding: 1rem !important;
    }
    .status-text {
        text-align: center !important;
        display: block !important;
        width: 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)

def app(input_data):
    prediction = model.predict_proba(input_data)[:, 1]

    # Use a single column on mobile
    if st.session_state.get('is_mobile', False):
        cols = st.columns(1)
    else:
        cols = st.columns(2)

    def stream_data():
        is_diabetes = f'Diabetes' if prediction >= thresholds else 'No Diabetes'
        text = f"Model Accuracy: {accuracy_result}%\n\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        text = f"\nPrediction: {is_diabetes}\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        text = f"\nProbability: {(prediction * 100).round(2)[0]}%\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        
        return 80

    # Add container class for styling
    with st.container():
        st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
        cols[0].write_stream(stream_data)
        st.markdown('</div>', unsafe_allow_html=True)

    # Wrap the status text in a div with the status-text class
    is_diabetes = f'<div class="status-text"><strong>Warning:</strong> Diabetes!</div>' if prediction >= thresholds else '<div class="status-text">No Diabetes</div>'
    color = f'red' if prediction >= thresholds else 'blue'

    # Add container class for styling
    with st.container():
        st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
        cols[1].markdown(mrk.format(color, is_diabetes), unsafe_allow_html=True)
        cols[1].write('\n\n\n\n\n')
        donut_chart_population = make_donut((prediction * 100).round(2)[0], 
                                          'Diabetes Risk',
                                          input_color=color)
        cols[1].altair_chart(donut_chart_population)
        st.markdown('</div>', unsafe_allow_html=True)