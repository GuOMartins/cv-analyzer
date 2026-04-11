import gradio as gr
from ocr_module import extrair_texto
from nlp_module import analisar_curriculo
from ranker import calcular_score

def processar(arquivo, descricao_vaga):
    if arquivo is None:            return "❌ Envie um currículo.", "", "", ""
    if not descricao_vaga.strip(): return "❌ Descreva a vaga.",    "", "", ""
    try:
        texto_bruto = extrair_texto(arquivo.name)
        if not texto_bruto:        return "❌ Não consegui extrair texto.", "", "", ""

        analise = analisar_curriculo(texto_bruto)
        r = calcular_score(analise["texto_limpo"], descricao_vaga, analise["habilidades"])

        principal = (
            f"## {r['classificacao']}\n"
            f"**Score:** {r['score']} / 100 — {r['recomendacao']}\n\n---\n"
            f"📊 Similaridade textual: **{r['sim_textual']}%** · "
            f"🛠️ Match de habilidades: **{r['match_hab']}%**"
        )
        habilidades = (
            f"**✅ Em comum com a vaga:** {', '.join(r['em_comum']) or 'Nenhuma'}\n\n"
            f"**➕ Extras do candidato:** {', '.join(r['extras']) or 'Nenhuma'}"
        )
        ent  = analise["entidades"]
        info = (
            f"**📧 E-mail:** {analise['email']}\n\n"
            f"**📞 Telefone:** {analise['telefone']}\n\n"
            f"**🏢 Organizações:** {', '.join(ent['organizacoes'][:5]) or 'Não identificadas'}\n\n"
            f"**📅 Datas:** {', '.join(ent['datas'][:5]) or 'Não identificadas'}"
        )
        ocr_preview = texto_bruto[:1500] + ("..." if len(texto_bruto) > 1500 else "")
        return principal, habilidades, info, ocr_preview

    except Exception as e:
        return f"❌ Erro: {e}", "", "", ""


with gr.Blocks(title="Analisador de Currículos", theme=gr.themes.Soft()) as app:
    gr.Markdown("# 🤖 Analisador de Currículos com OCR + IA")
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📤 Entrada")
            arquivo_in = gr.File(label="Currículo (PDF, JPG ou PNG)",
                                 file_types=[".pdf", ".jpg", ".jpeg", ".png"])
            vaga_in    = gr.Textbox(label="Descrição da vaga",
                                    placeholder="Cole aqui os requisitos da vaga...",
                                    lines=8)
            btn        = gr.Button("🔍 Analisar", variant="primary", size="lg")
        with gr.Column():
            gr.Markdown("### 📊 Resultado")
            out_score = gr.Markdown()
            out_hab   = gr.Markdown()
            out_info  = gr.Markdown()
    with gr.Accordion("📄 Texto extraído pelo OCR", open=False):
        out_ocr = gr.Textbox(lines=10)
    btn.click(fn=processar,
              inputs=[arquivo_in, vaga_in],
              outputs=[out_score, out_hab, out_info, out_ocr])

if __name__ == "__main__":
    app.launch(share=True)
