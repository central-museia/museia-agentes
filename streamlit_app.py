import streamlit as st
from nocodb.catalogo import obter_catalogo, obter_perfis, obter_colecoes

# 1. CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="MuseIA Digital", layout="wide", initial_sidebar_state="collapsed")

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
    .mosaico-container { text-align: center; padding: 10px; }
    .mosaico-label { font-size: 14px; font-weight: bold; margin-top: 8px; color: white; }
</style>
""", unsafe_allow_html=True)

# --- CARREGAMENTO DE DADOS ---
colecoes_db = obter_colecoes()
perfis_db = obter_perfis()
agentes_db = obter_catalogo()

# --- SEÇÃO 1: HEADER ---
col_logo, col_vazio, col_login = st.columns([1, 2, 1])
with col_logo:
    st.image("assets/logo.png", width=120) 
with col_login:
    if st.button("👤 Acessar Minha Área"):
        st.toast("Área do cliente em desenvolvimento!")

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

# --- SEÇÃO 3: MOSAICO DE COLEÇÕES (Dinâmico com Imagem) ---
st.divider()
st.subheader("🌐 Um Ecossistema de Automação ao Seu Alcance")
if colecoes_db:
    cols_m = st.columns(5)
    for i, col in enumerate(colecoes_db):
        with cols_m[i % 5]:
            if col.get('imagem'):
                st.image(col['imagem'], use_container_width=True)
                st.markdown(f"<div style='text-align:center; font-weight:bold; font-size:12px;'>{col['nome']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color: {col['cor']}; padding: 20px; border-radius: 10px; text-align: center; color: white; font-weight: bold; border: 1px solid white;">
                    {col['nome']}
                </div>
                """, unsafe_allow_html=True)

# --- SEÇÃO 4: PERFIS (Agora com Imagens) ---
st.divider()
st.header("👤 Escolha Seu Perfil e Descubra Suas Soluções")
if perfis_db:
    cols_p = st.columns(4)
    for i, perfil in enumerate(perfis_db):
        with cols_p[i % 4]:
            with st.container():
                if perfil.get('imagem'):
                    st.image(perfil['imagem'], use_container_width=True)
                
                st.markdown(f"""
                <div class="card-perfil">
                    <h4>{perfil['nome']}</h4>
                    <p style="font-size: 13px;">{perfil['descricao'][:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Ver Soluções", key=f"btn_perf_{perfil['codigo']}", use_container_width=True):
                    st.session_state.filtro_selecionado = perfil['nome']

# --- SEÇÃO 5: CATÁLOGO DE AGENTES ---
st.divider()
st.header("🚀 Navegue por Nossas Coleções")

# Multiselect alimentado pelo banco
opcoes_colecoes = [c['nome'] for c in colecoes_db]
# Se o usuário clicou em um perfil, ele já começa selecionado aqui
filtro_inicial = [st.session_state.filtro_selecionado] if "filtro_selecionado" in st.session_state else []

selecao = st.multiselect("Filtre os agentes por categoria:", opcoes_colecoes, default=filtro_inicial)

if selecao:
    cols_ag = st.columns(4)
    idx = 0
    for agente in agentes_db:
        # Verifica se o agente pertence às coleções selecionadas (pelo nome ou código)
        if any(c in agente['colecoes'] for c in selecao) or any(c in agente['perfis'] for c in selecao):
            with cols_ag[idx % 4]:
                st.image(agente['imagem'] if agente['imagem'] else "assets/logo.png", use_container_width=True)
                st.markdown(f"**{agente['nome']}**")
                st.caption(f"Código: {agente['codigo']}")
                
                if st.button("🚀 Usar Agente", key=f"run_{agente['codigo']}"):
                    st.session_state.agente_atual = agente['codigo']
                    st.info(f"Validando acesso para o agente {agente['codigo']}...")
            idx += 1
    if idx == 0:
        st.warning("Nenhum agente encontrado para esta seleção.")
else:
    st.info("💡 Escolha uma coleção ou perfil acima para visualizar os agentes disponíveis.")

# --- SEÇÃO 7: FAQ ---
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
<div style="text-align: center; opacity: 0.7; padding: 20px;">
    <p>MuseIA Digital 2026 - A Inteligência Humana que controla a IA</p>
    <p style="font-size: 12px;">Termos de Uso | Política de Privacidade | Suporte</p>
</div>
""", unsafe_allow_html=True)
