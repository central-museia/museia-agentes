import requests
import streamlit as st
import re
from logger_museia import registrar_falha

# 1. Configuração Centralizada de Headers
def obter_headers():
    return {
        "xc-token": st.secrets["nocodb"]["api_key"],
        "Content-Type": "application/json"
    }

# 2. Lógica de Extração e Limpeza de Imagem
def extrair_imagem(item, campo_nome):
    """
    Captura a URL da imagem de forma robusta.
    Resolve o problema de links temporários do NocoDB e links 'sujos' de CSV.
    """
    # Tenta o nome exato ou minúsculo (evita erro de digitação no banco)
    imagem_campo = item.get(campo_nome) or item.get(campo_nome.lower())
    
    if not imagem_campo:
        return None

    # Caso A: Upload direto no NocoDB (Lista de objetos)
    if isinstance(imagem_campo, list) and len(imagem_campo) > 0:
        return imagem_campo[0].get("url") or imagem_campo[0].get("path", "")
    
    # Caso B: String (Link direto ou formato 'nome.png(http...)')
    if isinstance(imagem_campo, str):
        # Filtra apenas o que é URL válida dentro da string
        links = re.findall(r'https?://[^\s)]+', imagem_campo)
        if links:
            return links[0]
            
    return None

# --- FUNÇÃO 1: AGENTES (O Catálogo Principal) ---
def obter_catalogo():
    try:
        url = st.secrets['nocodb']['url_agentes']
        response = requests.get(url, headers=obter_headers(), timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        catalogo = []
        for item in records:
            if str(item.get("ativo")).lower() == "true":
                catalogo.append({
                    "nome": item.get("nome_agente"),
                    "codigo": item.get("codigo_agente"),
                    "descricao": item.get("descricao"),
                    "imagem": extrair_imagem(item, "Imagem"), 
                    "colecoes": str(item.get("prioridade_colecao", "")).split(","),
                    "perfis": str(item.get("prioridade_perfil", "")).split(","),
                    "cor": item.get("cor_hex", "#14B8A6")
                })
        return catalogo
    except Exception as e:
        registrar_falha("obter_catalogo", e)
        return []

# --- FUNÇÃO 2: COLEÇÕES (Mosaico) ---
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
                    "cor": item.get("cor_hex", "#0EA5E9"),
                    "imagem": extrair_imagem(item, "imagem_colecao") 
                })
        return colecoes
    except Exception as e:
        registrar_falha("obter_colecoes", e)
        return []

# --- FUNÇÃO 3: PERFIS (Filtros de Jornada) ---
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
                    "descricao": item.get("descricao"),
                    "imagem": extrair_imagem(item, "imagem_perfil")
                })
        return perfis
    except Exception as e:
        registrar_falha("obter_perfis", e)
        return []
