import streamlit as st
import requests
import json
from nocodb.catalogo import obter_headers

def cadastrar_usuario(nome, email, senha):
    """Insere o novo lead no NocoDB tratando as variações de nomes de colunas."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        
        # O NocoDB exige que os campos batam EXATAMENTE com o que está no banco.
        # Vamos usar os nomes que você provavelmente criou, mas o código agora
        # vai capturar o erro se o nome estiver diferente.
        payload = {
            "nome_completo": nome,
            "email": email,
            "senha": senha,
            "status": "Lead"
        }
        
        response = requests.post(url, headers=obter_headers(), json=payload, timeout=10)
        
        if response.status_code in [200, 201]:
            return True
        else:
            # INTERPRETAÇÃO DO ERRO PARA VOCÊ:
            erro_detalhado = response.json()
            msg_erro = erro_detalhado.get('message', '')
            
            if "column" in msg_erro.lower():
                st.error(f"⚠️ Erro de Coluna: O banco não reconheceu um dos campos. Detalhe: {msg_erro}")
            else:
                st.error(f"❌ Erro no NocoDB: {msg_erro}")
            return False
            
    except Exception as e:
        st.error(f"🚨 Falha de conexão com o banco: {e}")
        return False

def validar_login(email, senha):
    """Valida o login buscando o usuário pelo e-mail."""
    try:
        url = st.secrets['nocodb']['url_usuarios']
        # Busca exata pelo e-mail
        params = {"where": f"(email,eq,{email})"}
        response = requests.get(url, headers=obter_headers(), params=params, timeout=10)
        
        records = response.json().get("list") or response.json().get("records") or []
        
        if records:
            user = records[0]
            # Verificação de senha simples (string)
            if str(user.get("senha")) == str(senha):
                return user
        return None
    except Exception as e:
        st.error(f"Erro na validação: {e}")
        return None

def renderizar_interface_login():
    """Desenha a aba de Login e Cadastro."""
    st.markdown("### 🔐 Área do Cliente MuseIA")
    tab_in, tab_up = st.tabs(["Entrar", "Criar Minha Conta"])
    
    with tab_in:
        e = st.text_input("E-mail", key="login_e")
        s = st.text_input("Senha", type="password", key="login_s")
        if st.button("Acessar Painel", use_container_width=True):
            usuario = validar_login(e, s)
            if usuario:
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.success(f"Bem-vinda, {usuario.get('nome_completo', 'Mestra')}!")
                st.rerun()
            else:
                st.error("Login ou senha inválidos.")

    with tab_up:
        st.caption("Cadastre-se para acessar seus robôs e kits gratuitos.")
        n_novo = st.text_input("Nome Completo", key="reg_n")
        e_novo = st.text_input("E-mail", key="reg_e")
        s_novo = st.text_input("Crie uma Senha", type="password", key="reg_s")
        
        if st.button("Concluir Cadastro 🚀", use_container_width=True):
            if n_novo and e_novo and s_novo:
                if cadastrar_usuario(n_novo, e_novo, s_novo):
                    st.balloons()
                    st.success("Conta criada! Agora é só fazer login na aba ao lado.")
            else:
                st.warning("Preencha todos os campos para continuar.")
