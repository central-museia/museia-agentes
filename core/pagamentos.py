import streamlit as st


# =========================================
# 🔐 LOGIN PRINCIPAL (NÃO MUDAR NOME)
# =========================================
def exibir_login():
    st.title("🔐 Entrar na MuseIA")

    email = st.text_input("Digite seu e-mail")

    if st.button("🚀 Acessar plataforma"):

        if not email:
            st.warning("Digite seu e-mail.")
            return

        if validar_email(email):
            st.session_state["logado"] = True
            st.session_state["email"] = email
            st.rerun()
        else:
            st.error("Acesso não autorizado.")


# =========================================
# 🧠 VALIDAÇÃO (MOCK AGORA, BANCO DEPOIS)
# =========================================
def validar_email(email):

    clientes_autorizados = [
        "seuemail@email.com",  # <-- coloque seu e-mail real aqui
    ]

    return email.lower() in clientes_autorizados


# =========================================
# 🚪 LOGOUT (IMPORTANTE TER)
# =========================================
def logout():
    st.session_state.clear()
    st.rerun()


# =========================================
# 🔒 PROTEÇÃO GLOBAL DO APP
# =========================================
def proteger_app():

    if "logado" not in st.session_state or not st.session_state["logado"]:
        exibir_login()
        st.stop()
