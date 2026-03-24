import streamlit as st

st.set_page_config(
    page_title="MuseIA",
    layout="wide"
)

# --- ESTILO ---
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
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
.cta button {
    background-color: #22C55E !important;
    color: white !important;
    border-radius: 10px !important;
    height: 60px !important;
    font-size: 18px !important;
}
.card {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-weight:bold;
    margin:10px;
}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown('<div class="big-title">MuseIA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A inteligência humana que controla a IA</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Quero dominar a IA agora"):
        st.success("Você está a um clique da sua nova realidade.")

with col2:
    if st.button("🔥 Ver todos os agentes"):
        st.info("Prepare-se. Isso muda tudo.")

st.divider()

# --- PROPOSTA ---
st.header("🔥 O que você ganha com a MuseIA?")
st.write("Produtividade absurda. Clareza. Estratégia. Execução. Tudo no piloto automático inteligente.")

# --- FUNÇÃO DE CARDS ---
def card(nome, cor):
    st.markdown(f'<div class="card" style="background:{cor}">{nome}</div>', unsafe_allow_html=True)

# --- GROWTH ---
st.header("🚀 Growth")
cols = st.columns(3)
with cols[0]: card("Prospecção de Vendas", "#16A34A")
with cols[1]: card("Assistente de E-mail", "#22C55E")
with cols[2]: card("Conteúdo Multicanal", "#84CC16")

# --- BI ---
st.header("📊 Business Intelligence")
cols = st.columns(3)
with cols[0]: card("Pesquisa de Mercado", "#2563EB")
with cols[1]: card("Inteligência de Pesquisa", "#1D4ED8")
with cols[2]: card("Notícias do Setor", "#0EA5E9")

# --- GESTÃO ---
st.header("🧠 Gestão & Cultura")
cols = st.columns(4)
with cols[0]: card("Feedback do Cliente", "#7C3AED")
with cols[1]: card("Voz da Marca", "#9333EA")
with cols[2]: card("Eventos", "#A855F7")
with cols[3]: card("RH no Slack", "#C084FC")

# --- MARKETING ---
st.header("🎯 Marketing")
card("Criador de Conteúdo", "#F97316")

st.divider()

# --- CTA FINAL ---
st.header("💡 Ainda está pensando?")

col1, col2 = st.columns(2)

with col1:
    if st.button("💥 Isso era exatamente o que me faltava"):
        st.success("Bem-vindo à evolução.")

with col2:
    if st.button("🧠 Quero evoluir agora"):
        st.success("Você não está comprando… está evoluindo.")

st.divider()

# --- FAQ ---
st.header("❓ Dúvidas Frequentes")

with st.expander("Isso é só mais uma IA?"):
    st.write("Não. É estratégia aplicada com inteligência humana.")

with st.expander("Preciso saber tecnologia?"):
    st.write("Zero. A MuseIA simplifica tudo.")

with st.expander("Funciona pra qualquer negócio?"):
    st.write("Sim. Se você precisa crescer, funciona.")

with st.expander("É acesso imediato?"):
    st.write("Sim. Comprou, começou.")

# --- FOOTER ---
st.markdown("---")
st.markdown("MuseIA © 2026 — Revolucionando a forma de pensar, criar e vender.")
