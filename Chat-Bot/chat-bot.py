# libraries
import streamlit as st
import google.generativeai as genai

# Google_API configuration
GOOGLE_API_KEY = "AIzaSyA1dfdxtl_4YiT_BBR-fmbnvYFZrCuZu0o"
genai.configure(api_key=GOOGLE_API_KEY)

# initalize generative ai model
model = genai.GenerativeModel('gemini-1.5-flash')

# function to get response from model
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# streamlit interface
st.set_page_config(page_title="Simple ChatBot!", layout='centered')
st.title("Simple Chatbot 🤖")
st.write("Powered by Google.")



with st.form(key="chat-form", clear_on_submit=True):

    # promopt input text using streamlit
    prompt = st.text_input("", max_chars=2000)
    # send button
    submit_button = st.form_submit_button("Send")
    # condition if text_input empty
    if submit_button:
        if prompt:
            response = get_response(prompt)
            # display response 
            st.write(response)
            # st.session_state.history.append((prompt, response))
        else:
            st.warning("Please enter a prompt.")