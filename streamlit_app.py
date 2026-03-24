import streamlit as st

st.set_page_config(page_title="MuseIA Digital", layout="wide")

# ===== ESTILO =====
st.markdown("""
## 🚀 Central de Automação com IA

Acesse agentes prontos para gerar resultados reais no seu negócio.
""")
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
st.markdown("## 🎬 Explore os Agentes da MuseIA")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#1e293b;padding:25px;border-radius:20px;margin-bottom:20px">
        <h3>🏆 Analista de Mercado Deep Scan</h3>
        <p>Descubra como seus concorrentes posicionam ofertas, preços e público-alvo em segundos.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Acessar Deep Scan"):
        st.session_state["agente"] = "deepscan"

with col2:
    st.markdown("""
    <div style="background-color:#1e293b;padding:25px;border-radius:20px;margin-bottom:20px">
        <h3>📑 Filtro Inteligente de Currículos</h3>
        <p>Analise dezenas de currículos automaticamente e receba um ranking pronto.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Acessar Currículos"):
        st.session_state["agente"] = "curriculos"


col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div style="background-color:#1e293b;padding:25px;border-radius:20px;margin-bottom:20px">
        <h3>📧 Humanizador Anti-Robô</h3>
        <p>Transforme respostas frias em mensagens naturais e humanas.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Acessar Humanizador"):
        st.session_state["agente"] = "humanizador"
