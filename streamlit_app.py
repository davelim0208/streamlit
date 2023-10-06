import streamlit as st

# Streamlit UI
st.title("Button Display App")

# Create four buttons
if st.button("Button 1"):
    st.write("You clicked Button 1!")

if st.button("Button 2"):
    st.write("You clicked Button 2!")

if st.button("Button 3"):
    st.write("You clicked Button 3!")

if st.button("Button 4"):
    st.write("You clicked Button 4!")
