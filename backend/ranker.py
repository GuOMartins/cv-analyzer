from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import re

try:
    STOPWORDS_PT = set(stopwords.words('portuguese'))
except:
    STOPWORDS_PT = set()

def preprocessar(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', ' ', texto)
    return ' '.join([p for p in texto.split()
                     if p not in STOPWORDS_PT and len(p) > 2])

def calcular_score(texto_curriculo, texto_vaga, habilidades):
    c, v = preprocessar(texto_curriculo), preprocessar(texto_vaga)
    try:
        mat = TfidfVectorizer().fit_transform([c, v])
        sim_tfidf = float(cosine_similarity(mat[0:1], mat[1:2])[0][0])
    except:
        sim_tfidf = 0.0

    vl = texto_vaga.lower()
    em_comum = [h for h in habilidades if h in vl]
    extras   = [h for h in habilidades if h not in vl]
    pct_hab  = len(em_comum) / max(len(habilidades), 1)
    score    = round(min((sim_tfidf * 0.6 + pct_hab * 0.4) * 100, 100), 1)

    if score >= 75:   cls, rec = "🟢 Alta compatibilidade",       "Candidato fortemente recomendado!"
    elif score >= 50: cls, rec = "🟡 Média compatibilidade",       "Candidato com potencial."
    elif score >= 25: cls, rec = "🟠 Baixa compatibilidade",       "Candidato com lacunas relevantes."
    else:             cls, rec = "🔴 Muito baixa compatibilidade", "Perfil distante da vaga."

    return {
        "score": score, "classificacao": cls, "recomendacao": rec,
        "sim_textual": round(sim_tfidf * 100, 1),
        "match_hab": round(pct_hab * 100, 1),
        "em_comum": em_comum, "extras": extras,
    }
