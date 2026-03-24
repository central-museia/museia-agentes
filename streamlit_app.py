import streamlit as st

# 1. CONFIGURAÇÃO DE PÁGINA (Sempre a primeira)
st.set_page_config(page_title="MuseIA Digital", layout="wide", page_icon="🟣")

# 2. TENTATIVA DE IMPORTAÇÃO DAS CAMADAS (BLINDAGEM)
# Se a pasta ou arquivo não existir, o site NÃO QUEBRA.
try:
    from core import pagamentos
except Exception:
    class pagamentos: 
        @staticmethod
        def exibir_login(): st.warning("⚠️ Módulo de Login (core/pagamentos.py) não encontrado.")

try:
    from utils import ia, scraping
except Exception:
    class ia:
        @staticmethod
        def humanizar_texto(t): return "⚠️ Erro: Módulo 'utils/ia.py' ausente."
    class scraping:
        @staticmethod
        def extrair_dados_site(u): return "Conteúdo indisponível (Erro no script de scraping)."

# 3. ESTILO CSS (NETFLIX DARK)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    #MainMenu, footer, header {visibility: hidden;}
    h1 { color: #E50914; font-family: 'Arial Black'; text-transform: uppercase; }
    .card {
        background-color: #141414; border: 1px solid #333; padding: 25px; border-radius: 8px;
        text-align: center; transition: 0.3s; min-height: 150px;
    }
    .card:hover { transform: scale(1.03); border-color: #E50914; }
    div.stButton > button {
        background-color: #E50914 !important; color: white !important; font-weight: bold !important;
        width: 100% !important; border: none !important; padding: 10px !important;
    }
    .stTextInput input, .stTextArea textarea { background-color: #333 !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

# 4. SISTEMA DE ACESSO
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    pagamentos.exibir_login()
    # Botão de emergência caso o arquivo pagamentos.py suma
    if st.button("DESBLOQUEIO DE EMERGÊNCIA (TESTE)"):
        st.session_state["logado"] = True
        st.rerun()
    st.stop()

# 5. VITRINE E NAVEGAÇÃO
if "agente" not in st.session_state:
    st.session_state["agente"] = None

if st.session_state["agente"] is None:
    st.title("MUSEIA DIGITAL")
    st.markdown("### Séries de Produtividade")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🏆 DEEP SCAN</h3><p>Agente 04</p></div>', unsafe_allow_html=True)
        if st.button("ACESSAR 04"): st.session_state["agente"] = "deepscan"; st.rerun()
    with col2:
        st.markdown('<div class="card"><h3>📑 CURRÍCULOS</h3><p>Agente 31</p></div>', unsafe_allow_html=True)
        if st.button("ACESSAR 31"): st.session_state["agente"] = "curriculos"; st.rerun()
    with col3:
        st.markdown('<div class="card"><h3>📧 HUMANIZADOR</h3><p>Agente 13</p></div>', unsafe_allow_html=True)
        if st.button("ACESSAR 13"): st.session_state["agente"] = "humanizador"; st.rerun()

# 6. EXECUÇÃO DOS AGENTES
else:
    if st.button("← VOLTAR"):
        st.session_state["agente"] = None
        st.rerun()

    if st.session_state["agente"] == "humanizador":
        st.title("📧 Humanizador Anti-Robô")
        texto = st.text_area("Mensagem:")
        if st.button("GERAR"):
            # Aqui ele tenta usar a camada utils/ia.py, mas se ela falhar, 
            # o site apenas mostra o aviso em vez de travar tudo.
            resultado = ia.humanizar_texto(texto)
            st.info(resultado)

    elif st.session_state["agente"] == "deepscan":
        st.title("🏆 Deep Scan")
        url = st.text_input("URL:")
        if st.button("ESCANEAR"):
            conteudo = scraping.extrair_dados_site(url)
            st.write(conteudo)
