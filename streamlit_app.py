import streamlit as st
from nocodb.catalogo import obter_catalogo, obter_perfis, obter_colecoes
from auth.auth_museia import renderizar_interface_login

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="MuseIA Digital", layout="wide", initial_sidebar_state="collapsed")

# Estados de Sessão
if "logado" not in st.session_state: st.session_state.logado = False
if "mostrar_auth" not in st.session_state: st.session_state.mostrar_auth = False

# Carregamento de Dados (Importações corrigidas)
colecoes_db = obter_colecoes()
perfis_db = obter_perfis()
agentes_db = obter_catalogo()

# HEADER
col_logo, col_busca, col_login = st.columns([1, 2, 1])
with col_logo:
    st.image("assets/logo.png", width=120)
with col_busca:
    termo = st.text_input("🔍", placeholder="O que vamos automatizar?", label_visibility="collapsed")
with col_login:
    if not st.session_state.logado:
        if st.button("Área do Cliente 🔐", use_container_width=True):
            st.session_state.mostrar_auth = not st.session_state.mostrar_auth
    else:
        st.write(f"Olá, {st.session_state.usuario.get('nome')}")
        if st.button("Sair"):
            st.session_state.logado = False
            st.rerun()

# INTERFACE DE LOGIN (Apenas se solicitado)
if st.session_state.mostrar_auth and not st.session_state.logado:
    renderizar_interface_login()

# VITRINE DE AGENTES
st.title("MuseIA")
st.markdown("---")

if agentes_db:
    agentes_filtrados = [a for a in agentes_db if not termo or termo.lower() in a['nome'].lower()]
    cols = st.columns(4)
    for idx, agente in enumerate(agentes_filtrados):
        with cols[idx % 4]:
            st.image(agente.get('imagem', "assets/logo.png"), use_container_width=True)
            st.subheader(agente['nome'])
            if st.button("🚀 Usar Agente", key=f"run_{idx}"):
                if st.session_state.logado:
                    st.success(f"Iniciando {agente['nome']}...")
                else:
                    st.warning("Acesse sua conta para usar.")
                    st.session_state.mostrar_auth = True
                    st.rerun()

st.divider()
st.markdown("<center>MuseIA Digital 2026</center>", unsafe_allow_html=True)
