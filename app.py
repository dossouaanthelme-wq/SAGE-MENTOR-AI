import streamlit as st
import google.generativeai as genai

# Configuration de l'app
st.set_page_config(page_title="Sage Mentor AI", page_icon="🌿")
st.title("🌿 Sage : Ton Mentor Personnel")

# Barre latérale pour la clé API
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Entre ta clé API Google :", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Utilisation du nom de modèle le plus stable
        model = genai.GenerativeModel('gemini-1.5-flash')

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Affichage de l'historique
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Zone de chat - Utilisation stricte de 'prompt' partout
        if prompt := st.chat_input("Comment puis-je t'aider aujourd'hui ?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Génération de la réponse
            response = model.generate_content(prompt)
            
            with st.chat_message("assistant"):
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
else:
    st.info("Bienvenue ! Pour activer Sage, entre ta clé API Google dans le menu à gauche.")
