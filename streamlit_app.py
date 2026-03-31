import streamlit as st
import sys
import os

# 🛠️ AJUSTE DE PATH (Para o Python enxergar suas pastas locais)
_root = os.path.dirname(os.path.abspath(__file__))
if _root not in sys.path:
    sys.path.insert(0, _root)

# 📦 IMPORTAÇÕES DOS SEUS MÓDULOS
try:
    # Importando dos arquivos que você confirmou na pasta 'database'
    from database.catalogo import obter_catalogo, obter_perfis
    # Importando da pasta 'auth'
    from auth.auth_museia import inicializar_sessao, login_ui, pode_utilizar
    # Importando da pasta 'utils'
    from utils.ia import gerar_resposta
except Exception as e:
    st.error(f"Erro de mapeamento: {e}")
    st.stop()

# 🎨 CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="MuseIA Digital", layout="wide")

# Inicializa as variáveis de login (do auth_museia.py)
inicializar_sessao()

# 🔝 HEADER (Estilo que você validou)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("assets/logo.png", width=120)
with col2:
    busca = st.text_input("🔍", placeholder="O que vamos automatizar?", label_visibility="collapsed")
with col3:
    login_ui()

st.divider()

# 🍿 VITRINE DE AGENTES
try:
    perfis = obter_perfis()
    agentes = obter_catalogo()

    if perfis and agentes:
        for p in perfis:
            nome_p = p.get("nome")
            # Filtro simples
            filtrados = [a for a in agentes if nome_p in a.get("perfis", [])]
            
            if filtrados:
                st.subheader(f"👤 {nome_p}")
                cols = st.columns(4)
                for i, ag in enumerate(filtrados):
                    with cols[i % 4]:
                        st.image(ag.get("imagem") or "assets/logo.png", use_container_width=True)
                        st.markdown(f"**{ag.get('nome')}**")
                        
                        if st.button("🚀 Usar", key=f"ag_{ag.get('id', i)}"):
                            if pode_utilizar():
                                # Lógica de produção: Python ou IA
                                if ag.get('tipo') == 'ia':
                                    with st.spinner("IA processando..."):
                                        st.write(gerar_resposta(ag.get('descricao')))
                                else:
                                    st.success(f"Agente {ag.get('nome')} ativado via Python.")
    else:
        st.warning("Banco de dados vazio ou inacessível.")
except Exception as e:
    st.error(f"Falha ao renderizar catálogo: {e}")

st.divider()
st.markdown("<center> MuseIA Digital 2026 </center>", unsafe_allow_html=True)