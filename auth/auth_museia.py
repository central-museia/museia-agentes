import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    """Envia o novo lead para o NocoDB."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        payload = {
            "nome_completo": nome,
            "email": email,
            "senha": senha,
            "status": "Lead",
            "nivel_acesso": "Gratuito"
        }
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        return response.status_code in [200, 201]
    except:
        return False

def validar_login(email, senha):
    """Verifica se o usuário existe e a senha bate no NocoDB."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        # Filtro para buscar apenas o e-mail específico
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        dados = response.json().get("list") or []
        
        if dados and dados[0].get("senha") == senha:
            return dados[0] # Retorna os dados do usuário
        return None
    except:
        return None

def renderizar_interface_login():
    """Desenha a caixa de login/cadastro de forma isolada."""
    st.markdown("### 🔐 Área do Cliente")
    aba_login, aba_cadastro = st.tabs(["Entrar", "Criar Conta Grátis"])
    
    with aba_login:
        email = st.text_input("E-mail", key="auth_email")
        senha = st.text_input("Senha", type="password", key="auth_senha")
        if st.button("Acessar Minha MuseIA", use_container_width=True):
            user = validar_login(email, senha)
            if user:
                st.session_state.logado = True
                st.session_state.usuario = user
                st.success(f"Bem-vindo(a), {user['nome_completo']}!")
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with aba_cadastro:
        nome = st.text_input("Nome Completo", key="reg_nome")
        email_reg = st.text_input("E-mail", key="reg_email")
        senha_reg = st.text_input("Defina uma Senha", type="password", key="reg_senha")
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if nome and email_reg and senha_reg:
                if cadastrar_usuario(nome, email_reg, senha_reg):
                    st.success("Cadastro realizado! Você já pode entrar.")
                else:
                    st.error("Erro ao cadastrar. Tente novamente.")
