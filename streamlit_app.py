import streamlit as st

# Configuração de Página (Sempre a 1ª linha)
st.set_page_config(page_title="MuseIA Digital", layout="wide", page_icon="🟣")

# --- BLINDAGEM DE CONEXÃO ---
# Tenta importar o pagamento, se falhar ou não tiver a função, ele cria uma versão genérica local
try:
    from core import pagamentos
    if not hasattr(pagamentos, 'exibir_login'):
        raise ImportError
except (ImportError, ModuleNotFoundError, Exception):
    class pagamentos:
        @staticmethod
        def exibir_login():
            st.warning("⚠️ Camada de Pagamento em construção...")
            if st.button("Pular para o Catálogo (Modo Admin)"):
                st.session_state["logado"] = True
                st.rerun()

# --- CSS NETFLIX (APARÊNCIA) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1 { color: #E50914; font-family: 'Arial Black'; text-transform: uppercase; }
    .card { background-color: #141414; border: 1px solid #333; padding: 20px; border-radius: 8px; text-align: center; }
    div.stButton > button { background-color: #E50914 !important; color: white !important; border: none !important; }
</style>
""", unsafe_allow_html=True)

# --- LÓGICA DE NAVEGAÇÃO ---
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    pagamentos.exibir_login()
    st.stop()

# Vitrine de Agentes
if "agente" not in st.session_state:
    st.session_state["agente"] = None

if st.session_state["agente"] is None:
    st.title("MUSEIA DIGITAL")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card"><h3>🏆 DEEP SCAN</h3></div>', unsafe_allow_html=True)
        if st.button("ACESSAR 04"): st.session_state["agente"] = "04"; st.rerun()
    # Outros botões seguem o mesmo padrão...
else:
    if st.button("← VOLTAR"):
        st.session_state["agente"] = None
        st.rerun()
    st.write(f"Você está no Agente {st.session_state['agente']}")
