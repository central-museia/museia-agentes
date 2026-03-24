import streamlit as st

# 1. CONFIGURAÇÃO DE ELITE (Deve ser a primeira linha)
st.set_page_config(
    page_title="MuseIA Digital | Inteligência Artificial",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BLINDAGEM DE IMPORTAÇÃO (SILENCIOSA) ---
try:
    from core import pagamentos
except:
    class pagamentos:
        @staticmethod
        def exibir_login(): 
            st.markdown("<div style='text-align:center; padding:50px;'><h2>🔐 Portal Reservado</h2><p>Aguardando conexão com o módulo de segurança.</p></div>", unsafe_allow_html=True)
            if st.button("ACESSO ADMINISTRADOR"): st.session_state["logado"] = True; st.rerun()

# 2. DESIGN SYSTEM MUSEIA (CSS PREMIUM)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');

    /* Background & Global */
    .stApp {{
        background-color: #050505;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }}

    /* Header Estilo Payhip/Netflix */
    .main-header {{
        text-align: center;
        padding: 60px 0 20px 0;
    }}
    .logo-text {{
        font-size: 50px;
        font-weight: 700;
        color: #E50914; /* Vermelho Assinatura */
        letter-spacing: -1.5px;
        margin-bottom: 0px;
    }}
    .subtitle {{
        color: #808080;
        font-size: 18px;
        font-weight: 300;
        margin-bottom: 40px;
    }}

    /* Grid de Agentes (Cards Estilo Glassmorphism) */
    .agent-card {{
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        border: 1px solid #333;
        border-radius: 12px;
        padding: 35px 25px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .agent-card:hover {{
        transform: translateY(-10px);
        border-color: #E50914;
        box-shadow: 0 20px 40px rgba(229, 9, 20, 0.15);
    }}
    .agent-icon {{ font-size: 45px; margin-bottom: 15px; }}
    .agent-name {{ font-size: 22px; font-weight: 700; margin-bottom: 10px; }}
    .agent-desc {{ font-size: 14px; color: #999; line-height: 1.4; }}

    /* CTA / Botões Estratégicos */
    div.stButton > button {{
        background: #E50914 !important;
        color: white !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 6px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: 0.3s !important;
        width: 100%;
    }}
    div.stButton > button:hover {{
        background: #b20710 !important;
        transform: scale(1.02);
    }}

    /* Inputs Dark */
    .stTextInput input {{ background-color: #1a1a1a !important; border: 1px solid #333 !important; color: white !important; }}
</style>
""", unsafe_allow_html=True)

# 3. CONTROLE DE SESSÃO
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "agente" not in st.session_state:
    st.session_state["agente"] = None

# --- TELA DE LOGIN (CORE) ---
if not st.session_state["logado"]:
    st.markdown("<div class='main-header'><h1 class='logo-text'>MUSEIA DIGITAL</h1><p class='subtitle'>A maior central de automação e inteligência de mercado.</p></div>", unsafe_allow_html=True)
    pagamentos.exibir_login()
    st.stop()

# --- VITRINE PRINCIPAL (UI DE CATÁLOGO) ---
if st.session_state["agente"] is None:
    # Header do Catálogo
    st.markdown("<div class='main-header'><h1 class='logo-text'>MUSEIA</h1><p class='subtitle'>Selecione sua ferramenta original de produtividade.</p></div>", unsafe_allow_html=True)
    
    st.markdown("### 🔥 Populares no Mercado")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class='agent-card'>
            <div class='agent-icon'>🏆</div>
            <div class='agent-name'>Deep Scan</div>
            <div class='agent-desc'>Análise profunda de concorrência e extração de diferenciais estratégicos.</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Iniciar Agente 04"):
            st.session_state["agente"] = "deepscan"; st.rerun()

    with col2:
        st.markdown("""<div class='agent-card'>
            <div class='agent-icon'>📑</div>
            <div class='agent-name'>Currículo Master</div>
            <div class='agent-desc'>Triagem de talentos em massa com ranking de compatibilidade por IA.</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Iniciar Agente 31"):
            st.session_state["agente"] = "curriculos"; st.rerun()

    with col3:
        st.markdown("""<div class='agent-card'>
            <div class='agent-icon'>📧</div>
            <div class='agent-name'>Humanizador</div>
            <div class='agent-desc'>Transformação de scripts robóticos em comunicações de alto engajamento.</div>
        </div>""", unsafe_allow_html=True)
        if st.button("Iniciar Agente 13"):
            st.session_state["agente"] = "humanizador"; st.rerun()

# --- ÁREA DE TRABALHO (INTERNA) ---
else:
    col_nav, _ = st.columns([1, 4])
    with col_nav:
        if st.button("← VOLTAR"):
            st.session_state["agente"] = None
            st.rerun()
    
    st.markdown(f"## Operando Agente: {st.session_state['agente'].upper()}")
    st.divider()
    
    # Aqui o Mandante fica esperando você conectar os arquivos das pastas utils/
    st.info("Aguardando entrada de dados na camada de utilitários...")
