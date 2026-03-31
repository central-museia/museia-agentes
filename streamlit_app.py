import streamlit as st
import sys
import os

# =========================================
# 🛠️ CONFIGURAÇÃO UNIFICADA DE CAMINHOS (PATH)
# =========================================
_root_dir = os.path.dirname(os.path.abspath(__file__))
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

# Importações ÚNICAS dos nossos módulos
try:
    # Bases e Segurança
    from database.catalogo import obter_catalogo, obter_perfis
    from auth.auth_museia import inicializar_sessao, login_ui, pode_utilizar
    from logger_museia import registrar_falha, exibir_painel_debug
    
    # Importando as funções da pasta /utils
    from utils.ia import gerar_resposta
    # from utils.pdf import ler_pdf
    # from utils.scraping import capturar
    
except Exception as e:
    st.error(f"Erro crítico ao carregar componentes da MuseIA: {e}")
    st.stop()
    
# =========================================
# 🎨 CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(page_title="MuseIA Digital", layout="wide", page_icon="🎬")

# Inicializa as variáveis de login e usuário
inicializar_sessao()

# CSS Estilo Netflix
st.markdown("""
<style>
    .main { background-color: #0E1117; }
    .card {
        background-color: #1e2130;
        border-radius: 10px;
        padding: 15px;
        transition: 0.3s;
        height: 100%;
        border: 1px solid #2e3140;
    }
    .card:hover {
        transform: scale(1.05);
        border-color: #e50914; 
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# 🔝 CABEÇALHO (HEADER)
# =========================================
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    try:
        st.image("assets/logo.png", width=120)
    except:
        st.title("MuseIA")

with col2:
    st.write("") 
    busca = st.text_input("🔍 Buscar agente ou categoria...", label_visibility="collapsed", placeholder="O que você quer automatizar hoje?")

with col3:
    login_ui()

st.divider()

# =========================================
# 🎬 HERO SECTION
# =========================================
st.markdown("# 🎬 Central de Agentes MuseIA")
st.markdown("### A inteligência humana que controla a IA")

# =========================================
# 🍿 CATÁLOGO ESTILO NETFLIX
# =========================================
try:
    perfis_db = obter_perfis()
    agentes_db = obter_catalogo()

    if perfis_db and agentes_db:
        for perfil in perfis_db:
            nome_perfil = perfil.get("nome")

            agentes_filtrados = [
                a for a in agentes_db 
                if nome_perfil in a.get("perfis", [])
            ]

            if busca:
                agentes_filtrados = [
                    a for a in agentes_filtrados
                    if busca.lower() in a.get("nome", "").lower() 
                    or busca.lower() in a.get("descricao", "").lower()
                ]

            if agentes_filtrados:
                st.subheader(nome_perfil)
                cols = st.columns(4)
                
                for i, agente in enumerate(agentes_filtrados):
                    with cols[i % 4]:
                        with st.container():
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            
                            img = agente.get("imagem") if agente.get("imagem") else "assets/logo.png"
                            st.image(img, use_container_width=True)
                            
                            st.markdown(f"### {agente.get('nome')}")
                            st.write(agente.get("descricao", "")[:100] + "...")
                            
                            # BOTÃO DE USO COM LÓGICA HÍBRIDA (PYTHON OU IA)
                            if st.button("🚀 Usar Agente", key=f"btn_{agente.get('id', i)}"):
                                if pode_utilizar():
                                    # Definimos o tipo de execução (Padrão: Python para economizar)
                                    # Se no seu banco a coluna 'tipo' for 'ia', ele usa o Gemini.
                                    tipo_agente = agente.get('tipo', 'python')
                                    
                                    if tipo_agente == 'ia':
                                        with st.spinner("IA processando..."):
                                            prompt = f"Atue como {agente.get('nome')}. Missão: {agente.get('descricao')}"
                                            resposta = gerar_resposta(prompt)
                                            st.markdown("---")
                                            st.write(resposta)
                                    else:
                                        # LÓGICA ESTRATÉGICA EM PYTHON (Custo Zero)
                                        st.success(f"Executando lógica estratégica Python para: {agente.get('nome')}")
                                        st.info("Processamento concluído localmente (Sem uso de tokens de IA).")
                                        # Aqui você insere a chamada para suas funções de WFM/Planejamento
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                st.write("") 

    else:
        st.info("O catálogo está sendo atualizado. Volte em instantes!")

except Exception as e:
    registrar_falha("streamlit_app_catalogo", e)
    st.error("Erro ao carregar a vitrine. Verifique os logs.")

# =========================================
# 🛠️ RODAPÉ & DEBUG
# =========================================
st.divider()
st.markdown("<center> MuseIA Digital © 2026 - Inteligência e Governança </center>", unsafe_allow_html=True)

if st.session_state.get('logado', False):
    exibir_painel_debug()