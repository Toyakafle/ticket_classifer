import streamlit as st
from predict import predict_category

st.title('Ticket Category Predictor')

user_input = st.text_input('Enter your support ticket description:')

if st.button('Predict Category'):
    if user_input:
        predicted_category = predict_category(user_input)
        st.success(f'Predicted Category: {predicted_category}')
    else:
        st.warning('Please enter some text to predict the category.')
