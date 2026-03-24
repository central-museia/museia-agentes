import streamlit as st

# 1. SETUP DE ELITE
st.set_page_config(
    page_title="MuseIA Digital | Central de Inteligência",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PERSONALIZADO (MUSEIA HIGH-TECH) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;700&display=swap');

    .stApp {
        background-color: #0A0A0B;
        color: #F8F9FA;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Esconder elementos padrão */
    #MainMenu, footer, header {visibility: hidden;}

    /* Título MuseIA - Tipografia Forte */
    .logo-museia {
        font-size: 62px;
        font-weight: 800;
        background: -webkit-linear-gradient(#FFFFFF, #8A2BE2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
        text-align: center;
        margin-top: 50px;
    }

    .tagline {
        text-align: center;
        color: #A0A0A0; /* Cor corrigida para leitura clara */
        font-size: 20px;
        font-weight: 300;
        margin-bottom: 50px;
    }

    /* Carrossel de Ofertas (Simulado com Estilo) */
    .highlight-box {
        background: linear-gradient(90deg, #161618 0%, #1D1D20 100%);
        border: 1px solid #2D2D30;
        border-radius: 16px;
        padding: 40px;
        text-align: left;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Input de E-mail / Token Estilizado */
    .stTextInput input {
        background-color: #161618 !important;
        border: 1px solid #333 !important;
        color: white !important;
        padding: 15px !important;
        border-radius: 8px !important;
        font-size: 16px !important;
    }

    /* Botão CTA Magnético */
    div.stButton > button {
        background: #8A2BE2 !important; /* Roxo MuseIA */
        color: white !important;
        border: none !important;
        padding: 20px 40px !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        text-transform: uppercase;
        width: 100%;
        transition: 0.4s all;
    }
    div.stButton > button:hover {
        background: #7A1FC2 !important;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.5);
        transform: translateY(-2px);
    }

    /* Grid de Agentes */
    .card-agente {
        background: #161618;
        border: 1px solid #2D2D30;
        padding: 30px;
        border-radius: 12px;
        height: 250px;
        transition: 0.3s;
    }
    .card-agente:hover {
        border-color: #8A2BE2;
        background: #1D1D20;
    }
</style>
""", unsafe_allow_html=True)

# 2. LÓGICA DE ESTADO
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "agente" not in st.session_state:
    st.session_state["agente"] = None

# --- PÁGINA DE ENTRADA (OFERTA E ACESSO) ---
if not st.session_state["logado"]:
    st.markdown('<h1 class="logo-museia">MuseIA Digital</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Inteligência de Mercado e Automação de Alto Impacto.</p>', unsafe_allow_html=True)
    
    # Simulação de Carrossel de Ofertas
    st.markdown("""
    <div class="highlight-box">
        <span style="color: #8A2BE2; font-weight: bold; text-transform: uppercase; font-size: 12px;">Destaque da Semana</span>
        <h2 style="margin: 10px 0;">Deep Scan Agente 04</h2>
        <p style="color: #B0B0B0; font-size: 16px;">Analise seus concorrentes em segundos e descubra brechas de mercado invisíveis a olho nu.</p>
    </div>
    """, unsafe_allow_html=True)

    # Campo de Entrada Estratégico
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        email_acesso = st.text_input("", placeholder="Insira seu e-mail ou token de acesso")
        if st.button("ATIVAR MINHA INTELIGÊNCIA"):
            if email_acesso: # Lógica de validação virá da pasta CORE
                st.session_state["logado"] = True
                st.rerun()
            else:
                st.error("Por favor, insira uma credencial válida.")
    st.stop()

# --- ÁREA INTERNA (CATÁLOGO DE PRODUTOS) ---
if st.session_state["agente"] is None:
    st.markdown('<h1 style="font-size: 40px; margin-bottom: 30px;">Sua Central de Comando</h1>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown('<div class="card-agente"><h3>🏆 Deep Scan</h3><p style="color:#808080">Raio-x de concorrência e propostas de valor.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Deep Scan"): st.session_state["agente"] = "04"; st.rerun()

    with col_b:
        st.markdown('<div class="card-agente"><h3>📑 Filtro CV</h3><p style="color:#808080">Triagem automatizada de talentos por competência.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Filtro"): st.session_state["agente"] = "31"; st.rerun()

    with col_c:
        st.markdown('<div class="card-agente"><h3>📧 Humanizador</h3><p style="color:#808080">Otimização de comunicação para conversão.</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Humanizador"): st.session_state["agente"] = "13"; st.rerun()

else:
    if st.button("← VOLTAR PARA CENTRAL"):
        st.session_state["agente"] = None
        st.rerun()
    st.write(f"### Módulo {st.session_state['agente']} em operação...")
