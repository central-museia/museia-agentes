import streamlit as st

st.set_page_config(page_title="MuseIA", layout="centered")

# --- CSS LIMPO (ESTILO LOJA) ---
st.markdown("""
<style>
.block-container {
    max-width: 700px;
}
h1 {
    font-size: 32px;
}
.price {
    font-size: 28px;
    font-weight: bold;
}
.buy-btn button {
    width: 100%;
    height: 55px;
    font-size: 18px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("Novos Agentes de Automação disponíveis")
st.caption("Implemente IA generativa no seu dia")

st.divider()

# --- BUSCA (igual vibe Payhip simples) ---
st.text_input("O que você está procurando?")

st.divider()

# --- COPY DIRETA ---
st.write("""
Pare de perder tempo com tarefas repetitivas.

Use automações simples e recupere horas do seu dia com a MuseIA.
""")

# --- CTA PRINCIPAL ---
if st.button("🚀 Comece agora gratuitamente"):
    st.success("Você começou.")

st.divider()

# --- PRODUTO (ESTILO PAYHIP) ---
st.header("Kit Inicial MuseIA")

st.markdown("""
Seu primeiro passo para automatizar seu dia sem precisar entender tecnologia.

- Organize tarefas automaticamente  
- Responda mensagens com mais agilidade  
- Evite esquecimentos e retrabalho  
- Ganhe tempo no seu dia  
""")

# --- PREÇO DESTACADO ---
st.markdown('<div class="price">R$ 69,90</div>', unsafe_allow_html=True)

# --- BOTÃO DE COMPRA (PRINCIPAL) ---
if st.button("💥 Comprar agora"):
    st.success("Redirecionando para pagamento...")

st.caption("Produto digital. Acesso imediato após pagamento.")

st.divider()

# --- REPETIÇÃO (IGUAL PAYHIP) ---
st.write("""
Pare de perder tempo com tarefas repetitivas.

Use automações simples e recupere horas do seu dia com a MuseIA.
""")

if st.button("⚡ Simplificar meu dia agora"):
    st.info("Você está a um passo.")

st.divider()

# --- BENEFÍCIOS (LISTA SIMPLES, NÃO GRID) ---
st.subheader("Por que usar a MuseIA?")

st.write("""
Assinatura mensal  
Central de Agentes MuseIA  
Aceleração de Vendas  
Inteligência de Dados  
Gestão de Pessoas & Feedback  
Consistência de Marca  
""")

st.divider()

# --- FAQ ---
st.subheader("Perguntas frequentes")

with st.expander("1. O que é a MuseIA Digital?"):
    st.write("Uma Central de Agentes de Automação com instruções práticas.")

with st.expander("2. Quanto custa?"):
    st.write("R$ 69,90 ou assinatura futura de R$ 79,90.")

with st.expander("3. Onde posso usar?"):
    st.write("Em tarefas do dia a dia, vendas, marketing e organização.")

with st.expander("4. Posso cancelar?"):
    st.write("Sim.")

with st.expander("5. É seguro?"):
    st.write("Sim.")

with st.expander("6. Posso compartilhar?"):
    st.write("Uso individual recomendado.")

with st.expander("7. Preciso de suporte?"):
    st.write("Sim, disponível após compra.")

with st.expander("8. Posso denunciar conteúdo?"):
    st.write("Sim.")

st.divider()

# --- FOOTER ---
st.caption("Home • Central de Automação • Sobre a MuseIA")
st.caption("Desenvolvido por MuseIA © 2026")
