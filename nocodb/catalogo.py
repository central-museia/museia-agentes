import requests
import streamlit as st


def obter_catalogo():
    try:
        url = st.secrets['nocodb']['url']
        api_key = st.secrets["nocodb"]["api_key"]

        headers = {
            "xc-token": api_key,
            "Content-Type": "application/json"
        }

        params = {"limit": 100}

        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        dados_brutos = response.json()
        records = dados_brutos.get("list") or dados_brutos.get("records") or []

        catalogo = []

        for item in records:
            codigo = item.get("codigo_agente", "")

            catalogo.append({
                "nome": item.get("nome_agente", "Agente Sem Nome"),
                "imagem": extrair_imagem(item),
                "codigo": codigo,
                "colecoes": extrair_codigos(item.get("prioridade_colecao")),
                "perfis": extrair_codigos(item.get("prioridade_perfil")),
                "arquivo": str(codigo).lower() if codigo else "indefinido"
            })

        return catalogo

    except Exception:
        st.warning("⚠️ Conexão NocoDB indisponível. Usando fallback.")
        return []


def extrair_codigos(valor):
    if not valor:
        return []
    return [v.strip() for v in str(valor).split(",") if v.strip()]


def extrair_imagem(item):
    imagem_campo = item.get("imagem")

    if isinstance(imagem_campo, list) and len(imagem_campo) > 0:
        img = imagem_campo[0]
        return img.get("url") or img.get("path", "")
    
    return ""
