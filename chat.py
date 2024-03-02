import streamlit as st
import pathlib
import textwrap
import os
import PIL.Image

import google.ai.generativelanguage as glm

# Importing Necessary packages
import pathlib
import textwrap
import os
import PIL.Image

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


# Initialize gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel('gemini-pro')
hist={}
chat=model.start_chat(history=[])
# Function to process text input and generate bot response
def process_text_message(user_input):
    # Add your text-based chatbot logic here
    bot_response = response=chat.send_message(user_input)
    return bot_response

# Function to process image input and generate bot response
def process_image_message(image):
    # Add your image-based chatbot logic here
    bot_response = "Bot: Image received and processed successfully!"
    return bot_response

# Streamlit app layout
st.title("Chatbot Interface")

st.markdown(
    """
    <style>
    .stTextInput > div > div > div > input {
        border-radius: 20px;
        border: 1px solid #ddd;
        padding: 10px;
        width: 400px;
    }
    .stButton > button {
        border-radius: 20px;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stTextArea > div > textarea {
        border-radius: 20px;
        border: 1px solid #ddd;
        padding: 10px;
        width: 400px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Text input for user message
user_input = st.text_input("Enter your message here:")

# Send message button for text input
if st.button("Send"):
    # Process user message and get bot response
    bot_response = process_text_message(user_input)
    # Display bot response
    st.text_area("Bot's Response:", value=bot_response.text, height=100)