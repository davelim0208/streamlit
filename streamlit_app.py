import streamlit as st

# Streamlit UI
st.title("Prompt Generator App")

# Input fields for user details
name = st.text_input("Your Name:", "John Doe")
location = st.text_input("Your Location:", "New York")
age = st.number_input("Your Age:", min_value=0, max_value=150, value=30, step=1)

# Button to generate the prompt
if st.button("Generate Prompt"):
    # Create a prompt based on user details
    prompt = f"Name: {name}\nLocation: {location}\nAge: {age}"
    
    # Display the generated prompt
    st.write("Generated Prompt:")
    st.write(prompt)

