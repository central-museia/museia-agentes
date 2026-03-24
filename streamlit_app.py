import streamlit as st

# 1. CONFIGURAÇÃO DE ALTA CONVERSÃO
st.set_page_config(
    page_title="MuseIA Digital | Central de Agentes",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DESIGN SYSTEM MUSEIA (FOCO EM CREDIBILIDADE E MOBILE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');
    
    .stApp { background-color: #080808; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}

    /* Seção Hero */
    .hero-container { text-align: center; padding: 40px 10px; background: radial-gradient(circle at top, #1a1a1a 0%, #080808 100%); }
    .logo-museia { font-size: 28px; font-weight: 800; color: #8A2BE2; letter-spacing: -1px; margin-bottom: 20px; }
    .headline { font-size: 38px; font-weight: 800; line-height: 1.1; margin-bottom: 20px; background: linear-gradient(90deg, #FFF, #BBB); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .sub-headline { font-size: 18px; color: #A0A0A0; margin-bottom: 30px; line-height: 1.4; }

    /* Estilo de Vídeo/Imagem */
    .video-placeholder { width: 100%; max-width: 700px; height: 350px; background: #111; border: 1px solid #333; border-radius: 12px; margin: 0 auto 30px auto; display: flex; align-items: center; justify-content: center; color: #444; }

    /* Preço e Garantia */
    .price-tag { font-size: 22px; font-weight: 700; color: #FFF; margin-bottom: 5px; }
    .garantia-text { font-size: 14px; color: #00FF7F; font-weight: 400; margin-bottom: 30px; }

    /* Benefícios (Grid Mobile Friendly) */
    .benefit-card { background: #121212; border: 1px solid #222; padding: 25px; border-radius: 12px; text-align: center; margin-bottom: 20px; }
    .benefit-icon { font-size: 30px; margin-bottom: 10px; }
    .benefit-title { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: #8A2BE2; }
    .benefit-desc { font-size: 14px; color: #808080; }

    /* Botão CTA Gigante */
    div.stButton > button {
        background: linear-gradient(180deg, #9D4EDD 0%, #7B2CBF 100%) !important;
        color: white !important;
        border: none !important;
        padding: 25px !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(138, 43, 226, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SEÇÃO 1: HERO ---
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown('<div class="logo-museia">MUSEIA DIGITAL</div>', unsafe_allow_html=True)
st.markdown('<h1 class="headline">Biblioteca de Agentes Inteligentes</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-headline">Automatize tarefas e multiplique sua produtividade com IA — sem ser técnico.</p>', unsafe_allow_html=True)

# Player de Vídeo ou Imagem de Destaque
st.markdown('<div class="video-placeholder">VÍDEO DE APRESENTAÇÃO (60s)</div>', unsafe_allow_html=True)

st.markdown('<div class="price-tag">R$ 79,90/mês</div>', unsafe_allow_html=True)
st.markdown('<div class="garantia-text">🛡️ 7 dias de garantia | Cancele quando quiser</div>', unsafe_allow_html=True)

if st.button("QUERO ACESSO IMEDIATO"):
    st.session_state["checkpoint"] = "checkout" # Próximo passo: CORE/pagamentos.py

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- SEÇÃO 2: 3 BENEFÍCIOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="benefit-card">
        <div class="benefit-icon">⚡</div>
        <div class="benefit-title">EM 5 MINUTOS</div>
        <div class="benefit-desc">Agentes prontos para usar. Copie, cole e implemente hoje mesmo.</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="benefit-card">
        <div class="benefit-icon">🔄</div>
        <div class="benefit-title">ATUALIZAÇÕES</div>
        <div class="benefit-desc">Novos agentes todo mês na sua central,
