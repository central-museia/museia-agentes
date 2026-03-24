import streamlit as st
from core import pagamentos
from utils import ia, scraping, pdf
# from nocodb import catalogo  # Ative quando configurar o Nocodb

# 1. Configuração de Página
st.set_page_config(page_title="MuseIA Digital | Netflix Edition", layout="wide", page_icon="🟣")

# ===== ESTILO CSS CUSTOMIZADO (NETFLIX STYLE) =====
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    h1 { color: #E50914; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    h2, h3 { color: #ffffff; font-weight: 300; }
    .card {
        background-color: #141414; border: 1px solid #333; padding: 40px 20px; border-radius: 8px;
        text-align: center; transition: transform .3s; min-height: 200px;
        display: flex; flex-direction: column; justify-content: center; margin-bottom: 10px;
    }
    .card:hover { transform: scale(1.05); border-color: #E50914; background-color: #181818; }
    .card-title { font-size: 24px; font-weight: bold; margin-bottom: 10px; }
    div.stButton > button {
        background-color: #E50914 !important; color: white !important; border-radius: 4px !important;
        border: none !important; width: 100% !important; font-weight: bold !important; padding: 10px !important; text-transform: uppercase;
    }
    .stTextInput input, .stTextArea textarea { background-color: #333 !important; color: white !important; border: 1px solid #444 !important; }
</style>
""", unsafe_allow_html=True)

# ===== LÓGICA DE ACESSO (CORE) =====
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    pagamentos.exibir_login()
    st.stop()

# ===== NAVEGAÇÃO =====
if "agente" not in st.session_state:
    st.session_state["agente"] = None

# VITRINE PRINCIPAL
if st.session_state["agente"] is None:
    st.title("MUSEIA DIGITAL")
    st.markdown("### Agentes Originais, Séries de Produtividade.")
    st.markdown("## Populares na MuseIA")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><div class="card-title">🏆<br>DEEP SCAN</div><p>Espionagem Industrial Ética</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 04"):
            st.session_state["agente"] = "deepscan"; st.rerun()

    with col2:
        st.markdown('<div class="card"><div class="card-title">📑<br>CURRÍCULOS</div><p>Triagem de Talentos em Massa</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 31"):
            st.session_state["agente"] = "curriculos"; st.rerun()

    with col3:
        st.markdown('<div class="card"><div class="card-title">📧<br>HUMANIZADOR</div><p>Respostas Anti-Robô</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 13"):
            st.session_state["agente"] = "humanizador"; st.rerun()

# ÁREA DE EXECUÇÃO DO AGENTE
else:
    if st.button("← Voltar para o Catálogo"):
        st.session_state["agente"] = None; st.rerun()
    
    st.markdown("---")

    if st.session_state["agente"] == "deepscan":
        st.title("🏆 Deep Scan | Agente 04")
        url = st.text_input("URL do alvo")
        if st.button("INICIAR ESCANEAMENTO"):
            texto = scraping.extrair_dados_site(url)
            resultado = ia.analisar_concorrente(texto)
            st.markdown(resultado)

    elif st.session_state["agente"] == "curriculos":
        st.title("📑 Filtro de Currículos | Agente 31")
        arquivos = st.file_uploader("Suba os PDFs", accept_multiple_files=True)
        if arquivos and st.button("GERAR RANKING"):
            texto_extraido = pdf.processar_multiplos_pdfs(arquivos)
            resultado = ia.classificar_curriculos(texto_extraido)
            st.markdown(resultado)

    elif st.session_state["agente"] == "humanizador":
        st.title("📧 Humanizador Anti-Robô | Agente 13")
        texto_bruto = st.text_area("Mensagem do lead")
        if st.button("HUMANIZAR"):
            resposta = ia.humanizar_texto(texto_bruto)
            st.info(resposta)
