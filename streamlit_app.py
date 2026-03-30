import streamlit as st
import sys
import os

# =========================================
# 🛠️ CONFIGURAÇÃO DE CAMINHOS (PATH)
# =========================================
# Adiciona a raiz do projeto ao sys.path para que as pastas /auth, /core e /supabase sejam encontradas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações dos nossos módulos criados nas etapas anteriores
from supabase.catalogo import obter_catalogo, obter_perfis
from auth.auth_museia import inicializar_sessao, login_ui, pode_utilizar
from logger_museia import registrar_falha, exibir_painel_debug

# =========================================
# 🎨 CONFIGURAÇÃO DA PÁGINA & UI
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
        border-color: #e50914; /* Vermelho Netflix no hover */
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
    # Tenta carregar a logo, se falhar usa texto
    try:
        st.image("assets/logo.png", width=120)
    except:
        st.title("MuseIA")

with col2:
    st.write("") # Espaçador
    busca = st.text_input("🔍 Buscar agente ou categoria...", label_visibility="collapsed", placeholder="O que você quer automatizar hoje?")

with col3:
    # Chamar a interface de login (ela decide se mostra o botão 'Sair' ou o form 'Entrar')
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

            # 1. Filtra agentes por perfil
            agentes_filtrados = [
                a for a in agentes_db 
                if nome_perfil in a.get("perfis", [])
            ]

            # 2. Aplica filtro de busca (se houver)
            if busca:
                agentes_filtrados = [
                    a for a in agentes_filtrados
                    if busca.lower() in a.get("nome", "").lower() 
                    or busca.lower() in a.get("descricao", "").lower()
                ]

            # 3. Renderiza a fileira (Row) se houver agentes
            if agentes_filtrados:
                st.subheader(nome_perfil)
                
                # Cria colunas (ex: 4 colunas por linha)
                cols = st.columns(4)
                
                for i, agente in enumerate(agentes_filtrados):
                    with cols[i % 4]:
                        with st.container():
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            
                            # Imagem do Agente
                            img = agente.get("imagem") if agente.get("imagem") else "assets/logo.png"
                            st.image(img, use_container_width=True)
                            
                            st.markdown(f"### {agente.get('nome')}")
                            st.write(agente.get("descricao", "")[:100] + "...")
                            
                            # BOTÃO DE USO (Com trava de segurança)
                            if st.button("🚀 Usar Agente", key=f"btn_{agente.get('id', i)}"):
                                # Aqui aplicamos a regra: Pode navegar? SIM. Pode usar? SÓ SE ATIVO.
                                if pode_utilizar():
                                    st.success(f"Iniciando {agente.get('nome')}...")
                                    # Lógica para chamar o agente aqui
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                st.write("") # Espaçador entre linhas

    else:
        st.info("O catálogo está sendo atualizado. Volte em instantes!")

except Exception as e:
    registrar_falha("streamlit_app_catalogo", e)
    st.error("Ocorreu um erro ao carregar a vitrine. Nossa equipe técnica já foi avisada.")

# =========================================
# 🛠️ RODAPÉ & DEBUG (SÓ PARA VOCÊ)
# =========================================
st.divider()
st.markdown("<center> MuseIA Digital © 2026 - Inteligência e Governança </center>", unsafe_allow_html=True)

# Exibe o histórico de falhas apenas se você estiver logada (opcional)
if st.session_state.logado:
    exibir_painel_debug()