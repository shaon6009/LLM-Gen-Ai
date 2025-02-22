import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("Google API Key not found. Please set it in a .env file.")
#     st.stop()

api_key = "AIzaSyAZSVrLnYWBdIT9asZu7Qo5Y9EtN7taHFM"

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")


def load_custom_data(file_path="G:\ornob\ai.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "No custom data found."

custom_data = load_custom_data()

# Streamlit UI
st.title("💬 Custom AI Chatbot with Streamlit")
st.write("Chat with AI trained on your custom data!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("You:", "")

if user_input:
    # Combine user input with custom data
    prompt = f"Use the following information to answer: {custom_data}\n\nUser: {user_input}"

    try:
        # Generate response
        response = model.generate_content([prompt])  # Gemini API requires input as a list

        # Ensure response exists
        if hasattr(response, "text"):
            bot_response = response.text
        else:
            bot_response = "Sorry, I couldn't generate a response."

        # Store in chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_response))

    except Exception as e:
        st.error(f"Error generating response: {str(e)}")

# Display chat history
for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")
