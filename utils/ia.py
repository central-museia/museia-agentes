import streamlit as st
import google.generativeai as genai


# =========================================
# CONFIGURAÇÃO
# =========================================
def configurar_ia():
    genai.configure(api_key=st.secrets["ia"]["gemini_key"])


# =========================================
# FUNÇÃO PRINCIPAL
# =========================================
def gerar_resposta(prompt, modelo="gemini-1.5-flash"):

    try:
        configurar_ia()

        model = genai.GenerativeModel(modelo)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Erro na IA: {str(e)}"
