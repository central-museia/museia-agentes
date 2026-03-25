import streamlit as st
from nocodb.catalogo import obter_catalogo

# 1. CONFIGURAÇÃO (Mantida)
st.set_page_config(page_title="MuseIA", layout="wide")

# --- ESTADO (Mantido) ---
if "colecoes" not in st.session_state:
    st.session_state.colecoes = []

# --- ESTILO (Personalizado para o novo Layout) ---
st.markdown("""
<style>
.big-title { font-size: 60px; font-weight: bold; text-align: center; }
.sub { text-align: center; font-size: 20px; opacity: 0.7; }
.card-perfil {
    padding: 20px; border-radius: 15px; text-align: center;
    background-color: #1e2130; border: 1px solid #3e4259;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- HERO (Original) ---
st.image("assets/logo.png", width=180)
st.markdown('<div class="big-title">MuseIA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A inteligência humana que controla a IA</div>', unsafe_allow_html=True)

st.divider()

# --- NOVO: SEÇÃO DE PERFIS (Conforme seu novo plano de layout) ---
st.header("👤 Escolha seu perfil de atuação:")
cp1, cp2, cp3 = st.columns(3)

with cp1:
    st.markdown('<div class="card-perfil"><h3>Empreendedor</h3><p>Gestão e Escala</p></div>', unsafe_allow_html=True)
    if st.button("Ver como Empreendedor", key="p_emp"):
        st.session_state.colecoes = ["Produtividade Administrativa", "Financeiro & Cobrança"]
        st.rerun()

with cp2:
    st.markdown('<div class="card-perfil"><h3>Gestor</h3><p>Eficiência e Operações</p></div>', unsafe_allow_html=True)
    if st.button("Ver como Gestor", key="p_ges"):
        st.session_state.colecoes = ["Planejamento & Operações", "Recursos Humanos"]
        st.rerun()

with cp3:
    st.markdown('<div class="card-perfil"><h3>Especialista</h3><p>Vendas e Marketing</p></div>', unsafe_allow_html=True)
    if st.button("Ver como Especialista", key="p_esp"):
        st.session_state.colecoes = ["Vendas & Prospecção", "Marketing & Conteúdo"]
        st.rerun()

st.divider()

# --- COLEÇÕES (Original - Mantido todas as cores e chaves) ---
st.header("🔥 Escolha sua transformação:")

colecoes_dict = {
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
    "Selecione suas coleções:",
    list(colecoes_dict.keys()),
    default=st.session_state.colecoes,
    key="multiselect_colecoes"
)
st.session_state.colecoes = selecionadas

st.divider()

# --- EXIBIÇÃO DE AGENTES (Original - Lógica de grid 4 colunas) ---
catalogo = obter_catalogo()

if st.session_state.colecoes:
    st.subheader("🎬 Agentes disponíveis:")
    cols = st.columns(4)
    grid_i = 0

    for agente in catalogo:
        # Filtro de coleção original
        if agente.get("colecoes"):
            if not any(c in agente["colecoes"] for c in st.session_state.colecoes):
                continue
        
        with cols[grid_i % 4]:
            if agente.get("imagem"):
                st.image(agente["imagem"])
            else:
                st.image("assets/logo.png")

            st.markdown(f"**{agente['nome']}**")
            st.caption(agente["codigo"])

            # Botão com validação de e-mail integrada conforme combinamos
            if st.button("🚀 Usar agente", key=f"btn_{agente['codigo']}"):
                email = st.text_input("Confirme seu e-mail de acesso:", key=f"in_{agente['codigo']}")
                if email:
                    st.success(f"{agente['nome']} ativado para {email}")
        grid_i += 1
else:
    st.warning("⚠️ Escolha pelo menos uma coleção ou perfil para avançar.")

# --- CTA FINAL (Original - Mantido exatamente seus textos) ---
st.divider()
st.header("🚀 Agora sim, você está jogando sério.")

col1, col2 = st.columns(2)
with col1:
    if st.button("🔥 Ativar minha estrutura"):
        st.success("Sistema ativado. Você desbloqueou outro nível.")

with col2:
    if st.button("🧠 Montar solução completa"):
        st.info("Você não está comprando. Está construindo vantagem.")

# --- FAQ (Original - Mantido exatamente suas perguntas e respostas) ---
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

# --- FOOTER (Original) ---
st.markdown("---")
st.markdown("MuseIA © 2026 — Inteligência aplicada que gera resultado.")
