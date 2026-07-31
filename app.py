"""
App Principal — R.M Imobiliária
================================
Servidor Flask que gerencia as rotas da aplicação
de orçamento de aluguel.

Rotas:
    GET  /                → Formulário de orçamento
    POST /gerar           → Processa formulário e exibe resultado
    GET  /exportar_excel  → Download de planilha Excel estilizada (.xlsx)
    GET  /exportar_csv    → Download do arquivo CSV com 12 parcelas
"""

import os
from flask import Flask, render_template, request, send_file, session

from models.imovel import Apartamento, Casa, Estudio
from models.contrato import Contrato
from models.orcamento import Orcamento, ExportadorCSV, ExportadorExcel


# --- Inicialização do Flask ---
app = Flask(__name__)
app.secret_key = "rm_imobiliaria_2025"

# Variável global para manter o último orçamento gerado
ultimo_orcamento = None


@app.route("/")
def index():
    """
    Rota principal — exibe o formulário de orçamento.
    """
    return render_template("index.html", resultado=None)


@app.route("/favicon.ico")
def favicon():
    """
    Evita erro 404 no log do servidor quando o navegador busca o favicon.
    """
    return "", 204


@app.route("/gerar", methods=["POST"])
def gerar_orcamento():
    """
    Processa o formulário e gera o orçamento.
    """
    global ultimo_orcamento

    # --- 1. Captura os dados do formulário ---
    nome_cliente = request.form.get("nome_cliente", "Cliente")
    tipo_imovel = request.form.get("tipo_imovel", "apartamento")
    quartos = int(request.form.get("quartos", 1))
    garagem = request.form.get("garagem") == "sim"
    tem_criancas = request.form.get("tem_criancas") == "sim"
    estacionamento = request.form.get("estacionamento") == "sim"
    vagas_extras = int(request.form.get("vagas_extras", 0))
    parcelas_contrato = int(request.form.get("parcelas_contrato", 1))

    # --- 2. Cria a instância do imóvel (polimorfismo) ---
    if tipo_imovel == "apartamento":
        imovel = Apartamento(
            quartos=quartos,
            garagem=garagem,
            tem_criancas=tem_criancas
        )
    elif tipo_imovel == "casa":
        imovel = Casa(
            quartos=quartos,
            garagem=garagem
        )
    else:  # estudio
        imovel = Estudio(
            estacionamento=estacionamento,
            vagas_extras=vagas_extras
        )

    # --- 3. Cria o contrato ---
    contrato = Contrato(parcelas=parcelas_contrato)

    # --- 4. Gera o orçamento ---
    orcamento = Orcamento(
        imovel=imovel,
        contrato=contrato,
        nome_cliente=nome_cliente
    )

    # Armazena para exportação
    ultimo_orcamento = orcamento

    # --- 5. Envia o resumo para o template ---
    resultado = orcamento.resumo()

    return render_template("index.html", resultado=resultado)


@app.route("/exportar_excel")
def exportar_excel():
    """
    Exporta o orçamento para uma planilha Excel (.xlsx) altamente estilizada,
    com cores corporativas, fontes, bordas e fórmulas nativas.
    """
    global ultimo_orcamento

    if ultimo_orcamento is None:
        return "Nenhum orçamento foi gerado ainda. Volte e gere um orçamento primeiro.", 400

    caminho_xlsx = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "orcamento.xlsx"
    )

    ExportadorExcel.exportar(ultimo_orcamento, caminho_xlsx)

    return send_file(
        caminho_xlsx,
        as_attachment=True,
        download_name="orcamento_rm_imobiliaria.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@app.route("/exportar_csv")
def exportar_csv():
    """
    Exporta o último orçamento gerado para um arquivo CSV (.csv).
    """
    global ultimo_orcamento

    if ultimo_orcamento is None:
        return "Nenhum orçamento foi gerado ainda. Volte e gere um orçamento primeiro.", 400

    caminho_csv = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "orcamento.csv"
    )

    ExportadorCSV.exportar(ultimo_orcamento, caminho_csv)

    return send_file(
        caminho_csv,
        as_attachment=True,
        download_name="orcamento_rm_imobiliaria.csv",
        mimetype="text/csv"
    )


# --- Ponto de entrada ---
if __name__ == "__main__":
    print("=" * 50)
    print("  R.M Imobiliária — Orçamento de Aluguel")
    print("  Acesse: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True)
