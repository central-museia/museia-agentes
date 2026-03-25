import requests
import streamlit as st
from logger_museia import registrar_falha

# Configurações de Conexão (Puxando do st.secrets)
API_KEY = st.secrets["nocodb"]["api_key"]
HEADERS = {
    "xc-token": API_KEY,
    "Content-Type": "application/json"
}

def extrair_imagem(item):
    """Extrai a URL da imagem do campo anexo do NocoDB."""
    imagem_campo = item.get("Imagem") or item.get("imagem")
    
    if isinstance(imagem_campo, list) and len(imagem_campo) > 0:
        img = imagem_campo[0]
        # O NocoDB pode retornar 'url' ou 'path' dependendo da versão
        return img.get("url") or img.get("path", "")
    return None

def extrair_lista(valor):
    """Transforma strings separadas por vírgula em listas limpas."""
    if not valor:
        return []
    if isinstance(valor, list):
        return valor
    return [v.strip() for v in str(valor).split(",") if v.strip()]

# --- FUNÇÃO 1: AGENTES ---
def obter_catalogo():
    try:
        url = st.secrets['nocodb']['url'] # URL da sua tabela de Agentes
        params = {"limit": 100}
        
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        
        dados = response.json()
        records = dados.get("list") or dados.get("records") or []
        
        catalogo = []
        for item in records:
            # Só adiciona se o agente estiver ativo no banco
            if item.get("ativo") is True or str(item.get("ativo")).lower() == "true":
                codigo = item.get("codigo_agente", "")
                catalogo.append({
                    "nome": item.get("nome_agente", "Agente Sem Nome"),
                    "imagem": extrair_imagem(item),
                    "codigo": codigo,
                    "descricao": item.get("descricao", ""),
                    "colecoes": extrair_lista(item.get("prioridade_colecao")),
                    "perfis": extrair_lista(item.get("prioridade_perfil")),
                    "cor": item.get("cor_hex", "#14B8A6")
                })
        return catalogo

    except Exception as e:
        registrar_falha("obter_catalogo", e)
        return []

# --- FUNÇÃO 2: COLEÇÕES ---
def obter_colecoes():
    try:
        # IMPORTANTE: Adicione a URL da tabela Colecoes no seu st.secrets ou cole aqui
        url = st.secrets['nocodb'].get('url_colecoes') 
        if not url: return []

        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        colecoes = []
        for item in records:
            if item.get("ativo") is True or str(item.get("ativo")).lower() == "true":
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
        # IMPORTANTE: Adicione a URL da tabela Perfis no seu st.secrets ou cole aqui
        url = st.secrets['nocodb'].get('url_perfis')
        if not url: return []

        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        records = response.json().get("list") or response.json().get("records") or []
        
        perfis = []
        for item in records:
            if item.get("ativo") is True or str(item.get("ativo")).lower() == "true":
                perfis.append({
                    "nome": item.get("nome_perfil"),
                    "codigo": item.get("codigo"),
                    "descricao": item.get("descricao")
                })
        return perfis
    except Exception as e:
        registrar_falha("obter_perfis", e)
        return []
