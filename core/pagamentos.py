# integração com pagamento (Payhip)
import streamlit as st

def exibir_login():  # <--- O nome tem que ser EXATAMENTE este
    st.title("🍿 Entrar na MuseIA")
    token = st.text_input("Digite seu Token de Acesso", type="password")
    if st.button("ASSISTIR AGORA"):
        if token == "teste123":
            st.session_state["logado"] = True
            st.rerun()
        else:
            st.error("Token inválido.")
