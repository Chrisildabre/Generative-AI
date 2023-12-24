import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

GOOGLE_API_KEY="AIzaSyC-RosGyJE2NMu9_JnJ5UvbF5jJHPiox3U"
genai.configure(api_key=GOOGLE_API_KEY)

#func to load gemini
model=genai.GenerativeModel("gemini-pro-vision")

def get_gem_response(question,image):
    if input!="":
        response=model.generate_content([question,image])
    else:
         response=model.generate_content(image)
    return response.text

#streamlit app
st.set_page_config(page_title="Gemini image Query Application")
st.header("Gemini vision Query Application")
input=st.text_input("Input: ",key="Input")

uploadded_file=st.file_uploader("Choose an image..", type=["jpg", "png","gif","jpeg"])
image=""
if uploadded_file is not None:
    image=image.open(uploadded_file)
    st.image(image, caption="upload image", use_column_width=True)

submit=st.button("Tell me about the image")

if submit:
    response=get_gem_response(input,image)
    st.subheader("The response is:")
    st.write(response)