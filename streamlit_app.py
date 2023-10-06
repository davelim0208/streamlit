import streamlit as st
from googletrans import Translator

# Streamlit UI
st.title("English to Chinese Text Converter")

# Create a text input field for English text
english_text = st.text_input("Enter English text:")

# Create a button to perform the translation
if st.button("Translate to Chinese"):
    # Initialize the translator
    translator = Translator()

    # Translate the English text to Chinese
    chinese_text = translator.translate(english_text, src="en", dest="zh-CN")

    # Display the translated text
    st.write(f"Chinese translation: {chinese_text.text}")
