import streamlit as st
import openai

# Set your Azure OpenAI API key
api_key = '250783a2a3ed4cbe93dd0d7d2c443144'

# Initialize the Azure OpenAI client
openai.api_key = api_key

# Streamlit UI
st.title("ChatGPT Simulation")

# Create a conversation history to store user and AI messages
conversation_history = []

# Function to send a message to ChatGPT and update the conversation history
def send_message(message):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": message})

    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        messages=conversation_history
    )

    # Add ChatGPT's response to the conversation history
    conversation_history.append({"role": "assistant", "content": response.choices[0].message["content"]})

    return response.choices[0].message["content"]

# Chat input field
user_input = st.text_input("You:", "")

# Send button
if st.button("Send"):
    if user_input.strip() != "":
        user_message = user_input
        st.text(f"You: {user_message}")
        
        # Send the user's message to ChatGPT
        assistant_message = send_message(user_message)
        
        st.text(f"ChatGPT: {assistant_message}")
        st.text("")

# Clear button to reset the conversation
if st.button("Clear Conversation"):
    conversation_history = []

# Display the conversation history
if len(conversation_history) > 0:
    st.markdown("## Conversation History")
    for message in conversation_history:
        if message["role"] == "user":
            st.text(f"You: {message['content']}")
        else:
            st.text(f"ChatGPT: {message['content']}")
