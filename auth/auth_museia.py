import streamlit as st
import requests
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    """Insere o lead no NocoDB usando os nomes de coluna: nome, email, senha, status."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        
        # Usando 'nome' conforme sua orientação do banco
        payload = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "status": "Lead"
        }
        
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            return True
        else:
            # Se ainda der erro, o Streamlit vai mostrar o motivo exato aqui:
            st.error(f"Erro do Banco (Verifique os nomes das colunas): {response.text}")
            return False
    except Exception as e:
        st.error(f"Falha de comunicação: {e}")
        return False

def validar_login(email, senha):
    """Valida o login buscando pelo campo 'email'."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        
        # Tenta capturar a lista de registros
        dados = response.json().get("list") or response.json().get("records") or []
        
        if dados:
            user = dados[0]
            # Valida se a senha bate com a coluna 'senha'
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except Exception as e:
        st.error(f"Erro na validação: {e}")
        return None

def renderizar_interface_login():
    """Interface de acesso simplificada."""
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
                st.success(f"Bem-vinda, {user.get('nome', 'Usuária')}!")
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with aba_cadastro:
        nome_input = st.text_input("Nome", key="reg_nome")
        email_input = st.text_input("E-mail", key="reg_email")
        senha_input = st.text_input("Defina uma Senha", type="password", key="reg_senha")
        
        if st.button("Finalizar Cadastro 🚀", use_container_width=True):
            if nome_input and email_input and senha_input:
                if cadastrar_usuario(nome_input, email_input, senha_input):
                    st.success("✅ Cadastro realizado! Agora você pode fazer login.")
            else:
                st.warning("Preencha todos os campos.")
