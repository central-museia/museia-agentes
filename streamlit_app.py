import streamlit as st
from nocodb.catalogo import obter_catalogo, obter_perfis, obter_colecoes
from auth.auth_museia import renderizar_interface_login

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="MuseIA Digital", layout="wide", initial_sidebar_state="collapsed")

# Inicialização de Estados
if "logado" not in st.session_state:
    st.session_state.logado = False
if "mostrar_auth" not in st.session_state:
    st.session_state.mostrar_auth = False

# --- ESTILO CSS ---
st.markdown("""
<style>
    .big-title { font-size: 55px; font-weight: bold; text-align: center; margin-bottom: 0px; }
    .sub { text-align: center; font-size: 20px; opacity: 0.8; margin-bottom: 40px; }
    .card-perfil {
        padding: 20px; border-radius: 15px; text-align: center;
        background-color: #1e2130; border: 1px solid #3e4259;
        min-height: 250px; display: flex; flex-direction: column; align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# --- CARREGAMENTO DE DADOS ---
colecoes_db = obter_colecoes()
perfis_db = obter_perfis()
agentes_db = obter_catalogo()

# --- SEÇÃO 1: HEADER (Logo, Busca, Login) ---
col_logo, col_busca, col_login = st.columns([1, 2, 1])

with col_logo:
    st.image("assets/logo.png", width=120) 

with col_busca:
    # Busca com Lupa
    termo_busca = st.text_input("🔍", placeholder="O que você deseja automatizar?", label_visibility="collapsed")

with col_login:
    if not st.session_state.logado:
        if st.button("👤 Entrar / Cadastrar", use_container_width=True):
            st.session_state.mostrar_auth = not st.session_state.mostrar_auth
    else:
        st.success(f"Olá, {st.session_state.usuario['nome_completo'].split()[0]}!")

# Exibição da Área de Login Separada (Se acionada)
if st.session_state.mostrar_auth and not st.session_state.logado:
    st.divider()
    renderizar_interface_login()
    st.divider()

# --- SEÇÃO 2: HERO ---
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

# --- SEÇÃO 3: MOSAICO DE COLEÇÕES ---
st.divider()
st.subheader("🌐 Um Ecossistema de Automação ao Seu Alcance")
if colecoes_db:
    cols_m = st.columns(5)
    for i, col in enumerate(colecoes_db):
        with cols_m[i % 5]:
            # Mantendo foco funcional (sem travar por falta de imagem)
            if col.get('imagem'):
                st.image(col['imagem'], use_container_width=True)
            st.markdown(f"<div style='text-align:center; font-weight:bold;'>{col['nome']}</div>", unsafe_allow_html=True)

# --- SEÇÃO 4: PERFIS ---
st.divider()
st.header("👤 Escolha Seu Perfil e Descubra Suas Soluções")
if perfis_db:
    cols_p = st.columns(4)
    for i, perfil in enumerate(perfis_db):
        with cols_p[i % 4]:
            with st.container():
                st.markdown(f"""<div class="card-perfil"><h4>{perfil['nome']}</h4>
                <p style="font-size: 13px;">{perfil['descricao'][:100]}...</p></div>""", unsafe_allow_html=True)
                if st.button(f"Ver Soluções", key=f"btn_perf_{perfil['codigo']}", use_container_width=True):
                    st.session_state.filtro_selecionado = perfil['nome']

# --- SEÇÃO 5: CATÁLOGO DE AGENTES (Com Filtro de Busca e Login) ---
st.divider()
st.header("🚀 Navegue por Nossas Coleções")

opcoes_colecoes = [c['nome'] for c in colecoes_db]
filtro_inicial = [st.session_state.filtro_selecionado] if "filtro_selecionado" in st.session_state else []

selecao = st.multiselect("Filtre os agentes por categoria:", opcoes_colecoes, default=filtro_inicial)

if agentes_db:
    # Lógica de Filtro Duplo: Multiselect + Busca do Header
    agentes_filtrados = [
        a for a in agentes_db 
        if (not selecao or any(c in a['colecoes'] or c in a['perfis'] for c in selecao))
        and (not termo_busca or termo_busca.lower() in a['nome'].lower() or termo_busca.lower() in a['descricao'].lower())
    ]

    if agentes_filtrados:
        cols_ag = st.columns(4)
        for idx, agente in enumerate(agentes_filtrados):
            with cols_ag[idx % 4]:
                # Vitrine sempre visível
                st.image(agente['imagem'] if agente['imagem'] else "assets/logo.png", use_container_width=True)
                st.markdown(f"**{agente['nome']}**")
                
                # Bloqueio de Utilização (Somente Logados)
                if st.button("🚀 Usar Agente", key=f"run_{agente['codigo']}", use_container_width=True):
                    if st.session_state.logado:
                        st.success(f"Iniciando {agente['nome']}...")
                        # Aqui entra o redirect para o robô
                    else:
                        st.warning("Acesse sua conta para utilizar este agente.")
                        st.session_state.mostrar_auth = True
                        st.rerun()
    else:
        st.info("Nenhum agente encontrado para sua busca.")

# --- FAQ & FOOTER (Mantidos conforme original) ---
st.divider()
st.markdown("<div style='text-align: center; opacity: 0.7;'>MuseIA Digital 2026</div>", unsafe_allow_html=True)
