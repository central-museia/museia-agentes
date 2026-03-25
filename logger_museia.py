import datetime
import os
import streamlit as st

# Caminho do arquivo de log
LOG_FILE = "falhas_sistema.txt"

def registrar_falha(origem, erro_objeto):
    """
    Grava os detalhes técnicos em um arquivo de texto.
    'origem' deve ser o nome da função (ex: 'obter_catalogo')
    'erro_objeto' é a exceção capturada no 'except'
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Detalhes técnicos para o arquivo
    conteudo_erro = (
        f"--- FALHA DETECTADA EM {timestamp} ---\n"
        f"LOCAL: {origem}\n"
        f"ERRO: {str(erro_objeto)}\n"
        f"{'-' * 40}\n"
    )
    
    # Escreve no arquivo (modo 'a' de append para não apagar os anteriores)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(conteudo_erro)

def exibir_painel_debug():
    """Função opcional para você ver o log direto no Streamlit se quiser"""
    if os.path.exists(LOG_FILE):
        with st.expander("📂 Ver Histórico de Falhas (Debug)"):
            with open(LOG_FILE, "r") as f:
                st.text(f.read())
            if st.button("Limpar Log"):
                os.remove(LOG_FILE)
                st.rerun()
    else:
        st.info("Nenhuma falha registrada até o momento. ✅")
