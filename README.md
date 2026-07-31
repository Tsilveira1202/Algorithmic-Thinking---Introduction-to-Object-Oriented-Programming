# 🏠 R.M Imobiliária — Orçamento de Aluguel

> **Tecnologias:** Python 3, Flask, HTML5, CSS3, Orientação a Objetos (POO)

Aplicação web desenvolvida para a **R.M Imobiliária** para automação e simulação de orçamentos de aluguel mensal de apartamentos, casas e estúdios.

---

## 🚀 Funcionalidades

- **Seleção de Imóveis:**
  - **Apartamento:** R$ 700,00 base (1 quarto), +R$ 200,00 (2º quarto), +R$ 300,00 (garagem), **5% de desconto** para famílias sem crianças.
  - **Casa:** R$ 900,00 base (1 quarto), +R$ 250,00 (2º quarto), +R$ 300,00 (garagem).
  - **Estúdio:** R$ 1.200,00 base, +R$ 250,00 (estacionamento com 2 vagas), +R$ 60,00 por vaga extra.
- **Contrato Imobiliário:**
  - Valor fixo de R$ 2.000,00 com opção de parcelamento de 1x a 5x.
- **Exportação CSV:**
  - Geração de relatório `.csv` contendo o detalhamento do cálculo e a projeção das **12 parcelas mensais**.
- **Interface Responsiva:**
  - Design moderno em tema escuro com interatividade dinâmica.

---

## 🛠️ Arquitetura Orientada a Objetos (POO)

- **Abstração:** Classe abstrata `Imovel` (`models/imovel.py`) definindo a interface padrão.
- **Herança:** Classes `Apartamento`, `Casa` e `Estudio` herdando de `Imovel`.
- **Polimorfismo:** Implementação própria do método `calcular_aluguel()` para cada tipo de imóvel.
- **Encapsulamento:** Atributos protegidos e acesso via `@property`.

---

## 📁 Estrutura do Código

```
Trabalho/
├── app.py                    # Servidor Flask e rotas
├── models/
│   ├── __init__.py           # Pacote de modelos
│   ├── imovel.py             # Classes Imovel, Apartamento, Casa e Estudio
│   ├── contrato.py           # Classe Contrato
│   └── orcamento.py          # Classes Orcamento e ExportadorCSV
├── templates/
│   └── index.html            # Interface web (Jinja2)
└── static/
    └── style.css             # Estilização CSS
```

---

## 💻 Como Executar

1. Instalar as dependências:
   ```bash
   pip install flask
   ```
2. Executar a aplicação:
   ```bash
   python app.py
   ```
3. Acesse no navegador: `http://127.0.0.1:5000`
