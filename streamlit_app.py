import streamlit as st

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

# --- MULTISELECT COM KEY ---
selecionadas = st.multiselect(
    "Selecione suas coleções:",
    list(colecoes.keys()),
    default=st.session_state.colecoes,
    key="multiselect_colecoes"
)

# --- ATUALIZA ESTADO ---
st.session_state.colecoes = selecionadas

st.divider()

# --- EXIBIÇÃO ---
if st.session_state.colecoes:

    st.subheader("📦 Sua estrutura escolhida:")

    cols = st.columns(3)

    for i, nome in enumerate(st.session_state.colecoes):
        with cols[i % 3]:
            st.markdown(
                f'<div class="card" style="background:{colecoes[nome]}">{nome}</div>',
                unsafe_allow_html=True
            )

    st.divider()

    st.header("🚀 Agora sim, você está jogando sério.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔥 Ativar minha estrutura"):
            st.success("Sistema ativado. Você desbloqueou outro nível.")

    with col2:
        if st.button("🧠 Montar solução completa"):
            st.info("Você não está comprando. Está construindo vantagem.")

else:
    st.warning("⚠️ Escolha pelo menos uma coleção para avançar.")

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
