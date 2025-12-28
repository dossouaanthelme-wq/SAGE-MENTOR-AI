import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sage Mentor AI", page_icon="🌿")
st.title("🌿 Sage : Ton Mentor Personnel")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Entre ta clé API Google :", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        if "messages" not in st.session_state:
            st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if prompt := st.chat_input("Comment puis-je t'aider aujourd'hui ?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            response = model.generate_content(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Erreur : {e}")
else:
    st.info("Bienvenue ! Entre ta clé API à gauche.")
