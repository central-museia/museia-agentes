import streamlit as st

# 1. Configuração de Página (Deve ser a primeira linha)
st.set_page_config(page_title="MuseIA Digital | Netflix Edition", layout="wide", page_icon="🟣")

# ===== ESTILO CSS CUSTOMIZADO (NETFLIX STYLE) =====
st.markdown("""
<style>
    /* Fundo principal e fontes */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Esconder o menu padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Títulos estilo Netflix */
    h1 {
        color: #E50914; /* Vermelho Netflix */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    h2, h3 {
        color: #ffffff;
        font-weight: 300;
    }

    /* Estilização dos Cards */
    .card {
        background-color: #141414;
        border: 1px solid #333;
        padding: 40px 20px;
        border-radius: 8px;
        text-align: center;
        transition: transform .3s; /* Efeito de zoom */
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 10px;
    }
    .card:hover {
        transform: scale(1.05);
        border-color: #E50914;
        background-color: #181818;
    }
    
    .card-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Botões Customizados */
    div.stButton > button {
        background-color: #E50914 !important;
        color: white !important;
        border-radius: 4px !important;
        border: none !important;
        width: 100% !important;
        font-weight: bold !important;
        padding: 10px !important;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        background-color: #ff0f1b !important;
        box-shadow: 0px 0px 15px 5px rgba(229, 9, 20, 0.4);
    }

    /* Input Fields */
    .stTextInput input, .stTextArea textarea {
        background-color: #333 !important;
        color: white !important;
        border: 1px solid #444 !important;
    }
</style>
""", unsafe_allow_html=True)

# ===== LÓGICA DE LOGIN =====
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    col_l1, col_l2, col_l3 = st.columns([1,2,1])
    with col_l2:
        st.title("🍿 Entrar na MuseIA")
        token = st.text_input("Digite seu Token de Acesso", type="password")
        if st.button("ASSISTIR AGORA"):
            if token == "teste123":
                st.session_state["logado"] = True
                st.rerun()
            else:
                st.error("Token inválido. Verifique sua assinatura.")
    st.stop()

# ===== HEADER PRINCIPAL =====
st.title("MUSEIA DIGITAL")
st.markdown("### Agentes Originais, Séries de Produtividade.")

# ===== VITRINE DE AGENTES (GRID) =====
if "agente" not in st.session_state:
    st.session_state["agente"] = None

# Só mostra a vitrine se nenhum agente estiver selecionado
if st.session_state["agente"] is None:
    st.markdown("## Populares na MuseIA")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><div class="card-title">🏆<br>DEEP SCAN</div><p>Espionagem Industrial Ética</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 04"):
            st.session_state["agente"] = "deepscan"
            st.rerun()

    with col2:
        st.markdown('<div class="card"><div class="card-title">📑<br>CURRÍCULOS</div><p>Triagem de Talentos em Massa</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 31"):
            st.session_state["agente"] = "curriculos"
            st.rerun()

    with col3:
        st.markdown('<div class="card"><div class="card-title">📧<br>HUMANIZADOR</div><p>Respostas Anti-Robô</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Agente 13"):
            st.session_state["agente"] = "humanizador"
            st.rerun()

# ===== ÁREA DOS AGENTES (DETALHES) =====
if st.session_state["agente"]:
    if st.button("← Voltar para o Catálogo"):
        st.session_state["agente"] = None
        st.rerun()
    
    st.markdown("---")

    # 1 - DEEP SCAN
    if st.session_state["agente"] == "deepscan":
        st.title("🏆 Deep Scan | Agente 04")
        url = st.text_input("Insira a URL do alvo para o Raio-X")
        if st.button("INICIAR ESCANEAMENTO"):
            st.info("Processando dados do concorrente...")
            # Aqui entrará sua lógica de Scraping com BeautifulSoup

    # 2 - CURRÍCULOS
    elif st.session_state["agente"] == "curriculos":
        st.title("📑 Filtro de Currículos | Agente 31")
        arquivos = st.file_uploader("Arraste os currículos (PDF) aqui", accept_multiple_files=True)
        if arquivos and st.button("GERAR RANKING"):
            st.success(f"Analisando {len(arquivos)} candidatos...")

    # 3 - HUMANIZADOR
    elif st.session_state["agente"] == "humanizador":
        st.title("📧 Humanizador Anti-Robô | Agente 13")
        texto = st.text_area("Cole a mensagem bruta do lead/cliente")
        if st.button("TRANSFORMAR EM RESPOSTA HUMANA"):
            st.markdown("#### Sugestão MuseIA:")
            import requests

def gerar_resposta(texto):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBCvWULn1WFVil-WIpNDvivZcFE2oSt-Mw"

    prompt = f"""
    Você é um especialista em comunicação humana.

    Transforme a mensagem abaixo em 3 versões:
    1. Formal
    2. Amigável
    3. Direta

    Mensagem:
    {texto}
    """

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Erro ao gerar resposta"
