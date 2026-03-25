import requests
import streamlit as st
from logger_museia import registrar_falha

# Configuração Centralizada de Headers
def obter_headers():
    return {
        "xc-token": st.secrets["nocodb"]["api_key"],
        "Content-Type": "application/json"
    }

def extrair_imagem(item):
    """Lógica robusta para extrair a URL da imagem (do campo 'Imagem')"""
    # O NocoDB pode mandar como lista de dicionários ou string com URL entre parênteses
    imagem_campo = item.get("Imagem") or item.get("imagem")
    
    if isinstance(imagem_campo, list) and len(imagem_campo) > 0:
        return imagem_campo[0].get("url") or imagem_campo[0].get("path", "")
    
    # Fallback caso a imagem venha como string (comum em CSVs/importações)
    if isinstance(imagem_campo, str) and "https" in imagem_campo:
        import re
        urls = re.findall(r'(https?://[^\s)]+)', imagem_campo)
        return urls[0] if urls else None
    return None

# --- FUNÇÃO 1: AGENTES ---
def obter_catalogo():
    try:
        url = st.secrets['nocodb']['url_agentes']
        response = requests.get(url, headers=obter_headers(), timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        catalogo = []
        for item in records:
            # Filtro de Ativo (aceita booleano ou string 'true')
            if str(item.get("ativo")).lower() == "true":
                catalogo.append({
                    "nome": item.get("nome_agente"),
                    "codigo": item.get("codigo_agente"),
                    "descricao": item.get("descricao"),
                    "imagem": extrair_imagem(item),
                    "colecoes": str(item.get("prioridade_colecao", "")).split(","),
                    "perfis": str(item.get("prioridade_perfil", "")).split(","),
                    "cor": item.get("cor_hex", "#14B8A6")
                })
        return catalogo
    except Exception as e:
        registrar_falha("obter_catalogo", e)
        return []

# --- FUNÇÃO 2: COLEÇÕES ---
def obter_colecoes():
    try:
        url = st.secrets['nocodb']['url_colecoes']
        response = requests.get(url, headers=obter_headers(), timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        colecoes = []
        for item in records:
            if str(item.get("ativo")).lower() == "true":
                colecoes.append({
                    "nome": item.get("nome_colecao"),
                    "codigo": item.get("codigo"),
                    "descricao": item.get("descricao"),
                    "cor": item.get("cor_hex", "#0EA5E9")
                })
        return colecoes
    except Exception as e:
        registrar_falha("obter_colecoes", e)
        return []

# --- FUNÇÃO 3: PERFIS ---
def obter_perfis():
    try:
        url = st.secrets['nocodb']['url_perfis']
        response = requests.get(url, headers=obter_headers(), timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        perfis = []
        for item in records:
            if str(item.get("ativo")).lower() == "true":
                perfis.append({
                    "nome": item.get("nome_perfil"),
                    "codigo": item.get("codigo"),
                    "descricao": item.get("descricao")
                })
        return perfis
    except Exception as e:
        registrar_falha("obter_perfis", e)
        return []
