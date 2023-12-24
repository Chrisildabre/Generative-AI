from dotenv import load_dotenv
load_dotenv() #load all env variables

import streamlit as st
import os
import google.generativeai as genai


GOOGLE_API_KEY="AIzaSyC-RosGyJE2NMu9_JnJ5UvbF5jJHPiox3U"
genai.configure(api_key=GOOGLE_API_KEY)

#func to load gemini
model=genai.GenerativeModel("gemini-pro")
def get_gem_response(question):
    response=model.generate_content(question)
    return response.text

#streamlit app
st.set_page_config(page_title="Gemini Pro Query Application")
st.header("Gemini Pro Query Application")
input=st.text_input("Input: ",key="Input")
submit=st.button("Ask Question")

#when submit is clicked
if submit:
    response=get_gem_response(input)
    st.subheader("The response is:")
    st.write(response)
    
                