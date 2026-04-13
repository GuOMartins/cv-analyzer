# 🤖 CV Analyzer — Análise de Currículos com OCR + IA

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tesseract](https://img.shields.io/badge/OCR-Tesseract-FF6B35?style=for-the-badge&logo=google&logoColor=white)
![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Gradio](https://img.shields.io/badge/Interface-Gradio-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-Google-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Replicando o que os recrutadores fazem com IA — de forma open source, transparente e educacional.**

[🚀 Abrir no Google Colab](#como-rodar) · [🎯 Demo](#demonstração) · [📖 Sobre o Projeto](#sobre-o-projeto)

</div>

---

## 📌 Sobre o Projeto

Empresas de recrutamento utilizam sistemas de **ATS (Applicant Tracking System)** para filtrar currículos automaticamente com IA antes mesmo de um humano ler. Este projeto **replica e torna transparente** essa tecnologia usando ferramentas 100% open source.

O **CV Analyzer** é um pipeline completo que:

1. **Extrai texto** de currículos em PDF ou imagem via OCR
2. **Analisa o conteúdo** com Processamento de Linguagem Natural (NLP)
3. **Compara** o perfil do candidato com a descrição de uma vaga
4. **Gera um score** de compatibilidade com explicação detalhada
5. **Exibe tudo** em uma interface web interativa

> 💡 **Por que isso importa?** Entender como os sistemas de triagem funcionam ajuda candidatos a otimizarem seus currículos e ajuda profissionais de RH a compreenderem as limitações dessas ferramentas.

---

## 🎬 Demonstração

[CV Analyzer em funcionamento](assets/app-demo.gif)

[Resultado com score de compatibilidade](assets/resultado_score.png)

```
┌─────────────────────────────────────────────────────────┐
│  📤 Upload: curriculo_joao.pdf                          │
│  📝 Vaga: "Desenvolvedor Python com Django e Docker"    │
│                                                         │
│  ✅ RESULTADO                                           │
│  ┌───────────────────────────────────────────────────┐  │
│  │  🟢 Alta compatibilidade — Score: 82.4/100        │  │
│  │                                                   │  │
│  │  Habilidades em comum: python, django, docker     │  │
│  │  Similaridade textual: 78%                        │  │
│  │  Match de habilidades: 90%                        │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## 🏗️ Arquitetura

```
curriculo.pdf / imagem
        │
        ▼
┌───────────────────┐
│   Módulo OCR      │  ← Tesseract + pdf2image
│  (ocr_module.py)  │    Extrai texto bruto
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   Módulo NLP      │  ← spaCy + NLTK + Regex
│  (nlp_module.py)  │    Entidades, habilidades, contatos
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Motor de Ranking │  ← TF-IDF + Similaridade de Cosseno
│    (ranker.py)    │    Score 0-100 contra a vaga
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Interface Web    │  ← Gradio
│     (app.py)      │    Upload, resultado, explicação
└───────────────────┘
```

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Por que foi escolhida |
|--------|-----------|----------------------|
| **OCR** | Tesseract 5 + pdf2image | Motor OCR mais robusto open source, mantido pelo Google |
| **NLP** | spaCy (pt_core_news_sm) | NER em português, rápido e preciso para produção |
| **Tokenização** | NLTK | Stopwords e pré-processamento de texto em PT |
| **Ranking IA** | scikit-learn (TF-IDF) | Vetorização e similaridade de cosseno — técnica usada em sistemas reais de ATS |
| **Interface** | Gradio 4 | Interface web funcional em poucas linhas, ideal para MVP e demos |
| **Ambiente** | Google Colab | Acessível sem configuração local, GPU gratuita disponível |

---

## 🧠 Técnicas de IA Aplicadas

### TF-IDF (Term Frequency-Inverse Document Frequency)
Converte textos em vetores numéricos, pesando palavras pela sua raridade e frequência. Permite comparar matematicamente dois documentos (currículo e vaga).

### Similaridade de Cosseno
Mede o ângulo entre dois vetores de texto. Quanto mais próximo de 1, mais similares os documentos. Técnica padrão em sistemas de recuperação de informação.

### NER — Named Entity Recognition
O spaCy identifica automaticamente nomes de pessoas, organizações, datas e locais dentro do texto extraído do currículo.

### Pipeline de pré-processamento NLP
- Limpeza de ruído do OCR
- Remoção de stopwords
- Extração de habilidades por pattern matching
- Normalização de texto

---

## 📁 Estrutura do Projeto

```
cv-analyzer/
│
├── backend/
│   ├── app.py              # Interface Gradio — ponto de entrada
│   ├── ocr_module.py       # Extração de texto via Tesseract
│   ├── nlp_module.py       # Análise NLP com spaCy
│   └── ranker.py           # Score TF-IDF + Cosseno
│
├── data/
│   ├── raw/                # Currículos originais (não versionados)
│   └── processed/          # Textos extraídos
│
├── utils/
│   └── constants.py        # Lista de habilidades técnicas
│
├── assets/
│   └── demo_screenshot.png # Screenshot da interface
│
├── notebooks/
│   └── cv_analyzer_colab.ipynb  # Notebook completo para Colab
│
├── requirements.txt        # Dependências Python
├── .gitignore
├── LICENSE
└── README.md
```

---

Abaixo está o texto pronto para você **copiar e colar diretamente** no seu `README.md`, substituindo a seção antiga de "Como Rodar".

```markdown
## 🚀 Como Rodar o Projeto (passo a passo)

### ▶️ Opção 1 — Google Colab (recomendado para quem só quer testar)

> ✅ **Nenhuma instalação necessária** – tudo roda no seu navegador.

1. Clique no botão abaixo:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GuOMartins/cv-analyzer/blob/main/notebooks/cv_analyzer_colab.ipynb)

2. No Colab, execute as células em ordem:  
   `Runtime → Run all`

3. Ao final, clique no link gerado (ex: `http://127.0.0.1:7860`) – a interface do CV Analyzer abrirá.

> 💡 **Dica:** O Colab é gratuito e não precisa de computador potente.

---

### 💻 Opção 2 — Rodar no seu computador (para desenvolvedores)

> ⚠️ **Pré-requisito:** Ter Python 3.10 ou superior instalado.  
> (Para verificar, digite `python --version` no terminal.)

#### 1. Baixar o projeto

```bash
git clone https://github.com/GuOMartins/cv-analyzer.git
cd cv-analyzer
```

#### 2. Criar e ativar um ambiente virtual (recomendado)

**Criar o ambiente:**

```bash
python -m venv venv
```

**Ativar o ambiente:**

| Sistema | Comando |
|---------|---------|
| Windows | `venv\Scripts\activate` |
| Linux / Mac | `source venv/bin/activate` |

Após ativar, você verá `(venv)` no início da linha do terminal.

> 💡 Para desativar depois, basta digitar `deactivate`.

#### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

#### 4. Instalar o Tesseract OCR (necessário para ler imagens)

| Sistema | Como instalar |
|---------|----------------|
| **Windows** | Baixe o instalador em [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki) (ex: `tesseract-ocr-w64-setup-5.3.3.20231005.exe`). Durante a instalação, marque a opção **"Add Tesseract to PATH"**. |
| **Linux (Ubuntu/Debian)** | `sudo apt-get install tesseract-ocr tesseract-ocr-por` |
| **Mac** | `brew install tesseract tesseract-lang` |

> 🔍 Para testar se o Tesseract foi instalado corretamente, digite `tesseract --version`.

#### 5. Baixar o modelo de linguagem em português (spaCy)

```bash
python -m spacy download pt_core_news_sm
```

#### 6. Iniciar a aplicação

```bash
python backend/app.py
```

- O Gradio iniciará um servidor local.  
- Abra o link exibido no terminal (geralmente `http://localhost:7860`).

---

### 🎯 Agora é só testar!

- Faça upload de um currículo (PDF ou imagem)  
- Digite a descrição de uma vaga  
- Clique em "Analisar" e veja o score de compatibilidade

---

## 📌 Resumo para os apressados (apenas comandos)

```bash
git clone https://github.com/GuOMartins/cv-analyzer.git
cd cv-analyzer
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
python backend/app.py
```
```

Apenas copie todo o bloco acima e **cole no lugar da seção anterior** que falava sobre "Como Rodar". O resto do seu README permanece igual.

---

## 📦 Dependências

```
pytesseract==0.3.10
pdf2image==1.16.3
Pillow==10.0.0
spacy==3.7.2
nltk==3.8.1
scikit-learn==1.3.0
gradio==4.7.1
python-docx==1.0.1
numpy==1.24.0
```

---

## 🗺️ Roadmap

- [x] Pipeline OCR → NLP → Ranking funcional
- [x] Interface web com Gradio
- [x] Suporte a PDF e imagens
- [ ] Suporte a arquivos `.docx`
- [ ] Comparação de múltiplos currículos simultaneamente
- [ ] Exportar relatório em PDF
- [ ] Modelo de NLP treinado especificamente para currículos
- [ ] Deploy no Hugging Face Spaces (acesso público permanente)
- [ ] Score por seções (formação, experiência, habilidades separadamente)

---

## ⚠️ Limitações e Considerações Éticas

- A qualidade do OCR depende da qualidade do currículo (fontes, formatação, resolução)
- O ranking por TF-IDF é uma aproximação — não substitui análise humana
- Sistemas de ATS reais utilizam modelos mais sofisticados e dados proprietários
- **Este projeto é educacional** — seu uso em processos seletivos reais requer validação rigorosa e conformidade com LGPD

---

## 🤝 Como Contribuir

Contribuições são bem-vindas!

```bash
# Fork → Clone → Branch → Commit → Pull Request
git checkout -b feature/minha-melhoria
git commit -m "feat: adiciona suporte a docx"
git push origin feature/minha-melhoria
```

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 👤 Autor

Desenvolvido como projeto de portfólio em IA aplicada a RH Tech.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/gustavoomartins)
[![GitHub](https://img.shields.io/badge/GitHub-Seguir-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GuOMartins)

<div align="center">
  <sub>⭐ Se este projeto foi útil, deixe uma estrela — ajuda muito!</sub>
</div>
