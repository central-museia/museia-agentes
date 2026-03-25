import streamlit as st
from nocodb.catalogo import obter_catalogo

# 1. CONFIGURAÇÃO (Mantida)
st.set_page_config(page_title="MuseIA - Central", layout="wide")

# --- ESTADO (Mantido) ---
if "colecoes" not in st.session_state:
    st.session_state.colecoes = []

# --- ESTILO (Evoluído para suportar os novos Cards) ---
st.markdown("""
<style>
    .big-title { font-size: 50px; font-weight: bold; text-align: center; margin-bottom: 0; }
    .sub { text-align: center; font-size: 18px; opacity: 0.7; margin-bottom: 30px; }
    .card-perfil {
        padding: 25px; border-radius: 15px; text-align: center;
        background-color: #1e2130; border: 1px solid #3e4259;
        margin-bottom: 15px; transition: 0.3s;
    }
    .card-perfil:hover { border-color: #ff4b4b; }
    .section-header { margin-top: 50px; margin-bottom: 20px; font-size: 28px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. HERO & IMPACTO (Conforme seu modelo) ---
col_logo, col_vazio = st.columns([1, 4])
with col_logo:
    st.image("assets/logo.png", width=120)

st.markdown('<div class="big-title">MuseIA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A inteligência humana que controla a IA</div>', unsafe_allow_html=True)

# --- NOVO: SEÇÃO DE PERFIS (Antes das coleções) ---
st.markdown('<div class="section-header">👤 Escolha seu perfil de atuação:</div>', unsafe_allow_html=True)
cp1, cp2, cp3 = st.columns(3)

with cp1:
    st.markdown('<div class="card-perfil"><h3>Empreendedor</h3><p>Gestão de tempo e escala de negócio.</p></div>', unsafe_allow_html=True)
    if st.button("Focar em Empreendedorismo", key="p_emp"):
        st.session_state.colecoes = ["Produtividade Administrativa", "Financeiro & Cobrança"]
        st.rerun()

with cp2:
    st.markdown('<div class="card-perfil"><h3>Gestor Ops</h3><p>Relatórios, RH e eficiência operacional.</p></div>', unsafe_allow_html=True)
    if st.button("Focar em Gestão", key="p_ges"):
        st.session_state.colecoes = ["Planejamento & Operações", "Recursos Humanos"]
        st.rerun()

with cp3:
    st.markdown('<div class="card-perfil"><h3>Especialista</h3><p>Vendas, Marketing e Prospecção ativa.</p></div>', unsafe_allow_html=True)
    if st.button("Focar em Vendas", key="p_esp"):
        st.session_state.colecoes = ["Vendas & Prospecção", "Marketing & Conteúdo"]
        st.rerun()

st.divider()

# --- 3. SEÇÃO DE COLEÇÕES (Sua lógica original preservada) ---
st.header("🔥 Explore por Coleções:")

colecoes_cores = {
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

# MULTISELECT (Agora atualizado pelos botões de perfil também!)
selecionadas = st.multiselect(
    "Filtre as soluções desejadas:",
    list(colecoes_cores.keys()),
    default=st.session_state.colecoes,
    key="multiselect_colecoes"
)
st.session_state.colecoes = selecionadas

# --- 4. EXIBIÇÃO DE AGENTES (Sua lógica original preservada) ---
catalogo = obter_catalogo()

if st.session_state.colecoes:
    st.markdown(f'<div class="section-header">🎬 Agentes disponíveis ({len(st.session_state.colecoes)} áreas):</div>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    grid_index = 0

    for agente in catalogo:
        # Lógica de filtro preservada
        if agente.get("colecoes"):
            if not any(c in agente["colecoes"] for c in st.session_state.colecoes):
                continue
        
        with cols[grid_index % 4]:
            # Container do Agente
            st.image(agente.get("imagem", "assets/logo.png"), use_container_width=True)
            st.markdown(f"**{agente['nome']}**")
            st.caption(f"ID: {agente['codigo']}")
            
            # VALIDAÇÃO DE ACESSO (Onde você pediu)
            if st.button("🚀 Usar agente", key=f"btn_{agente['codigo']}"):
                # Aqui entra o campo de e-mail para validar
                email = st.text_input("E-mail de assinante:", key=f"mail_{agente['codigo']}")
                if email:
                    st.success(f"Acesso validado para {email}! Iniciando...")
                else:
                    st.info("Insira seu e-mail para validar o plano.")
        
        grid_index += 1
else:
    st.info("💡 Dica: Selecione um Perfil acima ou escolha as coleções para ver as soluções.")

# --- 5. SEÇÕES FINAIS (FAQ e CTA - Preservados e Estilizados) ---
st.divider()
col_cta1, col_cta2 = st.columns(2)
with col_cta1:
    st.header("🚀 Pronto para o próximo nível?")
    if st.button("🔥 Ativar minha estrutura completa"):
        st.balloons()

with col_cta2:
    st.header("🧠 Dúvidas?")
    with st.expander("Como funciona o pagamento?"):
        st.write("A liberação é automática via e-mail cadastrado no checkout.")

# FOOTER
st.markdown("<br><hr><center>MuseIA © 2026 — Inteligência Aplicada</center>", unsafe_allow_html=True)

