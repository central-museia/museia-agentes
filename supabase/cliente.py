from supabase import create_client
import streamlit as st

def get_client():
    """Cria e retorna o cliente oficial do Supabase usando secrets seguros."""
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["anon_key"]
        return create_client(url, key)
    except KeyError:
        st.error("Erro de Configuração: As chaves do Supabase não foram encontradas no st.secrets.")
        st.stop()
        import bcrypt
from .cliente import get_client

# =========================================
# 🔐 GESTÃO DE ACESSO E SEGURANÇA
# =========================================

def hash_senha(senha):
    """Gera hash seguro para salvar no banco."""
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def verificar_senha(senha_digitada, senha_hash):
    """Compara senha digitada com o hash do banco."""
    return bcrypt.checkpw(senha_digitada.encode(), senha_hash.encode())

def validar_login(email, senha):
    """Valida o login. O 'strip().lower()' garante que espaços ou letras 
    maiúsculas no e-mail não bloqueiem o cliente legítimo."""
    try:
        supabase = get_client()
        email_limpo = email.strip().lower()
        
        response = (
            supabase
            .table("usuarios")
            .select("*")
            .eq("email", email_limpo)
            .execute()
        )
        
        if response.data:
            usuario = response.data[0]
            senha_hash = usuario.get("senha")
            if senha_hash and verificar_senha(senha, senha_hash):
                return usuario
        return None
    except Exception as e:
        print(f"Erro na validação: {str(e)}")
        return None