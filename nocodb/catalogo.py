import requests
import streamlit as st

def obter_catalogo():
    # Busca as credenciais nos secrets do Streamlit
    try:
        url = st.secrets['nocodb']['url']
        headers = {"xc-token": st.secrets["nocodb"]["api_key"]}
        
        # Adicionamos um timeout de 10 segundos para não travar o app se o NocoDB estiver lento
        response = requests.get(url, headers=headers, timeout=10)

        # Se o status não for 200, levantamos um erro para cair no bloco 'except'
        response.raise_for_status()

        data = response.json().get("records", [])
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

    except (requests.exceptions.RequestException, KeyError) as e:
        # Se houver erro de conexão, timeout ou erro de URL/Chave nos secrets
        st.error(f"⚠️ Não foi possível conectar ao catálogo do NocoDB. Exibindo modo de segurança.")
        
        # Retorna o Fallback para o app não parar de funcionar
        return [
            {
                "nome": "Agente de Teste (Modo Offline)",
                "imagem": "",
                "codigo": "TEST-001",
                "colecoes": ["ADM"],
                "perfis": ["EMP"],
                "arquivo": "test-001"
            }
        ]

# =========================================
# AUXILIARES (Mantidos como os seus)
# =========================================

def extrair_codigos(valor):
    if not valor:
        return []
    return [v.strip() for v in str(valor).split(",") if v.strip()]

def extrair_imagem(item):
    if isinstance(item.get("imagem"), list) and len(item["imagem"]) > 0:
        return item["imagem"][0].get("url", "")
    return ""
