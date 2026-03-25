import requests
import streamlit as st

def obter_catalogo():
    # Busca as credenciais nos secrets do Streamlit
    try:
        # Puxa os dados do st.secrets (conforme configurado no seu TOML)
       url = f"{st.secrets['nocodb']['url']}{st.secrets['nocodb']['table_path']}"
        api_key = st.secrets["nocodb"]["api_key"]
        
        headers = {
            "xc-token": api_key,
            "Content-Type": "application/json"
        }
        
        # Parâmetros para garantir que tragamos até 100 agentes de uma vez
        params = {"limit": 100}

        # Request com timeout de 10s para evitar travamento infinito
        response = requests.get(url, headers=headers, params=params, timeout=10)

        # Se houver erro de conexão ou permissão (401, 403, 404), vai direto para o except
        response.raise_for_status()

        # O NocoDB v2 usa "list" ou "records" dependendo da versão da API
        dados_brutos = response.json()
        records = dados_brutos.get("list") or dados_brutos.get("records") or []
        
        catalogo = []

        for item in records:
            # Extração segura com .get() para evitar erros de chave inexistente
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

    except Exception as e:
        # Log de erro silencioso no console do Streamlit Cloud, mas amigável na tela
        st.warning(f"⚠️ Conexão NocoDB indisponível. Usando catálogo de contingência.")
        
        # Fallback de segurança para o MuseIA não ficar em branco
        return [
            {
                "nome": "Agente de Teste (Offline)",
                "imagem": "",
                "codigo": "TEST-001",
                "colecoes": ["ADM"],
                "perfis": ["EMP"],
                "arquivo": "test-001"
            }
        ]

# =========================================
# FUNÇÕES AUXILIARES DE TRATAMENTO
# =========================================

def extrair_codigos(valor):
    """Trata strings separadas por vírgula vindas do banco."""
    if not valor:
        return []
    # Converte para string antes de fazer o split para evitar erro com números
    return [v.strip() for v in str(valor).split(",") if v.strip()]

def extrair_imagem(item):
    """Extrai a URL da imagem do formato de anexo do NocoDB."""
    imagem_campo = item.get("imagem")
    
    # O NocoDB envia imagens como uma lista de dicionários
    if isinstance(imagem_campo, list) and len(imagem_campo) > 0:
        # Tenta pegar a URL direta ou o path relativo
        img = imagem_campo[0]
        return img.get("url") or img.get("path", "")
    return ""
