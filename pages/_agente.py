import streamlit as st
from datetime import datetime
import time # Adicionado para não dar erro no sleep

# 1. Recupera o agente selecionado
ag = st.session_state.get("agente_selecionado")

# 2. Verifica se existe um agente no estado
if not ag:
    st.warning("Selecione um agente primeiro.")
    # Se você estiver na home ou em outra página, ele volta para a vitrine
    st.switch_page("pages/agentes.py") 
    st.stop()

# =========================================
# EXIBIÇÃO DO AGENTE (DESIGN LIMPO)
# =========================================
# Criando colunas para um visual mais profissional
col_img, col_txt = st.columns([1, 2])

with col_img:
    st.image(ag.get("url_publica") or "https://via.placeholder.com/400", use_container_width=True)

with col_txt:
    st.title(ag.get("nome"))
    st.write(ag.get("descricao"))

st.markdown("### ⚡ Benefícios")
st.markdown("""
- Economiza tempo real na sua operação
- Automatiza tarefas repetitivas
- Reduz erros humanos e aumenta a produtividade
""")

st.divider()

# =========================================
# BOTÃO DE AÇÃO (LÓGICA DE ACESSO)
# =========================================
if st.button("🚀 Usar este agente", use_container_width=True, key=f"btn_usar_{ag.get('id')}"):
    # 1. Checa se está logado
    if not st.session_state.get("logado"):
        st.warning("Para usar o agente, você precisa estar logado.")
        time.sleep(1.5)
        st.switch_page("pages/login.py")
        st.stop()

    # 2. Se logado, checa pagamento e validade
    user = st.session_state.usuario
    hoje = datetime.now().date()
    data_exp_str = user.get("data_expiracao")
    
    try:
        # Converte a data do banco para comparação
        expiracao = datetime.strptime(data_exp_str, '%Y-%m-%d').date() if data_exp_str else hoje
        
        if not user.get("ativo") or hoje > expiracao:
            st.error("Seu período de acesso expirou ou não está ativo.")
            # Em vez de st.button aqui dentro, usamos st.link_button ou informamos o caminho
            st.info("Acesse a página de Pagamento no menu para renovar.")
            # Se quiser mesmo o botão, o ideal é usar st.link_button para links externos 
            # ou apenas avisar, pois botões aninhados não funcionam bem.
        else:
            st.success(f"Acesso liberado! Bem-vinda, {user.get('nome').split()[0]}.")
            st.info("Iniciando interface de automação...")
            # Aqui entrará a chamada do seu robô
            
    except Exception as e:
        st.error("Erro ao validar sua assinatura. Por favor, contate o suporte.")

# =========================================
# BOTÃO VOLTAR (APENAS UM E COM KEY ÚNICA)
# =========================================
st.write("") # Espaçador visual
if st.button("⬅ Voltar para Galeria", key="btn_voltar_unico"):
    st.session_state.agente_selecionado = None 
    st.switch_page("pages/agentes.py")