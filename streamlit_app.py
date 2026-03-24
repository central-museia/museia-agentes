import streamlit as st
from nocodb.catalogo import obter_catalogo

st.set_page_config(page_title="MuseIA", layout="wide")

# --- ESTADO ---
if "colecoes" not in st.session_state:
    st.session_state.colecoes = []

# --- ESTILO ---
st.markdown("""
<style>
.big-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
}
.sub {
    text-align: center;
    font-size: 20px;
    opacity: 0.7;
}
.card {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-weight:bold;
    margin:10px;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.image("assets/logo.png", width=180)
st.markdown('<div class="big-title">MuseIA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A inteligência humana que controla a IA</div>', unsafe_allow_html=True)

st.divider()

st.header("🔥 Escolha sua transformação:")

colecoes = {
    "Produtividade Administrativa": "#14B8A6",
    "Atendimento & Recepção": "#0EA5E9",
    "Clínicas e Consultórios": "#2563EB",
    "Salões e Estética": "#F97316",
    "Planejamento & Operações": "#1D4ED8",
    "Vendas & Prospecção": "#16A34A",
    "Marketing & Conteúdo": "#84CC16",
    "Recursos Humanos": "#9333EA",
    "Suporte ao Cliente": "#7C3AED",
    "Financeiro & Cobrança": "#22C55E"
}

# --- MULTISELECT ---
selecionadas = st.multiselect(
    "Selecione suas coleções:",
    list(colecoes.keys()),
    default=st.session_state.colecoes,
    key="multiselect_colecoes"
)

st.session_state.colecoes = selecionadas

st.divider()

# =========================================
# 📦 EXIBIÇÃO DE AGENTES (NOVO)
# =========================================

catalogo = obter_catalogo()

if st.session_state.colecoes:

    st.subheader("🎬 Agentes disponíveis:")

    cols = st.columns(4)

    for i, agente in enumerate(catalogo):

        # filtro por coleção
        if agente["colecoes"]:
            nomes_colecao = st.session_state.colecoes
            if not any(c in agente["colecoes"] for c in nomes_colecao):
                continue

        with cols[i % 4]:

            # IMAGEM (COM FALLBACK)
            if agente.get("imagem"):
                st.image(agente["imagem"])
            else:
                st.image("assets/logo.png")

            st.markdown(f"**{agente['nome']}**")
            st.caption(agente["codigo"])

            if st.button("🚀 Usar agente", key=agente["codigo"]):
                st.success(f"{agente['nome']} ativado")

else:
    st.warning("⚠️ Escolha pelo menos uma coleção para avançar.")

# --- CTA FINAL ---
st.divider()

st.header("🚀 Agora sim, você está jogando sério.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔥 Ativar minha estrutura"):
        st.success("Sistema ativado. Você desbloqueou outro nível.")

with col2:
    if st.button("🧠 Montar solução completa"):
        st.info("Você não está comprando. Está construindo vantagem.")

# --- FAQ ---
st.divider()
st.header("❓ Dúvidas Frequentes")

with st.expander("Isso é só mais uma IA?"):
    st.write("Não. É execução estratégica com inteligência.")

with st.expander("Funciona pra qualquer negócio?"):
    st.write("Sim. Se precisa crescer, funciona.")

with st.expander("Preciso saber usar IA?"):
    st.write("Não. A MuseIA já pensa por você.")

with st.expander("É imediato?"):
    st.write("Sim. Entrou, começou.")

# --- FOOTER ---
st.markdown("---")
st.markdown("MuseIA © 2026 — Inteligência aplicada que gera resultado.")
