import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re

def extrair_texto(caminho_arquivo: str) -> str:
    ext = caminho_arquivo.lower().split('.')[-1]
    print(f"📄 Processando: {caminho_arquivo}")

    if ext == 'pdf':
        paginas = convert_from_path(caminho_arquivo, dpi=300)
        return "\n".join(
            pytesseract.image_to_string(p, lang='por+eng', config='--psm 6')
            for p in paginas
        ).strip()

    elif ext in ['jpg', 'jpeg', 'png']:
        img = Image.open(caminho_arquivo).convert('L')
        return pytesseract.image_to_string(img, lang='por+eng', config='--psm 6').strip()

    return "❌ Formato não suportado. Use PDF, JPG ou PNG."
