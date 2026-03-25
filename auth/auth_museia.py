import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    try:
        url = st.secrets['nocodb']['url_usuarios']
        # Usando estritamente as colunas do seu CSV
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha
        }
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        return response.status_code in [200, 201]
    except:
        return False

def validar_login(email, senha):
    try:
        url = st.secrets['nocodb']['url_usuarios']
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        records = response.json().get("list") or response.json().get("records") or []
        
        if records:
            user = records[0]
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except:
        return None

def renderizar_interface_login():
    st.markdown("### 🔐 Área do Cliente")
    tab_in, tab_up = st.tabs(["Entrar", "Criar Conta"])
    
    with tab_in:
        e = st.text_input("E-mail", key="l_e")
        s = st.text_input("Senha", type="password", key="l_s")
        if st.button("Acessar Painel", use_container_width=True):
            user = validar_login(e, s)
            if user:
                st.session_state.logado = True
                st.session_state.usuario = user
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with tab_up:
        n_input = st.text_input("Nome Completo", key="r_n")
        e_input = st.text_input("E-mail", key="r_e")
        s_input = st.text_input("Senha", type="password", key="r_s")
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if n_input and e_input and s_input:
                if cadastrar_usuario(n_input, e_input, s_input):
                    st.balloons()
                    st.success("Conta criada! Agora clique na aba 'Entrar'.")
                else:
                    st.warning("Não foi possível processar. Tente em instantes.")
