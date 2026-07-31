# 🏠 R.M Imobiliária — Orçamento de Aluguel

> **Disciplina:** Algorithmic Thinking & Introduction to Object-Oriented Programming  
> **Tecnologias:** Python 3, Flask, HTML5, CSS3 (Dark Theme), Orientação a Objetos  

Aplicação web desenvolvida para a empresa fictícia **R.M Imobiliária** para automação e simulação de orçamentos de aluguel mensal de apartamentos, casas e estúdios.

---

## 🚀 Funcionalidades

- **Seleção Dinâmica de Imóveis:**
  - **Apartamento:** R$ 700,00 base (1 quarto), +R$ 200,00 (2º quarto), +R$ 300,00 (garagem), **-5% de desconto** para familias sem crianças.
  - **Casa:** R$ 900,00 base (1 quarto), +R$ 250,00 (2º quarto), +R$ 300,00 (garagem).
  - **Estúdio:** R$ 1.200,00 base, +R$ 250,00 (estacionamento com 2 vagas), +R$ 60,00 por vaga extra.
- **Contrato Imobiliário:**
  - Valor fixo de R$ 2.000,00 com opção de parcelamento de 1x a 5x.
- **Exportação CSV:**
  - Geração de relatório `.csv` contendo o detalhamento do cálculo e a projeção das **12 parcelas mensais**.
- **Interface Responsiva:**
  - UI moderna e limpa com tema escuro e campos condicionais.

---

## 🛠️ Arquitetura Orientada a Objetos (POO)

O projeto aplica os princípios fundamentais da Programação Orientada a Objetos:

- **Abstração:** Classe abstrata `Imovel` (`models/imovel.py`) definindo a interface padrão.
- **Herança:** Classes `Apartamento`, `Casa` e `Estudio` herdando de `Imovel`.
- **Polimorfismo:** Implementação própria do método `calcular_aluguel()` para cada tipo de imóvel.
- **Encapsulamento:** Atributos protegidos e acesso controlado via `@property`.

---

## 📁 Estrutura do Projeto

```
Trabalho/
├── app.py                    # Servidor Flask e rotas
├── models/
│   ├── __init__.py           # Exportação dos modelos
│   ├── imovel.py             # Classes Imovel, Apartamento, Casa e Estudio
│   ├── contrato.py           # Classe Contrato
│   └── orcamento.py          # Classes Orcamento e ExportadorCSV
├── templates/
│   └── index.html            # Template HTML Jinja2
├── static/
│   ├── style.css             # Estilos CSS
│   ├── fluxograma_aplicacao.png
│   └── diagrama_classes_uml.png
├── fluxograma_e_logica.md    # Documentação teórica (Fluxograma e UML)
├── roteiro_video.md          # Roteiro para gravação do vídeo pitch
├── REQUISITOS.md             # Documentação dos requisitos
└── README.md                 # Documentação do repositório
```

---

## 💻 Como Executar a Aplicação

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Instale o **Flask**:
   ```bash
   pip install flask
   ```
3. Execute o servidor:
   ```bash
   python app.py
   ```
4. Acesse no navegador: `http://127.0.0.1:5000`

---

## 🎓 Entregáveis do Trabalho

1. **Parte Teórica (25%):** [fluxograma_e_logica.md](fluxograma_e_logica.md)
2. **Parte Prática (50%):** Código fonte Python / Flask com POO neste repositório.
3. **Vídeo Pitch (25%):** [roteiro_video.md](roteiro_video.md)
