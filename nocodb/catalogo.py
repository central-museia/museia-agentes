import requests
import streamlit as st


def obter_catalogo():
    url = f"{st.secrets['nocodb']['url']}/api/v2/tables/mdg3nak99r78agx/records""

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
            "imagem": extrair_imagem(item),
            "codigo": item.get("codigo_agente", ""),
            "colecoes": extrair_codigos(item.get("prioridade_colecao")),
            "perfis": extrair_codigos(item.get("prioridade_perfil")),
            "arquivo": item.get("codigo_agente", "").lower()
        })

    return catalogo


# =========================================
# AUXILIAR
# =========================================

def extrair_codigos(valor):
    if not valor:
        return []

    return [v.strip() for v in str(valor).split(",") if v.strip()]


def extrair_imagem(item):
    if "imagem" in item and item["imagem"]:
        return item["imagem"][0].get("url", "")
    return ""


def extrair_texto_seguro(item, campo):
    return str(item.get(campo, "")).strip()
