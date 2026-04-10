from supabase import create_client
import streamlit as st
import bcrypt

# =========================================
# 🔌 CONEXÃO SUPABASE
# =========================================

# 1. FUNÇÃO DE CONEXÃO (O "MOTOR")
def get_client():
    try:
        # Puxa as credenciais do seu arquivo secrets.toml
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["anon_key"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Erro na conexão com Supabase: {e}")
        return None

# 2. BUSCA DE AGENTES
def obter_agentes():
    """Busca todos os agentes ativos (Tabela: agentes)"""
    try:
        supabase = get_client()
        if not supabase: return []
        # AJUSTADO: 'agentes' no plural para casar com seu banco
        res = supabase.table("agentes").select("*").eq("ativo", True).execute()
        return res.data if res.data else []
    except Exception:
        return []

# 3. BUSCA DE PERFIS (DINÂMICO)
def obter_perfis():
    """Busca apenas os nomes dos perfis ativos"""
    try:
        supabase = get_client()
        if not supabase: return []
        res = supabase.table("perfis").select("").eq("ativo", True).execute()
        return [item['nome'] for item in res.data]
    except Exception:
        return []

# 4. BUSCA DE COLEÇÕES (DINÂMICO)
def obter_colecoes():
    try:
        supabase = get_client()
        res = supabase.table("colecoes").select("*").eq("ativo", True).execute()
        return res.data if res.data else []
    except Exception:
        return []
# =========================================
# 🔐 GESTÃO DE ACESSO
# =========================================

def hash_senha(senha):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

def verificar_senha(senha_digitada, senha_hash):
    if not senha_hash:
        return False
    return bcrypt.checkpw(senha_digitada.encode(), senha_hash.encode())

def validar_login(email, senha):
    try:
        supabase = get_client()
        email_limpo = email.strip().lower()
        response = supabase.table("usuarios").select("*").eq("email", email_limpo).execute()

        if response.data:
            usuario = response.data[0] # Pega o primeiro item da lista
            if not usuario.get("ativo"):
                st.warning("Esta conta não está ativa.")
                return None
            if usuario.get("bloqueado"):
                st.error("Acesso bloqueado.")
                return None
            
            senha_hash = usuario.get("senha")
            if senha_hash and verificar_senha(senha, senha_hash):
                return usuario
        return None
    except Exception as e:
        st.error(f"Erro na validação: {str(e)}")
        return None

# =========================================
# 📊 BUSCA DE DADOS (CATÁLOGO DINÂMICO)
# =========================================

def obter_agentes():
    """Busca todos os robôs ativos com seus perfis e coleções vinculados"""
    try:
        supabase = get_client()
        if not supabase: return []
        
        # AQUI ESTÁ A MÁGICA:
        # Selecionamos tudo do agente E mergulhamos nas tabelas de ligação
        # para buscar o 'nome' lá na ponta.
        res = supabase.table("agentes").select("""
            *,
            agentes_perfis (
                perfis (
                    nome
                )
            ),
            agentes_colecoes (
                colecoes (
                    nome
                )
            )
        """).eq("ativo", True).execute()
        
        return res.data if res.data else []
    except Exception as e:
        print(f"Erro ao buscar agentes: {e}")
        return []
    
def obter_perfis():
    """Busca os nomes dos perfis ativos"""
    try:
        supabase = get_client()
        if not supabase: return []
        # Garantindo que o select peça a coluna 'nome'
        res = supabase.table("perfis").select("nome").eq("ativo", True).execute()
        return [item['nome'] for item in res.data]
    except Exception:
        return []

def obter_colecoes():
    """Busca os nomes das coleções ativas"""
    try:
        supabase = get_client()
        if not supabase: return []
        res = supabase.table("colecoes").select("nome").eq("ativo", True).execute()
        return [item['nome'] for item in res.data]
    except Exception:
        return []