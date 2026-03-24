import streamlit as st

st.set_page_config(
    page_title="MuseIA Digital",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILO ---
st.markdown("""
<style>
    .stApp { background-color: #080808; color: white; }
    #MainMenu, footer, header {visibility: hidden;}

    .hero { text-align:center; padding:60px 20px; }
    .logo { font-size:26px; font-weight:800; color:#8A2BE2; }
    .headline { font-size:42px; font-weight:800; margin-top:10px; }
    .sub { font-size:18px; color:#AAA; margin-top:10px; }

    .card {
        background:#111;
        padding:20px;
        border-radius:12px;
        margin-bottom:15px;
        border:1px solid #222;
        transition:0.3s;
    }

    .card:hover {
        transform: scale(1.02);
        border:1px solid #555;
    }

    /* CORES POR CATEGORIA */
    .growth { border-left: 5px solid #16A34A; }
    .bi { border-left: 5px solid #2563EB; }
    .gestao { border-left: 5px solid #7C3AED; }
    .marketing { border-left: 5px solid #F97316; }
    .financeiro { border-left: 5px solid #14B8A6; }

    .price {
        font-size:28px;
        font-weight:800;
        margin-top:20px;
    }

    div.stButton > button {
        background: linear-gradient(180deg, #9D4EDD 0%, #7B2CBF 100%);
        color: white;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 800;
        padding: 18px;
        width:100%;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO ---
st.markdown('<div class="hero">', unsafe_allow_html=True)

st.markdown('<div class="logo">MUSEIA DIGITAL</div>', unsafe_allow_html=True)

st.markdown('<div class="headline">Deixe a IA trabalhar por você</div>', unsafe_allow_html=True)

st.markdown('<div class="sub">Automatize tarefas reais do seu dia a dia — sem precisar saber tecnologia.</div>', unsafe_allow_html=True)

if st.button("ACESSAR AGENTES AGORA"):
    st.success("Redirecionando...")

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- IDENTIFICAÇÃO POR PERFIL ---
st.markdown("## Para quem é a MuseIA?")
st.markdown("Escolha sua área e veja como a IA pode trabalhar por você:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card gestao">
    <h4>🩺 Clínicas e Consultórios</h4>
    <p>Reduza tarefas repetitivas e organize sua clínica automaticamente.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card growth">
    <h4>💼 Administrativo</h4>
    <p>Responda e-mails e gere relatórios sem esforço.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card marketing">
    <h4>💇 Salões e Estética</h4>
    <p>Mantenha sua agenda cheia e automatize o atendimento.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card bi">
    <h4>📊 Planejamento & Operações</h4>
    <p>Tome decisões com base em dados em minutos.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card marketing">
    <h4>📣 Marketing & Conteúdo</h4>
    <p>Crie posts e conteúdos sem travar na criação.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card gestao">
    <h4>👥 Recursos Humanos</h4>
    <p>Organize processos seletivos e respostas automaticamente.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- DEMONSTRAÇÃO ---
st.markdown("## Veja o que você pode fazer")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card growth">
    <h4>📧 Responder e-mails</h4>
    <p>Respostas profissionais em segundos.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card bi">
    <h4>📊 Criar relatórios</h4>
    <p>Transforme dados em decisões.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card marketing">
    <h4>📱 Criar conteúdo</h4>
    <p>Posts e legendas prontos.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- CATÁLOGO ---
st.markdown("## Explore os agentes")

agents = [
    ("Gerador de Respostas Profissionais", "growth"),
    ("Resumo de Reuniões", "gestao"),
    ("Priorizador de Atividades", "bi"),
    ("Gerador de Posts", "marketing"),
    ("Analisador de Inadimplência", "financeiro"),
    ("Planejador de Conteúdo", "marketing")
]

cols = st.columns(3)

for i, (agent, categoria) in enumerate(agents):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card {categoria}">
        <strong>{agent}</strong>
        <p>Pronto para uso imediato</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- BENEFÍCIOS ---
st.markdown("## Por que usar a MuseIA?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("⚡ **Rápido**  \nUse em minutos")

with col2:
    st.markdown("🧠 **Inteligente**  \nIA trabalhando por você")

with col3:
    st.markdown("💰 **Acessível**  \nAlto retorno com baixo custo")

st.divider()

# --- CTA FINAL ---
st.markdown('<div style="text-align:center; padding:40px;">', unsafe_allow_html=True)

st.markdown('<div class="price">R$ 79,90/mês</div>', unsafe_allow_html=True)

st.markdown(
    '<p style="color:#00FF7F;">7 dias de garantia • Cancele quando quiser</p>',
    unsafe_allow_html=True
)

if st.button("COMEÇAR AGORA"):
    st.success("Iniciando...")

st.markdown("</div>", unsafe_allow_html=True)
