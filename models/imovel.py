"""
Módulo de Imóveis — R.M Imobiliária
====================================
Define a hierarquia de classes para os tipos de imóveis:
- Imovel (classe base abstrata)
  ├── Apartamento
  ├── Casa
  └── Estudio

Utiliza herança e polimorfismo para calcular o aluguel
mensal de cada tipo de imóvel com suas regras específicas.
"""

from abc import ABC, abstractmethod


class Imovel(ABC):
    """
    Classe base abstrata que representa um imóvel genérico.

    Atributos:
        tipo (str): Tipo do imóvel (ex: 'Apartamento', 'Casa', 'Estúdio').
        quartos (int): Número de quartos do imóvel.
        garagem (bool): Indica se possui vaga de garagem.

    Método abstrato:
        calcular_aluguel(): Cada subclasse implementa sua própria
        lógica de cálculo do valor mensal do aluguel.
    """

    def __init__(self, tipo: str, quartos: int = 1, garagem: bool = False):
        self._tipo = tipo
        self._quartos = quartos
        self._garagem = garagem

    # --- Propriedades (encapsulamento) ---

    @property
    def tipo(self) -> str:
        """Retorna o tipo do imóvel."""
        return self._tipo

    @property
    def quartos(self) -> int:
        """Retorna o número de quartos."""
        return self._quartos

    @property
    def garagem(self) -> bool:
        """Indica se possui vaga de garagem."""
        return self._garagem

    # --- Método abstrato (polimorfismo) ---

    @abstractmethod
    def calcular_aluguel(self) -> float:
        """
        Calcula o valor mensal do aluguel.
        Deve ser implementado por cada subclasse.
        """
        pass

    @abstractmethod
    def detalhar_calculo(self) -> list:
        """
        Retorna uma lista de tuplas (descrição, valor) detalhando
        cada componente do cálculo do aluguel.
        """
        pass

    def __str__(self) -> str:
        return (
            f"{self._tipo} | {self._quartos} quarto(s) | "
            f"Garagem: {'Sim' if self._garagem else 'Não'} | "
            f"Aluguel: R$ {self.calcular_aluguel():,.2f}"
        )


class Apartamento(Imovel):
    """
    Representa um apartamento para locação.

    Regras de negócio:
        - Valor base: R$ 700,00 (1 quarto)
        - 2 quartos: + R$ 200,00
        - Garagem: + R$ 300,00
        - Sem crianças: desconto de 5% sobre o aluguel
    """

    VALOR_BASE = 700.00
    ACRESCIMO_SEGUNDO_QUARTO = 200.00
    VALOR_GARAGEM = 300.00
    DESCONTO_SEM_CRIANCAS = 0.05  # 5%

    def __init__(self, quartos: int = 1, garagem: bool = False, tem_criancas: bool = True):
        super().__init__(tipo="Apartamento", quartos=quartos, garagem=garagem)
        self._tem_criancas = tem_criancas

    @property
    def tem_criancas(self) -> bool:
        """Indica se há crianças no grupo familiar."""
        return self._tem_criancas

    def calcular_aluguel(self) -> float:
        """
        Calcula o aluguel mensal do apartamento.

        Fórmula:
            aluguel = 700 + (200 se 2 quartos) + (300 se garagem)
            Se não tem crianças: aluguel *= 0.95 (desconto de 5%)
        """
        valor = self.VALOR_BASE

        if self._quartos == 2:
            valor += self.ACRESCIMO_SEGUNDO_QUARTO

        if self._garagem:
            valor += self.VALOR_GARAGEM

        if not self._tem_criancas:
            valor *= (1 - self.DESCONTO_SEM_CRIANCAS)

        return round(valor, 2)

    def detalhar_calculo(self) -> list:
        """Retorna o detalhamento do cálculo do aluguel."""
        detalhes = [("Valor base (1 quarto)", self.VALOR_BASE)]

        if self._quartos == 2:
            detalhes.append(("Acréscimo 2º quarto", self.ACRESCIMO_SEGUNDO_QUARTO))

        if self._garagem:
            detalhes.append(("Vaga de garagem", self.VALOR_GARAGEM))

        # Calcula subtotal antes do desconto
        subtotal = sum(v for _, v in detalhes)

        if not self._tem_criancas:
            desconto_valor = round(subtotal * self.DESCONTO_SEM_CRIANCAS, 2)
            detalhes.append(("Desconto 5% (sem crianças)", -desconto_valor))

        return detalhes


class Casa(Imovel):
    """
    Representa uma casa para locação.

    Regras de negócio:
        - Valor base: R$ 900,00 (1 quarto)
        - 2 quartos: + R$ 250,00
        - Garagem: + R$ 300,00
    """

    VALOR_BASE = 900.00
    ACRESCIMO_SEGUNDO_QUARTO = 250.00
    VALOR_GARAGEM = 300.00

    def __init__(self, quartos: int = 1, garagem: bool = False):
        super().__init__(tipo="Casa", quartos=quartos, garagem=garagem)

    def calcular_aluguel(self) -> float:
        """
        Calcula o aluguel mensal da casa.

        Fórmula:
            aluguel = 900 + (250 se 2 quartos) + (300 se garagem)
        """
        valor = self.VALOR_BASE

        if self._quartos == 2:
            valor += self.ACRESCIMO_SEGUNDO_QUARTO

        if self._garagem:
            valor += self.VALOR_GARAGEM

        return round(valor, 2)

    def detalhar_calculo(self) -> list:
        """Retorna o detalhamento do cálculo do aluguel."""
        detalhes = [("Valor base (1 quarto)", self.VALOR_BASE)]

        if self._quartos == 2:
            detalhes.append(("Acréscimo 2º quarto", self.ACRESCIMO_SEGUNDO_QUARTO))

        if self._garagem:
            detalhes.append(("Vaga de garagem", self.VALOR_GARAGEM))

        return detalhes


class Estudio(Imovel):
    """
    Representa um estúdio para locação.

    Regras de negócio:
        - Valor base: R$ 1.200,00 (valor fixo, sem quartos extras)
        - Estacionamento: R$ 250,00 (pacote de 2 vagas)
        - Vagas extras: R$ 60,00 cada (além das 2 do pacote)
    """

    VALOR_BASE = 1200.00
    VALOR_ESTACIONAMENTO_PACOTE = 250.00  # 2 vagas inclusas
    VAGAS_PACOTE = 2
    VALOR_VAGA_EXTRA = 60.00

    def __init__(self, estacionamento: bool = False, vagas_extras: int = 0):
        # Estúdio não tem opção de quartos extras
        super().__init__(tipo="Estúdio", quartos=1, garagem=estacionamento)
        self._estacionamento = estacionamento
        self._vagas_extras = max(0, vagas_extras)

    @property
    def estacionamento(self) -> bool:
        """Indica se possui pacote de estacionamento."""
        return self._estacionamento

    @property
    def vagas_extras(self) -> int:
        """Número de vagas extras além do pacote."""
        return self._vagas_extras

    @property
    def total_vagas(self) -> int:
        """Total de vagas de estacionamento."""
        if not self._estacionamento:
            return 0
        return self.VAGAS_PACOTE + self._vagas_extras

    def calcular_aluguel(self) -> float:
        """
        Calcula o aluguel mensal do estúdio.

        Fórmula:
            aluguel = 1200 + (250 se estacionamento) + (vagas_extras * 60)
        """
        valor = self.VALOR_BASE

        if self._estacionamento:
            valor += self.VALOR_ESTACIONAMENTO_PACOTE
            valor += self._vagas_extras * self.VALOR_VAGA_EXTRA

        return round(valor, 2)

    def detalhar_calculo(self) -> list:
        """Retorna o detalhamento do cálculo do aluguel."""
        detalhes = [("Valor base", self.VALOR_BASE)]

        if self._estacionamento:
            detalhes.append((
                f"Estacionamento ({self.VAGAS_PACOTE} vagas)",
                self.VALOR_ESTACIONAMENTO_PACOTE
            ))
            if self._vagas_extras > 0:
                detalhes.append((
                    f"Vagas extras ({self._vagas_extras}x R$ {self.VALOR_VAGA_EXTRA:.2f})",
                    self._vagas_extras * self.VALOR_VAGA_EXTRA
                ))

        return detalhes
