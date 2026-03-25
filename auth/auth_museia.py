import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    """
    Cadastro seguindo EXATAMENTE o seu CSV: 
    nome, email, senha, status_pagamento, ativo, bloqueado
    """
    try:
        url = st.secrets['nocodb']['url_usuarios']
        
        # Payload com os nomes de coluna do seu arquivo 'Getting Started - Usuarios'
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "status_pagamento": "Gratuito",
            "ativo": True,
            "bloqueado": False
        }
        
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            return True
        else:
            # Se der erro de Throttler, vamos avisar de forma amigável
            if "ThrottlerException" in response.text:
                st.warning("⏳ O servidor do NocoDB pediu uma pausa. Aguarde 30 segundos e tente o último clique.")
            else:
                st.error(f"Erro do Banco: {response.text}")
            return False
    except Exception as e:
        st.error(f"Falha técnica: {e}")
        return False

def validar_login(email, senha):
    """Validação baseada nas colunas do seu banco."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        # Filtro de busca por e-mail
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        
        records = response.json().get("list") or response.json().get("records") or []
        
        if records:
            user = records[0]
            # Valida a coluna 'senha'
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except Exception as e:
        st.error(f"Erro na validação: {e}")
        return None

def renderizar_interface_login():
    st.markdown("### 🔐 Área do Cliente MuseIA")
    tab_login, tab_cadastro = st.tabs(["Entrar", "Criar Conta Grátis"])
    
    with tab_login:
        email = st.text_input("E-mail", key="l_email")
        senha = st.text_input("Senha", type="password", key="l_senha")
        if st.button("Acessar Minha Área", use_container_width=True):
            user = validar_login(email, senha)
            if user:
                st.session_state.logado = True
                st.session_state.usuario = user
                st.success(f"Bem-vinda, {user.get('nome')}!")
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with tab_cadastro:
        nome_reg = st.text_input("Nome", key="reg_nome")
        email_reg = st.text_input("E-mail", key="reg_email")
        senha_reg = st.text_input("Defina uma Senha", type="password", key="reg_senha")
        
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if nome_reg and email_reg and senha_reg:
                if cadastrar_usuario(nome_reg, email_reg, senha_reg):
                    st.balloons()
                    st.success("✅ Cadastro realizado! Vá para a aba 'Entrar'.")
            else:
                st.warning("Preencha todos os campos.")
