from utils.pdf import exportar_resultado_pdf
import streamlit as st
from datetime import datetime
import time

# =========================================
# CONFIGURAÇÃO E ESTADO INICIAL
# =========================================
ag = st.session_state.get("agente_selecionado")

if not ag:
    st.warning("Selecione um agente primeiro.")
    st.switch_page("pages/agentes.py") 
    st.stop()

if "processamento_liberado" not in st.session_state:
    st.session_state.processamento_liberado = False

# =========================================
# EXIBIÇÃO DO AGENTE (DESIGN LIMPO)
# =========================================
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

if not st.session_state.get("processamento_liberado"):
    if st.button("🚀 Usar este agente", use_container_width=True, key=f"btn_usar_{ag.get('id')}"):
        
        # 1. PRIORIDADE ZERO: Se não tem login, vai para login.py
        if not st.session_state.get("logado"):
            st.session_state.origem = "pages/_agente.py"
            st.warning("Identificamos que você não está logada. Redirecionando...")
            time.sleep(1)
            st.switch_page("pages/login.py")
            st.stop()

        # 2. LOGADO? Agora sim verificamos a situação da assinatura
        user = st.session_state.get("usuario")
        
        if user:
            hoje = datetime.now().date()
            data_exp_str = user.get("data_expiracao")
            
            try:
                expiracao = datetime.strptime(data_exp_str, '%Y-%m-%d').date() if data_exp_str else hoje
                
                # SE ESTÁ INATIVO OU EXPIROU: Vai para a página de Pagamento
                if not user.get("ativo") or hoje > expiracao:
                    st.error("Seu acesso expirou ou não está ativo.")
                    st.info("Redirecionando para a página de renovação...")
                    time.sleep(2)
                    st.switch_page("pages/pagamento.py") # <--- Direciona para pagamento
                    st.stop()
                
                # SE ESTÁ TUDO OK: Libera o processamento
                else:
                    st.success(f"Acesso liberado! Bem-vinda.")
                    st.session_state.processamento_liberado = True
                    st.rerun()
                    
            except Exception as e:
                st.error("Erro ao validar dados. Por favor, faça login novamente.")
                st.session_state.logado = False
                st.rerun()

# =========================================
# ÁREA DE TRABALHO (APARECE APÓS VALIDAÇÃO)
# =========================================
if st.session_state.processamento_liberado:
    st.info(f"Você está usando o robô: **{ag.get('nome')}**")
    
    if "resultado_final" not in st.session_state:
        st.session_state.resultado_final = None

    dados_input = st.text_area("📋 Insira ou cole aqui as informações para o agente analisar:", height=250)
    
    col_run, col_clear = st.columns([1, 1])
    
    with col_run:
        if st.button("🪄 Gerar Resultado Agora", use_container_width=True):
            if dados_input:
                with st.spinner("A MuseIA está processando sua solicitação..."):
                    time.sleep(3) 
                    st.session_state.resultado_final = f"RESULTADO DA MUSEIA\n---\nAgente: {ag.get('nome')}\nData: {datetime.now().strftime('%d/%m/%Y')}\n---\n\n{dados_input.upper()[:200]}... [Conteúdo Processado]"
            else:
                st.warning("O campo de informações está vazio.")

    with col_clear:
        if st.button("🔄 Nova Consulta", use_container_width=True):
            st.session_state.resultado_final = None 
            st.rerun()

# ... (resto do seu código acima)

    if st.session_state.resultado_final:
        st.divider()
        st.markdown("### ✅ Resultado Pronto")
        st.text_area("Resultado Gerado:", value=st.session_state.resultado_final, height=300)
        
        col_down1, col_down2 = st.columns(2)

        with col_down1:
            st.download_button(
                label="📥 Baixar em Texto (.txt)",
                data=st.session_state.resultado_final,
                file_name=f"MuseIA_{ag.get('nome')}.txt",
                mime="text/plain",
                use_container_width=True,
                key="btn_txt_vfinal"
            )

        with col_down2:
            # A IMPORTAÇÃO E A GERAÇÃO DEVEM FICAR AQUI DENTRO
            from utils.pdf import exportar_resultado_pdf
            
            # Só tentamos gerar se houver resultado, evitando o erro ao abrir a página
            try:
                pdf_bytes = exportar_resultado_pdf(ag.get("nome"), st.session_state.resultado_final)
                
                st.download_button(
                    label="📄 Baixar Relatório (PDF)",
                    data=pdf_bytes,
                    file_name=f"MuseIA_{ag.get('nome')}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="btn_pdf_vfinal"
                )
            except Exception as e:
                st.error("Erro ao preparar o PDF.")
                                
# =========================================
# BOTÃO VOLTAR
# =========================================
st.write("") 
if st.button("⬅ Voltar para Galeria", key="btn_voltar_unico"):
    st.session_state.agente_selecionado = None 
    st.session_state.processamento_liberado = False
    st.switch_page("pages/agentes.py")