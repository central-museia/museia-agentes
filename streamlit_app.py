import streamlit as st
from nocodb.catalogo import obter_catalogo, obter_perfis, obter_colecoes

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="MuseIA Digital", layout="wide", initial_sidebar_state="collapsed")

# --- ESTILO CSS (Mantendo sua identidade visual e cartões) ---
st.markdown("""
<style>
    .big-title { font-size: 55px; font-weight: bold; text-align: center; margin-bottom: 0px; }
    .sub { text-align: center; font-size: 20px; opacity: 0.8; margin-bottom: 40px; }
    .card-perfil {
        padding: 20px; border-radius: 15px; text-align: center;
        background-color: #1e2130; border: 1px solid #3e4259;
        height: 220px; display: flex; flex-direction: column; justify-content: center;
    }
    .mosaico-item {
        text-align: center; padding: 15px; border-radius: 10px;
        font-weight: bold; color: white; margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- SEÇÃO 1: HEADER ---
col_logo, col_vazio, col_login = st.columns([1, 2, 1])
with col_logo:
    st.image("assets/logo.png", width=120) # Certifique-se que o arquivo existe na pasta assets
with col_login:
    if st.button("👤 Acessar Minha Área"):
        st.toast("Área do cliente em desenvolvimento!")

# --- SEÇÃO 2: HERO & SLIDESHOW (Propaganda) ---
st.markdown('<div class="big-title">MuseIA</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">A inteligência humana que controla a IA</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🎁 KIT Gratuito", "⚡ Automação Rápida"])
with tab1:
    st.markdown("""
    <div style="background: linear-gradient(90deg, #14B8A6, #0EA5E9); padding: 30px; border-radius: 15px; color: white;">
        <h2>Kit Inicial MuseIA</h2>
        <p>Organize tarefas, responda mensagens e ganhe tempo sem entender de tecnologia.</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("Acessar KIT Gratuito 🚀", key="btn_kit")

# --- SEÇÃO 3: MOSAICO (Amplitude) ---
st.divider()
st.subheader("🌐 Um Ecossistema de Automação ao Seu Alcance")
colecoes_db = obter_colecoes()
if colecoes_db:
    cols_m = st.columns(5)
    for i, col in enumerate(colecoes_db):
        with cols_m[i % 5]:
            st.markdown(f"""
            <div class="mosaico-item" style="background-color: {col['cor']}; border: 1px solid white;">
                {col['nome']}
            </div>
            """, unsafe_allow_html=True)

# --- SEÇÃO 4: PERFIS (Jornada do Cliente) ---
st.divider()
st.header("👤 Escolha Seu Perfil e Descubra Suas Soluções")
perfis_db = obter_perfis()

if perfis_db:
    cols_p = st.columns(4)
    for i, perfil in enumerate(perfis_db):
        with cols_p[i % 4]:
            st.markdown(f"""
            <div class="card-perfil">
                <h4>{perfil['nome']}</h4>
                <p style="font-size: 13px;">{perfil['descricao'][:120]}...</p>
            </div>
            """, unsafe_allow_html=True)
            # Ao clicar, filtramos as coleções (lógica simplificada para exemplo)
            if st.button(f"Ver Soluções", key=f"btn_perf_{perfil['codigo']}"):
                st.session_state.filtro_manual = perfil['nome']

# --- SEÇÃO 5: O CORAÇÃO (Catálogo e Coleções) ---
st.divider()
st.header("🚀 Navegue por Nossas Coleções")

# Multiselect dinâmico
opcoes_colecoes = [c['nome'] for c in colecoes_db]
selecao = st.multiselect("Selecione para filtrar os agentes:", opcoes_colecoes)

agentes_db = obter_catalogo()

if selecao:
    cols_ag = st.columns(4)
    idx = 0
    for agente in agentes_db:
        # Filtro: O agente precisa estar em uma das coleções selecionadas
        if any(c in agente['colecoes'] for c in selecao) or any(c in agente['perfis'] for c in selecao):
            with cols_ag[idx % 4]:
                if agente['imagem']:
                    st.image(agente['imagem'], use_container_width=True)
                else:
                    st.image("assets/logo.png", width=150)
                
                st.markdown(f"**{agente['nome']}**")
                st.caption(f"Código: {agente['codigo']}")
                
                if st.button("🚀 Usar Agente", key=f"run_{agente['codigo']}"):
                    st.session_state.agente_atual = agente['codigo']
                    st.info("Validando sua assinatura para liberar o acesso...")
            idx += 1
else:
    st.info("💡 Escolha uma coleção ou perfil acima para visualizar os agentes disponíveis.")

# --- SEÇÃO 7: FAQ (Seus textos originais) ---
st.divider()
st.header("❓ Dúvidas Frequentes")
faqs = [
    ("Isso é só mais uma IA?", "Não. É execução estratégica com inteligência."),
    ("Funciona pra qualquer negócio?", "Sim. Se precisa crescer, funciona."),
    ("Preciso saber usar IA?", "Não. A MuseIA já pensa por você.")
]
for pergunta, resposta in faqs:
    with st.expander(pergunta):
        st.write(resposta)

# --- SEÇÃO 8: FOOTER ---
st.divider()
st.markdown("""
<div style="text-align: center; opacity: 0.7;">
    <p>MuseIA Digital 2026 - A Inteligência Humana que controla a IA</p>
    <p style="font-size: 12px;">Termos de Uso | Política de Privacidade | Suporte</p>
</div>
""", unsafe_allow_html=True)
