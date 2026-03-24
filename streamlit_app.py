import streamlit as st

# 1. CONFIGURAÇÃO DE ALTA CONVERSÃO
st.set_page_config(
    page_title="MuseIA Digital | Central de Agentes",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DESIGN SYSTEM MUSEIA (FOCO EM CREDIBILIDADE) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');
    .stApp { background-color: #080808; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; }
    #MainMenu, footer, header {visibility: hidden;}
    .hero-container { text-align: center; padding: 40px 10px; }
    .logo-museia { font-size: 28px; font-weight: 800; color: #8A2BE2; margin-bottom: 20px; }
    .headline { font-size: 38px; font-weight: 800; line-height: 1.1; margin-bottom: 20px; color: #FFFFFF; }
    .sub-headline { font-size: 18px; color: #A0A0A0; margin-bottom: 30px; }
    .video-placeholder { width: 100%; max-width: 700px; height: 350px; background: #111; border: 1px solid #333; border-radius: 12px; margin: 0 auto 30px auto; display: flex; align-items: center; justify-content: center; }
    .benefit-card { background: #121212; border: 1px solid #222; padding: 25px; border-radius: 12px; text-align: center; margin-bottom: 20px; min-height: 180px; }
    div.stButton > button {
        background: linear-gradient(180deg, #9D4EDD 0%, #7B2CBF 100%) !important;
        color: white !important; border: none !important; padding: 20px !important;
        border-radius: 12px !important; font-size: 20px !important; font-weight: 800 !important; width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SEÇÃO 1: HERO ---
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown('<div class="logo-museia">MUSEIA DIGITAL</div>', unsafe_allow_html=True)
st.markdown('<h1 class="headline">Biblioteca de Agentes Inteligentes</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-headline">Automatize tarefas e multiplique sua produtividade com IA — sem ser técnico.</p>', unsafe_allow_html=True)

# Espaço do Vídeo
st.markdown('<div class="video-placeholder">VÍDEO DE APRESENTAÇÃO (60s)</div>', unsafe_allow_html=True)

st.markdown('### R$ 79,90/mês')
st.markdown('<p style="color: #00FF7F;">🛡️ 7 dias de garantia | Cancele quando quiser</p>', unsafe_allow_html=True)

if st.button("QUERO ACESSO IMEDIATO"):
    st.success("Redirecionando para check-out seguro...")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- SEÇÃO 2: 3 BENEFÍCIOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="benefit-card"><h3>⚡ EM 5 MINUTOS</h3><p>Agentes prontos para usar. Copie, cole e implemente hoje mesmo.</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="benefit-card"><h3>🔄 ATUALIZAÇÕES</h3><p>Novos agentes todo mês na sua central, sem pagar nenhum extra.</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="benefit-card"><h3>🛡️ RISCO ZERO</h3><p>Garantia total de 7 dias. Se não gostar, devolvemos seu dinheiro.</p></div>', unsafe_allow_html=True)

st.divider()

# --- SEÇÃO 3: CTA FINAL ---
st.markdown("<div style='text-align:center; padding: 40px 10px;'>", unsafe_allow_html=True)
st.markdown("## MENOS DE R$ 3 POR DIA")
st.markdown("<p style='color:#808080;'>Para ter inteligência artificial trabalhando por você 24 horas por dia.</p>", unsafe_allow_html=True)

if st.button("COMEÇAR AGORA"):
    st.info("Iniciando processo de assinatura...")

st.markdown("<p style='font-size:12px; color:#444; margin-top:20px;'>Pagamento seguro via Hotmart | Acesso imediato</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
