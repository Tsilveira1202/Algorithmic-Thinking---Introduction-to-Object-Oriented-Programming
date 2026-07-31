"""
Módulo de Orçamento — R.M Imobiliária
=======================================
Define as classes Orcamento e ExportadorCSV, responsáveis
por gerar e exportar o orçamento de aluguel.
"""

import csv
import os
from datetime import datetime

from models.imovel import Imovel
from models.contrato import Contrato


def formatar_moeda(valor: float) -> str:
    """Formata valor numérico para padrão monetário brasileiro (ex: R$ 1.200,00)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class Orcamento:
    """
    Gera o orçamento completo de aluguel mensal.

    Combina as informações do imóvel e do contrato para
    produzir um orçamento com 12 parcelas mensais.

    Atributos:
        imovel (Imovel): Instância do imóvel escolhido.
        contrato (Contrato): Instância do contrato imobiliário.
        nome_cliente (str): Nome do cliente.
    """

    MESES_ORCAMENTO = 12

    def __init__(self, imovel: Imovel, contrato: Contrato, nome_cliente: str = "Cliente"):
        self._imovel = imovel
        self._contrato = contrato
        self._nome_cliente = nome_cliente
        self._data_geracao = datetime.now()

    # --- Propriedades ---

    @property
    def imovel(self) -> Imovel:
        """Retorna o imóvel do orçamento."""
        return self._imovel

    @property
    def contrato(self) -> Contrato:
        """Retorna o contrato do orçamento."""
        return self._contrato

    @property
    def nome_cliente(self) -> str:
        """Retorna o nome do cliente."""
        return self._nome_cliente

    @property
    def data_geracao(self) -> datetime:
        """Retorna a data de geração do orçamento."""
        return self._data_geracao

    # --- Métodos de cálculo ---

    def valor_aluguel_mensal(self) -> float:
        """Retorna o valor do aluguel mensal calculado pelo imóvel."""
        return self._imovel.calcular_aluguel()

    def valor_total_12_meses(self) -> float:
        """Retorna o valor total de 12 meses de aluguel."""
        return round(self.valor_aluguel_mensal() * self.MESES_ORCAMENTO, 2)

    def gerar_parcelas(self) -> list:
        """
        Gera a lista de 12 parcelas mensais do orçamento,
        incluindo a projeção do contrato e total acumulado.

        Retorna:
            list: Lista de dicionários com mês, aluguel, parcela do contrato e total.
        """
        aluguel = self.valor_aluguel_mensal()
        num_parcelas_contrato = self._contrato.parcelas
        valor_parcela_contrato = self._contrato.calcular_parcela()

        parcelas = []
        acumulado = 0.0

        for mes in range(1, self.MESES_ORCAMENTO + 1):
            # Parcela do contrato é devida apenas até o número de parcelas escolhido (1x a 5x)
            parcela_contrato = valor_parcela_contrato if mes <= num_parcelas_contrato else 0.0
            total_mes = aluguel + parcela_contrato
            acumulado += total_mes

            parcelas.append({
                "mes": mes,
                "descricao": f"Mês {mes:02d}",
                "aluguel": aluguel,
                "parcela_contrato": parcela_contrato,
                "total_mes": total_mes,
                "acumulado": acumulado,
            })

        return parcelas

    def resumo(self) -> dict:
        """
        Gera um resumo completo do orçamento.

        Retorna:
            dict: Dicionário com todas as informações do orçamento.
        """
        return {
            "cliente": self._nome_cliente,
            "data": self._data_geracao.strftime("%d/%m/%Y %H:%M"),
            "imovel_tipo": self._imovel.tipo,
            "imovel_quartos": self._imovel.quartos,
            "imovel_garagem": self._imovel.garagem,
            "detalhes_calculo": self._imovel.detalhar_calculo(),
            "aluguel_mensal": self.valor_aluguel_mensal(),
            "total_12_meses": self.valor_total_12_meses(),
            "contrato_valor": self._contrato.valor,
            "contrato_parcelas": self._contrato.parcelas,
            "contrato_valor_parcela": self._contrato.calcular_parcela(),
            "parcelas": self.gerar_parcelas(),
        }

    def __str__(self) -> str:
        aluguel = self.valor_aluguel_mensal()
        return (
            f"Orçamento R.M Imobiliária\n"
            f"Cliente: {self._nome_cliente}\n"
            f"Imóvel: {self._imovel}\n"
            f"Aluguel Mensal: {formatar_moeda(aluguel)}\n"
            f"Total 12 meses: {formatar_moeda(self.valor_total_12_meses())}\n"
            f"Contrato: {self._contrato}"
        )


class ExportadorCSV:
    """
    Exporta o orçamento para um arquivo CSV formatado e profissional.

    O arquivo é gerado no formato PT-BR (delimitado por ponto e vírgula ';',
    com codificação UTF-8 com BOM) para abertura perfeita no Microsoft Excel.
    """

    @staticmethod
    def exportar(orcamento: Orcamento, caminho: str = None) -> str:
        """
        Exporta o orçamento para um arquivo .csv altamente estruturado.

        Args:
            orcamento: Instância de Orcamento a ser exportada.
            caminho: Caminho do arquivo CSV (opcional).

        Retorna:
            str: Caminho do arquivo CSV gerado.
        """
        if caminho is None:
            caminho = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "orcamento.csv"
            )

        resumo = orcamento.resumo()
        parcelas = resumo["parcelas"]
        div = "=" * 80

        with open(caminho, mode="w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            # ----------------------------------------------------
            # CABEÇALHO DO RELATÓRIO
            # ----------------------------------------------------
            escritor.writerow(["R.M IMOBILIÁRIA — RELATÓRIO DE ORÇAMENTO DE LOCAÇÃO", "", "", "", "", ""])
            escritor.writerow([div, "", "", "", "", ""])
            escritor.writerow(["Cliente:", resumo["cliente"], "", "Data de Emissão:", resumo["data"], ""])
            escritor.writerow(["Tipo de Imóvel:", resumo["imovel_tipo"], "", "Quartos:", resumo["imovel_quartos"], ""])
            escritor.writerow(["Garagem / Estacionamento:", "Sim" if resumo["imovel_garagem"] else "Não", "", "", "", ""])
            escritor.writerow([])

            # ----------------------------------------------------
            # COMPOSIÇÃO DA MENSALIDADE
            # ----------------------------------------------------
            escritor.writerow(["1. COMPOSIÇÃO DO ALUGUEL MENSAL", "", "", "", "", ""])
            escritor.writerow(["Item / Descrição", "Tipo", "Valor (R$)", "", "", ""])
            escritor.writerow(["-" * 40, "-" * 15, "-" * 15, "", "", ""])

            for descricao, valor in resumo["detalhes_calculo"]:
                tipo_item = "Desconto" if valor < 0 else "Base/Adicional"
                escritor.writerow([descricao, tipo_item, formatar_moeda(valor), "", "", ""])

            escritor.writerow(["-" * 40, "-" * 15, "-" * 15, "", "", ""])
            escritor.writerow(["VALOR FINAL DO ALUGUEL MENSAL", "MENSALIDADE", formatar_moeda(resumo["aluguel_mensal"]), "", "", ""])
            escritor.writerow([])

            # ----------------------------------------------------
            # CONTRATO IMOBILIÁRIO
            # ----------------------------------------------------
            escritor.writerow(["2. CONTRATO IMOBILIÁRIO (TAXA ÚNICA)", "", "", "", "", ""])
            escritor.writerow(["Valor Total do Contrato:", formatar_moeda(resumo["contrato_valor"]), "", "", "", ""])
            escritor.writerow(["Condição de Pagamento:", f"{resumo['contrato_parcelas']}x de {formatar_moeda(resumo['contrato_valor_parcela'])}", "", "", "", ""])
            escritor.writerow([])

            # ----------------------------------------------------
            # TABELA DE 12 PARCELAS (CRONOGRAMA FINANCEIRO)
            # ----------------------------------------------------
            escritor.writerow(["3. CRONOGRAMA FINANCEIRO DE PAGAMENTOS (12 MESES)", "", "", "", "", ""])
            escritor.writerow([
                "Mês",
                "Descrição",
                "Aluguel Mensal (R$)",
                "Parcela Contrato (R$)",
                "Total Mensal (R$)",
                "Total Acumulado (R$)"
            ])
            escritor.writerow(["-" * 6, "-" * 15, "-" * 20, "-" * 20, "-" * 20, "-" * 20])

            total_aluguel = 0.0
            total_contrato = 0.0
            total_geral = 0.0

            for p in parcelas:
                total_aluguel += p["aluguel"]
                total_contrato += p["parcela_contrato"]
                total_geral += p["total_mes"]

                escritor.writerow([
                    f"{p['mes']:02d}",
                    p["descricao"],
                    formatar_moeda(p["aluguel"]),
                    formatar_moeda(p["parcela_contrato"]) if p["parcela_contrato"] > 0 else "R$ 0,00",
                    formatar_moeda(p["total_mes"]),
                    formatar_moeda(p["acumulado"])
                ])

            escritor.writerow(["-" * 6, "-" * 15, "-" * 20, "-" * 20, "-" * 20, "-" * 20])
            escritor.writerow([
                "TOTAL",
                "12 Meses",
                formatar_moeda(total_aluguel),
                formatar_moeda(total_contrato),
                formatar_moeda(total_geral),
                formatar_moeda(total_geral)
            ])
            escritor.writerow([])

            # ----------------------------------------------------
            # RODAPÉ E NOTAS
            # ----------------------------------------------------
            escritor.writerow(["RESUMO GERAL DA LOCAÇÃO", "", "", "", "", ""])
            escritor.writerow(["Total de Aluguel (12 meses):", formatar_moeda(total_aluguel), "", "", "", ""])
            escritor.writerow(["Total do Contrato Imobiliário:", formatar_moeda(total_contrato), "", "", "", ""])
            escritor.writerow(["INVESTIMENTO TOTAL NO PERÍODO (1 ANO):", formatar_moeda(total_geral), "", "", "", ""])
            escritor.writerow([div, "", "", "", "", ""])
            escritor.writerow(["Documento gerado automaticamente pelo Sistema R.M Imobiliária", "", "", "", "", ""])

        return caminho
