import pdfplumber


# =========================================
# 📄 EXTRAIR TEXTO DE PDF
# =========================================
def ler_pdf(arquivo):

    texto = ""

    with pdfplumber.open(arquivo) as pdf:
        for pagina in pdf.pages:
            conteudo = pagina.extract_text()
            if conteudo:
                texto += conteudo + "\n"

    return texto


# =========================================
# 📄 EXTRAIR TEXTO LIMITADO (PARA IA)
# =========================================
def ler_pdf_resumido(arquivo, limite=3000):

    texto = ler_pdf(arquivo)

    return texto[:limite]
