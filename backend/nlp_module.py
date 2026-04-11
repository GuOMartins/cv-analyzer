import spacy, re
from nltk.corpus import stopwords

nlp = spacy.load("pt_core_news_sm")

HABILIDADES_TECNICAS = {
    "python","java","javascript","typescript","c++","c#","go","rust",
    "kotlin","swift","php","ruby","scala","django","flask","fastapi",
    "react","vue","angular","node","spring","laravel","rails",
    "postgresql","mysql","mongodb","redis","sqlite","oracle",
    "docker","kubernetes","aws","azure","gcp","git","github",
    "jenkins","terraform","ansible","pandas","numpy","scikit-learn",
    "tensorflow","pytorch","spark","hadoop","power bi","tableau",
    "sql","nosql","rest","api","microservices","agile","scrum",
}

def limpar_texto(texto):
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'[^\w\s@.\-,/()áéíóúâêîôûãõàèìòùç]', '', texto, flags=re.IGNORECASE)
    return texto.strip()

def extrair_email(texto):
    r = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', texto)
    return r[0] if r else "Não encontrado"

def extrair_telefone(texto):
    r = re.findall(r'(\(?\d{2}\)?\s?\d{4,5}[-\s]?\d{4})', texto)
    return r[0] if r else "Não encontrado"

def extrair_habilidades(texto):
    tl = texto.lower()
    return sorted([h for h in HABILIDADES_TECNICAS
                   if re.search(r'\b' + re.escape(h) + r'\b', tl)])

def extrair_entidades(texto):
    doc = nlp(texto[:5000])
    res = {"pessoas": [], "organizacoes": [], "datas": [], "locais": []}
    mapa = {"PER": "pessoas", "ORG": "organizacoes", "DATE": "datas",
            "LOC": "locais", "GPE": "locais"}
    for ent in doc.ents:
        if ent.label_ in mapa:
            res[mapa[ent.label_]].append(ent.text)
    for k in res:
        res[k] = list(set(res[k]))
    return res

def analisar_curriculo(texto):
    tl = limpar_texto(texto)
    return {
        "texto_limpo": tl,
        "email": extrair_email(tl),
        "telefone": extrair_telefone(tl),
        "habilidades": extrair_habilidades(tl),
        "entidades": extrair_entidades(tl),
    }
