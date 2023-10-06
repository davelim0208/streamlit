import streamlit as st

# Streamlit UI
st.title("Simple Streamlit App")

# Text input
user_name = st.text_input("Enter your name:", "John Doe")

# Button to greet the user
if st.button("Greet"):
    st.write(f"Hello, {user_name}!")

# Add more content to your app as needed
streamlit run simple_streamlit_app.py

