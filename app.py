import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

#for m in genai.list_models():
  #  print(m.name)
  
sys_prompt = """You are an expert programmer. Review thw code given by user, analyze it and provide the response in following pattern.
                    * How much percentage of code provided by user is correct.
                    * List down the bugs in the code with explanantion in 1 line.
                    * Generate the correct code."""
    
llm = genai.GenerativeModel(model_name='gemini-1.5-flash',system_instruction=sys_prompt)
st.title("CODEVIEWER")
st.subheader('YOUR PERSONAL AI CODE REVIEWER')

user_prompt = st.text_area("Write your code...(ANY LANGUAGE)")
Submit = st.button('Submit')

       
if Submit:
    if user_prompt.strip():
        try:
            response = llm.generate_content(user_prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide code to analyze.")