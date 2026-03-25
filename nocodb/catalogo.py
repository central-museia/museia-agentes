import streamlit as st
import requests

def obter_headers():
    return {
        "xc-token": st.secrets["nocodb"]["api_key"],
        "Content-Type": "application/json"
    }

def obter_catalogo():
    try:
        url = st.secrets["nocodb"]["url_agentes"]
        response = requests.get(url, headers=obter_headers(), timeout=10)
        data = response.json()
        return data.get("list") or data.get("records") or []
    except:
        return []

def obter_perfis():
    try:
        url = st.secrets["nocodb"]["url_perfis"]
        response = requests.get(url, headers=obter_headers(), timeout=10)
        data = response.json()
        return data.get("list") or data.get("records") or []
    except:
        return []

def obter_colecoes():
    try:
        url = st.secrets["nocodb"]["url_colecoes"]
        response = requests.get(url, headers=obter_headers(), timeout=10)
        data = response.json()
        return data.get("list") or data.get("records") or []
    except:
        return []
