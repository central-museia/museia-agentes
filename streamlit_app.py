import streamlit as st

st.set_page_config(page_title="MuseIA", layout="wide")

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

# --- PROPOSTA ---
st.header("🔥 Você não precisa de mais ferramentas.")
st.subheader("Você precisa de decisões inteligentes sendo executadas por você.")

st.write("Escolha a coleção que resolve exatamente o seu problema agora:")

# --- COLEÇÕES ---
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

selecionadas = st.multiselect(
    "Escolha suas coleções:",
    list(colecoes.keys())
)

# --- EXIBIÇÃO ---
if selecionadas:
    st.subheader("📦 Sua seleção estratégica:")

    cols = st.columns(3)
    for i, nome in enumerate(selecionadas):
        with cols[i % 3]:
            st.markdown(
                f'<div class="card" style="background:{colecoes[nome]}">{nome}</div>',
                unsafe_allow_html=True
            )

    st.divider()

    st.header("🚀 Você está a um passo de destravar isso:")

    st.write("Automação + Clareza + Execução = Resultado real")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔥 Quero ativar essas coleções agora"):
            st.success("Decisão tomada. Agora você joga em outro nível.")

    with col2:
        if st.button("🧠 Montar minha estrutura completa"):
            st.info("Você está montando um sistema, não comprando um produto.")

else:
    st.info("Selecione pelo menos uma coleção para avançar.")

st.divider()

# --- FAQ ---
st.header("❓ Dúvidas Frequentes")

with st.expander("Isso substitui ferramentas?"):
    st.write("Sim. E mais importante: substitui confusão por clareza.")

with st.expander("Funciona pra meu tipo de negócio?"):
    st.write("Se você precisa organizar, vender ou escalar… funciona.")

with st.expander("Preciso saber usar IA?"):
    st.write("Não. A MuseIA já pensa por você.")

with st.expander("É acesso imediato?"):
    st.write("Sim. Entrou, começou.")

# --- FOOTER ---
st.markdown("---")
st.markdown("MuseIA © 2026 — Inteligência aplicada que gera resultado.")
