import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    try:
        url = st.secrets['nocodb']['url_usuarios']
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "status_pagamento": "pendente",
            "ativo": True,
            "bloqueado": False
        }
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            return True
        return False
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
    """Interface limpa, sem mensagens técnicas ou alertas de sistema."""
    st.markdown("### 🔐 Área do Cliente")
    tab_login, tab_cadastro = st.tabs(["Entrar", "Criar Conta Grátis"])
    
    with tab_login:
        email = st.text_input("E-mail", key="l_email")
        senha = st.text_input("Senha", type="password", key="l_senha")
        if st.button("Acessar Painel", use_container_width=True):
            user = validar_login(email, senha)
            if user:
                st.session_state.logado = True
                st.session_state.usuario = user
                st.rerun()
            else:
                st.error("Dados de acesso incorretos. Tente novamente.")

    with tab_cadastro:
        nome_reg = st.text_input("Nome", key="reg_nome")
        email_reg = st.text_input("E-mail", key="reg_email")
        senha_reg = st.text_input("Defina uma Senha", type="password", key="reg_senha")
        
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if nome_reg and email_reg and senha_reg:
                if cadastrar_usuario(nome_reg, email_reg, senha_reg):
                    st.balloons()
                    st.success("Conta criada com sucesso! Agora você pode acessar o painel.")
                else:
                    # Mensagem discreta para falhas de servidor ou limite de requisições
                    st.warning("Não foi possível processar agora. Por favor, tente em instantes.")
            else:
                st.info("Preencha todos os campos para continuar.")
