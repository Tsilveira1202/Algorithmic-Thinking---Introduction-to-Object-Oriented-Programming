# 📋 Documentação de Requisitos — Orçamento de Aluguel

> Disciplina: **Algorithmic Thinking & Introduction to Object-Oriented Programming**
> Empresa fictícia: **R.M Imobiliária**
> Fonte: [TRABALHO - Algorithmic Thinking & Introduction to Object-Oriented Programming.pdf](file:///c:/Users/Tiago/Documents/Projetos/Trabalho/TRABALHO%20-%20Algorithmic%20Thinking%20%26%20Introduction%20to%20Object-Oriented%20Programming.pdf)

---

## 1. Visão Geral do Desafio

Desenvolver uma **aplicação para geração de orçamento de aluguel mensal** para a empresa R.M Imobiliária, especializada na locação de **casas, apartamentos e estúdios**. O objetivo é automatizar e facilitar a geração de orçamentos de imóveis para os clientes.

---

## 2. Regras de Negócio

### 2.1 Tipos de Imóveis e Valores Base

| Tipo de Imóvel | Valor Base (mensal)  | Observação                |
|----------------|----------------------|---------------------------|
| Apartamento    | R$ 700,00            | Por 1 quarto              |
| Casa           | R$ 900,00            | Por 1 quarto              |
| Estúdio        | R$ 1.200,00          | Valor fixo (sem quartos extras) |

### 2.2 Quartos Adicionais (2 quartos)

| Tipo de Imóvel | Acréscimo por 2º quarto |
|----------------|-------------------------|
| Apartamento    | + R$ 200,00             |
| Casa           | + R$ 250,00             |
| Estúdio        | ❌ Não se aplica         |

### 2.3 Vaga de Garagem / Estacionamento

| Tipo de Imóvel      | Regra de estacionamento                                                   |
|---------------------|---------------------------------------------------------------------------|
| Apartamento / Casa  | + R$ 300,00 por vaga de garagem                                           |
| Estúdio             | + R$ 250,00 pelo pacote inicial (2 vagas), + R$ 60,00 por vaga adicional  |

### 2.4 Desconto

| Condição                                                | Desconto |
|---------------------------------------------------------|----------|
| Apartamento **sem crianças** no grupo familiar          | **5%** sobre o valor do aluguel |

### 2.5 Contrato Imobiliário

| Item                   | Valor       | Condições              |
|------------------------|-------------|------------------------|
| Contrato imobiliário   | R$ 2.000,00 | Parcelável em até **5 vezes** |

---

## 3. Funcionalidades Requeridas

### 3.1 Geração de Orçamento (funcionalidade principal)

O sistema deve:

1. **Selecionar tipo de imóvel** — Apartamento, Casa ou Estúdio
2. **Definir quantidade de quartos** — 1 ou 2 quartos (para Apartamento e Casa)
3. **Opção de garagem/estacionamento** — com regras diferenciadas por tipo
4. **Verificação de crianças** — para aplicar desconto de 5% em apartamentos
5. **Cálculo do aluguel mensal** — somatório de valor base + adicionais − descontos
6. **Apresentação do orçamento final** contendo:
   - Valor do aluguel mensal orçado
   - Valor do contrato imobiliário (R$ 2.000,00)
   - Opção de parcelamento do contrato (até 5x)

### 3.2 Exportação CSV

- Gerar arquivo `.csv` com as **12 parcelas** do orçamento (12 meses de aluguel)

---

## 4. Entregáveis e Distribuição de Nota

A entrega final é composta por **três entregáveis obrigatórios**:

### 4.1 Parte Teórica — Fluxograma e Estrutura Lógica (25% da nota)

| Critério                     | Detalhes                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **Formato**                  | PDF                                                                      |
| **Conteúdo obrigatório**     | Fluxograma da aplicação                                                  |
| **Complementos sugeridos**   | Pseudocódigo, esquemas, comentários explicativos sobre a estrutura do código |
| **Foco**                     | Demonstrar como o **pensamento algorítmico** foi aplicado                |

### 4.2 Parte Prática — Código e Estrutura do Projeto (50% da nota)

| Critério                     | Detalhes                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **Formato**                  | Pasta compactada (.zip)                                                  |
| **Conteúdo obrigatório**     | Arquivos `.py` com o código-fonte                                        |
| **Conteúdo opcional**        | Arquivos HTML/CSS (caso tenha interface web)                             |
| **Repositório**              | Link do repositório **GitHub** com o projeto publicado                   |
| **Requisitos de qualidade**  | Código funcional, bem estruturado, usando **princípios de OOP**          |

> **⚠️ IMPORTANTE:** O código deve utilizar **princípios de orientação a objetos** — isso é explicitamente avaliado.

### 4.3 Vídeo Pitch (25% da nota)

| Critério                     | Detalhes                                                                 |
|------------------------------|--------------------------------------------------------------------------|
| **Duração máxima**           | 4 minutos                                                               |
| **Formato**                  | Gravação de tela                                                         |
| **Publicação**               | YouTube ou rede social (LinkedIn)                                        |
| **Conteúdo esperado**        | Objetivo da aplicação, trechos de código, demonstração de navegação      |
| **Entrega**                  | Enviar o link do vídeo                                                   |

---

## 5. Requisitos Técnicos Implícitos

Com base na análise do documento, os seguintes requisitos técnicos são inferidos:

| #  | Requisito                                                        | Justificativa                                      |
|----|------------------------------------------------------------------|-----------------------------------------------------|
| T1 | Linguagem: **Python**                                            | Referências a `.py` e fontes de pesquisa em Python   |
| T2 | Paradigma: **Orientação a Objetos (OOP)**                        | Explicitamente exigido na avaliação                  |
| T3 | Interface (opcional): **HTML/CSS**                               | Mencionado como possível, mas não obrigatório        |
| T4 | Exportação de dados: **CSV**                                     | 12 parcelas do orçamento em arquivo `.csv`           |
| T5 | Versionamento: **GitHub**                                        | Link do repositório é obrigatório na entrega         |
| T6 | Documentação: **Fluxograma em PDF**                              | Parte teórica obrigatória                            |

---

## 6. Fórmulas de Cálculo

### Aluguel Mensal — Apartamento

```python
aluguel = 700.00
if quartos == 2:
    aluguel += 200.00
if garagem:
    aluguel += 300.00
if sem_criancas:
    aluguel *= 0.95  # desconto de 5%
```

### Aluguel Mensal — Casa

```python
aluguel = 900.00
if quartos == 2:
    aluguel += 250.00
if garagem:
    aluguel += 300.00
# Sem desconto por crianças para casas
```

### Aluguel Mensal — Estúdio

```python
aluguel = 1200.00
if estacionamento:
    aluguel += 250.00  # pacote de 2 vagas
    if vagas_extras > 0:
        aluguel += vagas_extras * 60.00
# Sem desconto por crianças para estúdios
```

### Contrato

```python
contrato = 2000.00
parcela_contrato = contrato / num_parcelas  # num_parcelas: 1 a 5
```

---

## 7. Checklist de Entrega

- [ ] Código Python funcional com OOP
- [ ] Cálculo correto do aluguel (Apartamento, Casa, Estúdio)
- [ ] Lógica de quartos adicionais
- [ ] Lógica de garagem/estacionamento
- [ ] Desconto de 5% para apartamentos sem crianças
- [ ] Cálculo e parcelamento do contrato (até 5x)
- [ ] Exportação `.csv` com 12 parcelas do orçamento
- [ ] Interface HTML/CSS (opcional, mas agrega valor)
- [ ] Repositório GitHub publicado
- [ ] Fluxograma da aplicação em PDF
- [ ] Pseudocódigo / comentários sobre a lógica
- [ ] Vídeo Pitch (até 4 min) publicado no YouTube/LinkedIn
