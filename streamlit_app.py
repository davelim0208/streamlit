import streamlit as st
import openai

# Set your Azure OpenAI API key
api_key = '250783a2a3ed4cbe93dd0d7d2c443144'

# Initialize the Azure OpenAI client
openai.api_key = api_key

# Streamlit UI
st.title("Azure OpenAI Prompt Generator")

# Create a text input field for the prompt
prompt = st.text_area("Enter a prompt:", "Translate the following English text to French: 'Hello, world.'")

# Create a button to generate a response
if st.button("Generate Response"):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.7  # Adjust for randomness
        )

        # Display the generated response
        st.write("Generated Response:")
        st.write(response.choices[0].text.strip())

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

