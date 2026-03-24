import streamlit as st

st.set_page_config(page_title="MuseIA", layout="wide")

# --- ESTILO ---
st.markdown("""
<style>
.main-title {
    font-size: 48px;
    font-weight: bold;
}
.subtitle {
    font-size: 20px;
    opacity: 0.7;
}
.cta button {
    height: 60px !important;
    font-size: 18px !important;
    border-radius: 10px !important;
}
.section {
    margin-top: 40px;
}
.box {
    padding: 20px;
    border-radius: 12px;
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown('<div class="main-title">Novos Agentes de Automação disponíveis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Implemente IA generativa no seu dia</div>', unsafe_allow_html=True)

st.divider()

# --- BUSCA / PROBLEMA ---
st.subheader("🔍 O que você está procurando?")

busca = st.text_input("Ex: automatizar atendimento, vender mais, organizar tarefas...")

st.divider()

# --- PROPOSTA ---
st.markdown("""
Pare de perder tempo com tarefas repetitivas.  
Use automações simples e recupere horas do seu dia com a MuseIA.
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Começar gratuitamente"):
        st.success("Você acabou de dar o primeiro passo.")

with col2:
    if st.button("⚡ Quero simplificar meu dia agora"):
        st.info("Você está mais perto do que imagina.")

st.divider()

# --- PRODUTO ---
st.header("📦 Kit Inicial MuseIA")

st.markdown("""
Seu primeiro passo para automatizar seu dia sem precisar entender tecnologia.

✔ Organize tarefas automaticamente  
✔ Responda mensagens com mais agilidade  
✔ Evite esquecimentos e retrabalho  
✔ Ganhe tempo no seu dia  
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("💥 Quero o Kit Inicial agora"):
        st.success("Escolha inteligente. Vamos começar.")

with col2:
    if st.button("👀 Ver como funciona"):
        st.info("Simples, direto e aplicável no seu dia.")

st.divider()

# --- BENEFÍCIOS ---
st.header("🔥 Por que usar a MuseIA?")

cols = st.columns(3)

with cols[0]:
    st.markdown("### 💰 Aceleração de Vendas")
    st.write("Mais oportunidades, menos esforço manual.")

with cols[1]:
    st.markdown("### 📊 Inteligência de Dados")
    st.write("Decisões com base real, não achismo.")

with cols[2]:
    st.markdown("### 🧠 Gestão de Pessoas & Feedback")
    st.write("Organização e clareza no time.")

cols2 = st.columns(2)

with cols2[0]:
    st.markdown("### 🎯 Consistência de Marca")
    st.write("Comunicação alinhada sempre.")

with cols2[1]:
    st.markdown("### 🤖 Central de Agentes MuseIA")
    st.write("Tudo em um só lugar.")

st.divider()

# --- PLANOS ---
st.header("💳 Como funciona")

st.markdown("""
**Venda unitária:** R$ 69,90  
**Assinatura mensal (em breve):** R$ 79,90/mês  

Promoções podem aparecer a qualquer momento.
""")

if st.button("🔥 Quero garantir meu acesso"):
    st.success("Você está entrando na nova forma de trabalhar.")

st.divider()

# --- FAQ ---
st.header("❓ Perguntas frequentes")

with st.expander("1. O que é a MuseIA Digital?"):
    st.write("Uma Central de Agentes de Automação com instruções práticas para você usar sozinho.")

with st.expander("2. Quanto custa?"):
    st.write("Venda unitária: R$ 69,90. Assinatura mensal prevista: R$ 79,90.")

with st.expander("3. Onde posso usar os agentes?"):
    st.write("Em ferramentas do dia a dia como e-mail, atendimento, marketing e gestão.")

with st.expander("4. Posso cancelar a assinatura?"):
    st.write("Sim. Sem burocracia.")

with st.expander("5. É seguro?"):
    st.write("Sim. Seus dados e uso são protegidos.")

with st.expander("6. Posso compartilhar meu acesso?"):
    st.write("O ideal é uso individual para melhor desempenho.")

with st.expander("7. Preciso de suporte. Como faço?"):
    st.write("Você terá canais de suporte disponíveis após a compra.")

with st.expander("8. Posso denunciar conteúdos inadequados?"):
    st.write("Sim. Prezamos pela qualidade da plataforma.")

st.divider()

# --- FOOTER / MENU ---
st.markdown("""
Home | Central de Automação | Sobre a MuseIA
""")

st.markdown("MuseIA © 2026 — Inteligência aplicada que gera resultado.")
