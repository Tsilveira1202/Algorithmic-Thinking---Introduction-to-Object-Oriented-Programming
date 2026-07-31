"""
Módulo de Contrato — R.M Imobiliária
======================================
Define a classe Contrato, responsável por gerenciar
o contrato imobiliário e seu parcelamento.
"""


class Contrato:
    """
    Representa o contrato imobiliário da R.M Imobiliária.

    Regras de negócio:
        - Valor fixo: R$ 2.000,00
        - Parcelamento: de 1 a 5 vezes

    Atributos:
        valor (float): Valor total do contrato.
        parcelas (int): Número de parcelas escolhido (1 a 5).
    """

    VALOR_CONTRATO = 2000.00
    MAX_PARCELAS = 5

    def __init__(self, parcelas: int = 1):
        if not 1 <= parcelas <= self.MAX_PARCELAS:
            raise ValueError(
                f"O número de parcelas deve ser entre 1 e {self.MAX_PARCELAS}. "
                f"Valor recebido: {parcelas}"
            )
        self._parcelas = parcelas

    # --- Propriedades (encapsulamento) ---

    @property
    def valor(self) -> float:
        """Retorna o valor total do contrato."""
        return self.VALOR_CONTRATO

    @property
    def parcelas(self) -> int:
        """Retorna o número de parcelas."""
        return self._parcelas

    # --- Métodos de cálculo ---

    def calcular_parcela(self) -> float:
        """
        Calcula o valor de cada parcela do contrato.

        Retorna:
            float: Valor de cada parcela (valor_contrato / num_parcelas).
        """
        return round(self.VALOR_CONTRATO / self._parcelas, 2)

    def __str__(self) -> str:
        parcela = self.calcular_parcela()
        return (
            f"Contrato R.M Imobiliária | "
            f"Total: R$ {self.VALOR_CONTRATO:,.2f} | "
            f"{self._parcelas}x de R$ {parcela:,.2f}"
        )
