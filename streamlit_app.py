import streamlit as st

st.set_page_config(page_title="MuseIA Digital", layout="wide")

# ===== ESTILO =====
st.markdown("""
<style>
body { background-color: #0f172a; }
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ===== LOGIN =====
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    st.title("🔐 Acesso MuseIA Digital")
    token = st.text_input("Digite seu token", type="password")

    if st.button("Entrar"):
        if token == "teste123":
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("Token inválido")

    st.stop()

# ===== HEADER =====
st.title("🚀 MuseIA Digital")
st.subheader("Central de Agentes Inteligentes")

# ===== MENU =====
st.markdown("## Escolha seu agente")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">🏆 Deep Scan</div>', unsafe_allow_html=True)
    if st.button("Acessar Deep Scan"):
        st.session_state["agente"] = "deepscan"

with col2:
    st.markdown('<div class="card">📑 Currículos</div>', unsafe_allow_html=True)
    if st.button("Acessar Currículos"):
        st.session_state["agente"] = "curriculos"

with col3:
    st.markdown('<div class="card">📧 Humanizador</div>', unsafe_allow_html=True)
    if st.button("Acessar Humanizador"):
        st.session_state["agente"] = "humanizador"

# ===== AGENTES =====

# 1 - DEEP SCAN
if st.session_state.get("agente") == "deepscan":
    st.title("🏆 Analista Deep Scan")

    url = st.text_input("Cole a URL do concorrente")

    if st.button("Analisar"):
        st.success("Análise simulada: concorrente foca em preço e público iniciante.")

# 2 - CURRÍCULOS
if st.session_state.get("agente") == "curriculos":
    st.title("📑 Filtro de Currículos")

    arquivos = st.file_uploader("Envie PDFs", accept_multiple_files=True)

    if arquivos and st.button("Analisar"):
        st.success(f"{len(arquivos)} currículos analisados com sucesso!")

# 3 - HUMANIZADOR
if st.session_state.get("agente") == "humanizador":
    st.title("📧 Humanizador Anti-Robô")

    texto = st.text_area("Cole a mensagem do cliente")

    if st.button("Gerar respostas"):
        st.write("### Formal")
        st.write("Prezado cliente, entendemos sua situação.")

        st.write("### Amigável")
        st.write("Oi! Entendo totalmente 😊")

        st.write("### Direta")
        st.write("Vamos resolver isso agora.")
