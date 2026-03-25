import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    try:
        url = st.secrets['nocodb']['url_usuarios']
        payload = {"nome": nome, "email": email, "senha": senha}
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        return response.status_code in [200, 201]
    except:
        return False

def validar_login(email, senha):
    try:
        url = st.secrets['nocodb']['url_usuarios']
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        data = response.json()
        records = data.get("list") or data.get("records") or []
        if records:
            user = records[0]
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except:
        return None

def renderizar_interface_login():
    st.markdown("#### 🔐 Acesso MuseIA")
    t1, t2 = st.tabs(["Entrar", "Cadastrar"])
    with t1:
        e = st.text_input("E-mail", key="l_e")
        s = st.text_input("Senha", type="password", key="l_s")
        if st.button("Confirmar Login"):
            u = validar_login(e, s)
            if u:
                st.session_state.logado = True
                st.session_state.usuario = u
                st.rerun()
            else: st.error("Dados incorretos.")
    with t2:
        n = st.text_input("Nome", key="r_n")
        em = st.text_input("E-mail", key="r_e")
        se = st.text_input("Senha", type="password", key="r_s")
        if st.button("Criar Conta"):
            if cadastrar_usuario(n, em, se):
                st.success("Sucesso! Vá em 'Entrar'.")
