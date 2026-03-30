from .cliente import get_client

# =========================================
# 🚀 OBTER AGENTES / CATÁLOGO
# =========================================
def obter_agentes():
    """Busca todos os agentes ativos e suas relações de coleções e perfis."""
    try:
        supabase = get_client()

        response = (
            supabase
            .table("agentes")
            .select("""
                *,
                agentes_colecoes(
                    colecoes(nome)
                ),
                agentes_perfis(
                    perfis(nome)
                )
            """)
            .eq("ativo", True)
            .execute()
        )

        agentes = []
        for a in response.data:
            # Organiza coleções e perfis em listas simples para o frontend
            a["colecoes"] = [c["colecoes"]["nome"] for c in a.get("agentes_colecoes", []) if c.get("colecoes")]
            a["perfis"] = [p["perfis"]["nome"] for p in a.get("agentes_perfis", []) if p.get("perfis")]
            agentes.append(a)

        return agentes
    except Exception as e:
        print(f"Erro ao obter catálogo: {str(e)}")
        return []

def obter_perfis():
    """Retorna perfis de agentes ativos (ex: BI, Vendas, RH)."""
    try:
        supabase = get_client()
        response = supabase.table("perfis").select("*").eq("ativo", True).execute()
        return response.data or []
    except Exception as e:
        print(f"Erro ao obter perfis: {str(e)}")
        return []

def obter_colecoes():
    """Retorna coleções ativas (ex: Kit Inicial, Gestão)."""
    try:
        supabase = get_client()
        response = supabase.table("colecoes").select("*").eq("ativo", True).execute()
        return response.data or []
    except Exception as e:
        print(f"Erro ao obter coleções: {str(e)}")
        return []