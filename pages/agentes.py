import streamlit as st
from database.catalogo import obter_agentes, obter_perfis, obter_colecoes

def normalizar(texto):
    if not texto: return ""
    import unicodedata
    return unicodedata.normalize('NFKD', str(texto)).encode('ascii', 'ignore').decode('utf-8').lower()

st.title("Escolha seu agente")

# 1. DADOS (A query precisa ser aquela com joins que ajustamos no catalogo.py)
agentes_db = obter_agentes() or []
perfis_db = obter_perfis() or []
colecoes_db = obter_colecoes() or []

# =========================================
# 2. LÓGICA DE SINCRONIZAÇÃO (HOME -> AGENTES)
# =========================================
# Recupera o que foi clicado na Home
p_inicial = st.session_state.get("filtro_perfil", "Todos")
c_inicial = st.session_state.get("filtro_colecao", "Todos")

# Opções para os selectboxes
opcoes_perfil = ["Todos"] + perfis_db
opcoes_colecao = ["Todos"] + colecoes_db

# Descobre o índice para o selectbox não resetar para "Todos"
idx_p = opcoes_perfil.index(p_inicial) if p_inicial in opcoes_perfil else 0
idx_c = opcoes_colecao.index(c_inicial) if c_inicial in opcoes_colecao else 0

# =========================================
# BUSCA
# =========================================
busca = st.text_input(
    "",
    placeholder="Buscar agente...",
    label_visibility="collapsed"
)

# =========================================
# FILTROS
# =========================================
col1, col2 = st.columns(2)

with col1:
    filtro_perfil = st.selectbox("Perfil", opcoes_perfil, index=idx_p)
    # Atualiza o state para manter a consistência
    st.session_state.filtro_perfil = filtro_perfil

with col2:
    filtro_colecao = st.selectbox("Coleção", opcoes_colecao, index=idx_c)
    st.session_state.filtro_colecao = filtro_colecao

# Botão de Reset (Aparece apenas se houver filtro ativo)
if filtro_perfil != "Todos" or filtro_colecao != "Todos" or busca:
    if st.button("❌ Limpar Filtros"):
        st.session_state.filtro_perfil = "Todos"
        st.session_state.filtro_colecao = "Todos"
        st.rerun()

# =========================================
# FILTRAGEM
# =========================================
agentes_filtrados = agentes_db

# 1. Filtro por Busca
if busca:
    agentes_filtrados = [
        a for a in agentes_filtrados
        if normalizar(busca) in normalizar(a.get("nome", ""))
    ]

# 2. Filtro por Perfil
if filtro_perfil != "Todos":
    agentes_filtrados = [
        a for a in agentes_filtrados
        if any(
            normalizar(filtro_perfil) == normalizar(p.get("perfis", {}).get("nome", ""))
            for p in a.get("agentes_perfis", [])
        )
    ]

# 3. Filtro por Coleção
if filtro_colecao != "Todos":
    agentes_filtrados = [
        a for a in agentes_filtrados
        if any(
            normalizar(filtro_colecao) == normalizar(c.get("colecoes", {}).get("nome", ""))
            for c in a.get("agentes_colecoes", [])
        )
    ]

# =========================================
# LISTA
# =========================================
if not agentes_filtrados:
    st.info("Nenhum agente encontrado para os filtros selecionados.")
else:
    cols = st.columns(3)
    for i, ag in enumerate(agentes_filtrados):
        with cols[i % 3]:
            # Fallback para imagem
            img = ag.get("url_publica") if ag.get("url_publica") else "https://via.placeholder.com/150"
            st.image(img, use_container_width=True)
            st.markdown(f"**{ag.get('nome')}**")

         # Na página agentes.py, mude para:
            if st.button("Acessar", key=f"ag_{ag.get('id')}"):
                st.session_state.agente_selecionado = ag
                st.switch_page("pages/_agente.py")  # <-- Caminho atualizado