import streamlit as st
import os
from PIL import Image #pillow library is for image handling
import google.generativeai as genai

genai.configure(api_key = "AIzaSyAVtthYPL9eOGa1g6vmPccuIpzb3W8HVf8")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt]) #model has an inbuilt function c/d generate_content
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
            "mime_type": uploaded_file.type,
            "data": bytes_data
            }
        ]
        return image_parts
    else: 
        raise FileNotFoundError("No file was uploaded. Please upload file.")


st.set_page_config(page_title="Pavni's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Pavni")
st.sidebar.write("Powered by Google Gemini AI")
st.header("RoboBill")
st.subheader("Made by Pavni")
st.subheader("Manage your expenses with RoboBill")


input = st.text_input("How can I help you?",key="input")
uploaded_file = st.file_uploader("Choose an image from your gallery",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",use_column_width=True)

ssumbit = st.button("Let's Go!")

input_prompt = """
You are a mathematics expert. user will upload a file and you have to solve the question using beta and gamma functions. show the steps. greet the user."""

if ssumbit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know!")
    st.write(response)
