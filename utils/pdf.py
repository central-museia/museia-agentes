import pdfplumber
from fpdf import FPDF
from datetime import datetime

# =========================================
# 📄 EXTRAIR TEXTO DE PDF (Leitura)
# =========================================
def ler_pdf(arquivo):
    texto = ""
    try:
        with pdfplumber.open(arquivo) as pdf:
            for pagina in pdf.pages:
                conteudo = pagina.extract_text()
                if conteudo:
                    texto += conteudo + "\n"
    except Exception as e:
        return f"Erro ao ler PDF: {e}"
    return texto

def ler_pdf_resumido(arquivo, limite=3000):
    texto = ler_pdf(arquivo)
    return texto[:limite]

# =========================================
# 📄 GERAR RELATÓRIO PROFISSIONAL (Escrita)
# =========================================
class MuseIAPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 15)
        self.set_text_color(229, 9, 20) # Vermelho MuseIA
        self.cell(0, 10, "MUSEIA DIGITAL", ln=True, align="L")
        self.set_draw_color(229, 9, 20)
        self.line(10, 20, 200, 20)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Página {self.page_no()} | Gerado em {datetime.now().strftime('%d/%m/%Y')}", align="C")

def exportar_resultado_pdf(agente_nome, texto_resultado):
    pdf = MuseIAPDF()
    pdf.add_page()
    
    # Título do Relatório
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 10, f"Relatório de Inteligência: {agente_nome}", ln=True)
    pdf.ln(5)
    
    # Corpo do Texto
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    
    # Limpeza de caracteres especiais (emojis/símbolos de IA)
    texto_limpo = texto_resultado.encode('latin-1', 'ignore').decode('latin-1')
    
    pdf.multi_cell(0, 8, texto_limpo)
    
    # --- SAÍDA SEGURA (O segredo do download) ---
    saida = pdf.output()
    
    if isinstance(saida, bytearray):
        return bytes(saida)
    elif isinstance(saida, str):
        return saida.encode('latin-1')
    return saida