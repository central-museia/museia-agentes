import requests
import streamlit as st


def obter_catalogo():
    url = f"{st.secrets['nocodb']['url']}/api/v1/db/data/v1/Agentes"

    headers = {
        "xc-token": st.secrets["nocodb"]["api_key"]
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    data = response.json().get("list", [])

    catalogo = []

    for item in data:
        catalogo.append({
            "nome": item.get("nome_agente", ""),
            "codigo": item.get("codigo_agente", ""),
            "colecao": extrair_colecao(item),
            "publico": extrair_perfil(item),
            "arquivo": item.get("codigo_agente", "").lower()
        })

    return catalogo


# =========================================
# AUXILIARES (SIMPLES POR ENQUANTO)
# =========================================

def extrair_colecao(item):
    # ajuste conforme estrutura do NocoDB
    if "colecoes" in item and item["colecoes"]:
        return item["colecoes"][0].get("nome_colecao", "")
    return ""


def extrair_perfil(item):
    if "perfis" in item and item["perfis"]:
        return item["perfis"][0].get("nome_perfil", "")
    return ""
