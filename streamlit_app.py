import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS", page_icon="🤖", layout="wide")
st.title("🤖 JARVIS")
st.caption("Assistente personale di Metà")

api_key = st.text_input("Incolla qui la tua API Key di Gemini", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Cosa devo fare Metà?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Sto pensando..."):
                response = model.generate_content("Sei Jarvis di cristian. Rispondi corto e diretto: " + prompt)
                st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Incolla la tua API Key di Google Gemini per iniziare")
