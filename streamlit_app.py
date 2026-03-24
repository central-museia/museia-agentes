import streamlit as st
import requests

# 1. CONFIGURAÇÃO DA PÁGINA (DEVE SER A PRIMEIRA LINHA)
st.set_page_config(page_title="MuseIA Digital", layout="wide", page_icon="🟣")

# 2. ESTILO CSS CUSTOMIZADO (NETFLIX DARK STYLE)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Títulos e Textos */
    h1 { color: #E50914; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    h2, h3 { color: #ffffff; font-weight: 300; }
    
    /* Cards de Agentes */
    .card {
        background-color: #141414; border: 1px solid #333; padding: 30px; border-radius: 8px;
        text-align: center; transition: transform .3s; min-height: 180px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .card:hover { transform: scale(1.05); border-color: #E50914; background-color: #181818; }
    .card-title { font-size: 22px; font-weight: bold; margin-bottom: 5px; color: #E50914; }
    
    /* Botões Netflix */
    div.stButton > button {
        background-color: #E50914 !important; color: white !important; border-radius: 4px !important;
        border: none !important; width: 100% !important; font-weight: bold !important; 
        padding: 12px !important; text-transform: uppercase; letter-spacing: 1px;
    }
    div.stButton > button:hover { background-color: #ff0f1b !important; box-shadow: 0px 0px 15px 5px rgba(229,9,20,0.3); }

    /* Inputs e Áreas de Texto */
    .stTextInput input, .stTextArea textarea { background-color: #333 !important; color: white !important; border: 1px solid #444 !important; }
</style>
""", unsafe_allow_html=True)

# 3. FUNÇÕES DE SUPORTE (AS "ENGRENAGENS")
def chamar_ia_gemini(prompt):
    """Função central de IA - Requer GEMINI_API_KEY nos Secrets"""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return "⚠️ Erro na API: Verifique se sua chave está correta nos Secrets."
    except Exception as e:
        return f"⚠️ Erro de Configuração: {e}"

# 4. LÓGICA DE LOGIN/ACESSO
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    col_l1, col_l2, col_l3 = st.columns([1,2,1])
    with col_l2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.title("🍿 Entrar na MuseIA")
        token = st.text_input("Token de Acesso", type="password", placeholder="Insira seu código do Payhip")
        if st.button("ASSISTIR AGORA"):
            if token == "teste123": # Altere para o token desejado
                st.session_state["logado"] = True
                st.rerun()
            else:
                st.error("Token Inválido.")
    st.stop()

# 5. HEADER PRINCIPAL
st.title("MUSEIA DIGITAL")
st.markdown("#### Agentes Originais MuseIA • Catálogo 2026")

# 6. NAVEGAÇÃO ENTRE AGENTES
if "agente" not in st.session_state:
    st.session_state["agente"] = None

# VITRINE (PÁGINA INICIAL)
if st.session_state["agente"] is None:
    st.markdown("## Populares na MuseIA")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><div class="card-title">🏆 DEEP SCAN</div><p>Análise de Concorrentes</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 04"):
            st.session_state["agente"] = "deepscan"; st.rerun()

    with col2:
        st.markdown('<div class="card"><div class="card-title">📑 CURRÍCULOS</div><p>Triagem Inteligente</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 31"):
            st.session_state["ag
