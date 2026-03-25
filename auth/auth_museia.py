import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    """
    Cadastro seguindo rigorosamente a estrutura do CSV:
    nome, email, senha, status_pagamento, ativo, bloqueado
    """
    try:
        url = st.secrets['nocodb']['url_usuarios']
        
        # Payload ajustado conforme o seu arquivo Getting Started - Usuarios
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "status_pagamento": "Gratuito", # Campo exato do seu CSV
            "ativo": True,                 # Campo exato do seu CSV
            "bloqueado": False             # Campo exato do seu CSV
        }
        
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            return True
        else:
            # Se o erro persistir, o NocoDB dirá o porquê aqui
            st.error(f"Erro do NocoDB: {response.text}")
            return False
    except Exception as e:
        st.error(f"Falha técnica: {e}")
        return False

def validar_login(email, senha):
    """Busca o usuário e valida a senha conforme as colunas do seu CSV."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        
        records = response.json().get("list") or response.json().get("records") or []
        
        if records:
            user = records[0]
            # Validação direta da coluna 'senha' do seu CSV
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except Exception as e:
        st.error(f"Erro na validação: {e}")
        return None

def renderizar_interface_login():
    st.markdown("### 🔐 Área do Cliente MuseIA")
    tab_in, tab_up = st.tabs(["Entrar", "Criar Conta Grátis"])
    
    with tab_in:
        e = st.text_input("E-mail", key="l_e")
        s = st.text_input("Senha", type="password", key="l_s")
        if st.button("Acessar Painel", use_container_width=True):
            usuario = validar_login(e, s)
            if usuario:
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.success(f"Bem-vinda, {usuario.get('nome')}!")
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with tab_up:
        n_input = st.text_input("Nome", key="r_n")
        e_input = st.text_input("E-mail", key="r_e")
        s_input = st.text_input("Defina uma Senha", type="password", key="r_s")
        
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if n_input and e_input and s_input:
                if cadastrar_usuario(n_input, e_input, s_input):
                    st.balloons()
                    st.success("✅ Cadastro realizado com sucesso! Vá para a aba 'Entrar'.")
            else:
                st.warning("Preencha todos os campos.")
