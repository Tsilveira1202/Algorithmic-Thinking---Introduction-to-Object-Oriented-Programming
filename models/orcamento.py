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
        Gera a lista de 12 parcelas mensais do orçamento.

        Retorna:
            list: Lista de dicionários com mês e valor do aluguel.
        """
        aluguel = self.valor_aluguel_mensal()
        parcelas = []

        for mes in range(1, self.MESES_ORCAMENTO + 1):
            parcelas.append({
                "mes": mes,
                "descricao": f"Mês {mes:02d}",
                "aluguel": aluguel,
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
            f"Aluguel Mensal: R$ {aluguel:,.2f}\n"
            f"Total 12 meses: R$ {self.valor_total_12_meses():,.2f}\n"
            f"Contrato: {self._contrato}"
        )


class ExportadorCSV:
    """
    Exporta o orçamento para um arquivo CSV.

    O arquivo gerado contém as 12 parcelas mensais com
    detalhes do aluguel para cada mês.
    """

    @staticmethod
    def exportar(orcamento: Orcamento, caminho: str = None) -> str:
        """
        Exporta o orçamento para um arquivo .csv.

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

        with open(caminho, mode="w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            # Cabeçalho com informações do orçamento
            escritor.writerow(["ORÇAMENTO R.M IMOBILIÁRIA"])
            escritor.writerow(["Cliente", resumo["cliente"]])
            escritor.writerow(["Data", resumo["data"]])
            escritor.writerow(["Tipo de Imóvel", resumo["imovel_tipo"]])
            escritor.writerow(["Quartos", resumo["imovel_quartos"]])
            escritor.writerow(["Garagem/Estacionamento", "Sim" if resumo["imovel_garagem"] else "Não"])
            escritor.writerow([])

            # Detalhamento do cálculo
            escritor.writerow(["DETALHAMENTO DO CÁLCULO"])
            for descricao, valor in resumo["detalhes_calculo"]:
                escritor.writerow([descricao, f"R$ {valor:,.2f}"])
            escritor.writerow(["ALUGUEL MENSAL", f"R$ {resumo['aluguel_mensal']:,.2f}"])
            escritor.writerow([])

            # Contrato
            escritor.writerow(["CONTRATO IMOBILIÁRIO"])
            escritor.writerow(["Valor Total", f"R$ {resumo['contrato_valor']:,.2f}"])
            escritor.writerow(["Parcelas", f"{resumo['contrato_parcelas']}x de R$ {resumo['contrato_valor_parcela']:,.2f}"])
            escritor.writerow([])

            # Tabela de 12 parcelas
            escritor.writerow(["PARCELAS DO ORÇAMENTO (12 MESES)"])
            escritor.writerow(["Mês", "Descrição", "Valor do Aluguel"])

            for parcela in parcelas:
                escritor.writerow([
                    parcela["mes"],
                    parcela["descricao"],
                    f"R$ {parcela['aluguel']:,.2f}",
                ])

            escritor.writerow([])
            escritor.writerow(["TOTAL 12 MESES", "", f"R$ {resumo['total_12_meses']:,.2f}"])

        return caminho
