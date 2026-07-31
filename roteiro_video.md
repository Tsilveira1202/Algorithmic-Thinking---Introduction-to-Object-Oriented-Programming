# 🎬 Roteiro do Vídeo Pitch — R.M Imobiliária

> **Duração total:** ~4 minutos
> **Formato:** Gravação de tela com narração
> **Estrutura:** Cada seção tem duas colunas: **O QUE FALAR** e **O QUE MOSTRAR NA TELA**

---

## 🟢 CENA 1 — Introdução (0:00 – 0:30)

### O que mostrar na tela:
> Abra a interface web da aplicação no navegador (`http://127.0.0.1:5000`).
> A tela deve mostrar o formulário inicial com o logo "R.M Imobiliária" visível.

### O que falar:

> "Olá! Meu nome é **[SEU NOME]** e este é o meu projeto da disciplina de Algorithmic Thinking e Introdução à Programação Orientada a Objetos.
>
> O desafio foi desenvolver uma aplicação para a **R.M Imobiliária**, uma empresa especializada em locação de imóveis. O objetivo da aplicação é **automatizar a geração de orçamentos de aluguel** para três tipos de imóvel: apartamentos, casas e estúdios.
>
> A aplicação foi desenvolvida em **Python**, usando o framework **Flask** para a interface web, e aplica princípios de **orientação a objetos** como herança, polimorfismo e encapsulamento."

---

## 🟡 CENA 2 — Estrutura do Código e OOP (0:30 – 2:00)

### O que mostrar na tela:
> Alterne para o **VS Code** (ou editor de código) com os arquivos do projeto abertos.

---

#### Subcena 2.1 — Visão geral dos arquivos (0:30 – 0:50)

### O que mostrar na tela:
> Mostre a **árvore de arquivos** no explorador lateral do VS Code:
> ```
> Trabalho/
> ├── app.py
> ├── models/
> │   ├── imovel.py
> │   ├── contrato.py
> │   └── orcamento.py
> ├── templates/
> │   └── index.html
> └── static/
>     └── style.css
> ```

### O que falar:

> "Aqui temos a estrutura do projeto. Organizei o código em módulos separados dentro da pasta `models`. Temos o arquivo `imovel.py` com as classes dos imóveis, `contrato.py` para o contrato, e `orcamento.py` para gerar o orçamento e exportar o CSV. O `app.py` é o servidor Flask, e as pastas `templates` e `static` contêm a interface web."

---

#### Subcena 2.2 — Classe base e herança (0:50 – 1:20)

### O que mostrar na tela:
> Abra o arquivo `models/imovel.py`. Mostre a **classe `Imovel`** (linha 17 até ~70) e depois scroll para a **classe `Apartamento`** (linha ~80).
> Destaque visualmente a linha `class Imovel(ABC)` e o método `calcular_aluguel`.

### O que falar:

> "Esse é o coração do projeto — o arquivo `imovel.py`. Aqui eu criei uma **classe base abstrata** chamada `Imovel`, usando o módulo `ABC` do Python. Ela define os atributos comuns como tipo, quartos e garagem, e declara o método abstrato `calcular_aluguel`.
>
> Depois, cada tipo de imóvel **herda** dessa classe base. Por exemplo, a classe `Apartamento` implementa o `calcular_aluguel` com as regras específicas: valor base de 700 reais, mais 200 se tiver dois quartos, mais 300 pela garagem, e um desconto de 5% se não houver crianças.
>
> As classes `Casa` e `Estúdio` seguem o mesmo padrão, cada uma com suas próprias regras. Isso é o **polimorfismo** — cada classe tem sua versão do mesmo método."

---

#### Subcena 2.3 — Orçamento e CSV (1:20 – 1:45)

### O que mostrar na tela:
> Abra `models/orcamento.py`. Mostre a **classe `Orcamento`** (método `gerar_parcelas`) e a **classe `ExportadorCSV`** (método `exportar`).

### O que falar:

> "A classe `Orcamento` recebe um imóvel e um contrato, e gera o orçamento completo com as 12 parcelas mensais. E a classe `ExportadorCSV` é responsável por exportar tudo para um arquivo `.csv`, usando o módulo nativo do Python."

---

#### Subcena 2.4 — Servidor Flask (1:45 – 2:00)

### O que mostrar na tela:
> Abra `app.py`. Mostre brevemente a **rota `/gerar`** (linhas ~40-90), destacando onde o tipo do imóvel é verificado e a classe correta é instanciada.

### O que falar:

> "No `app.py`, o servidor Flask recebe os dados do formulário e, com base no tipo selecionado, instancia a classe correta — Apartamento, Casa ou Estúdio. Isso demonstra o polimorfismo na prática: o mesmo fluxo funciona para qualquer tipo de imóvel, porque todos implementam a mesma interface."

---

## 🔵 CENA 3 — Demonstração da Aplicação (2:00 – 3:30)

### O que mostrar na tela:
> Volte para o **navegador** com a aplicação aberta em `http://127.0.0.1:5000`.

---

#### Subcena 3.1 — Orçamento de Apartamento (2:00 – 2:40)

### O que mostrar na tela:
> 1. Preencha o nome: "Maria Silva"
> 2. Selecione "Apartamento" (card)
> 3. Selecione "2 Quartos"
> 4. Ative o toggle "Vaga de Garagem"
> 5. Deixe "Possui Crianças?" desativado (para mostrar o desconto)
> 6. Selecione "3x" no contrato
> 7. Clique em "Gerar Orçamento"
> 8. Mostre o resultado com o valor, detalhamento e tabela de parcelas

### O que falar:

> "Vamos fazer uma demonstração. Vou simular um orçamento para a cliente Maria Silva, que quer alugar um apartamento de 2 quartos com garagem. Ela não tem crianças, então vai receber o desconto de 5%.
>
> Seleciono o apartamento, marco 2 quartos, ativo a garagem, e deixo 'crianças' desativado. No contrato, vou parcelar em 3 vezes.
>
> Ao clicar em 'Gerar Orçamento', o sistema calcula automaticamente: 700 de base, mais 200 do segundo quarto, mais 300 da garagem, totalizando 1.200 reais. Com o desconto de 5%, o aluguel fica em **1.140 reais por mês**.
>
> Aqui embaixo temos o contrato de 2 mil reais em 3 parcelas de 666,67, e a tabela com as 12 parcelas mensais."

---

#### Subcena 3.2 — Exportação CSV (2:40 – 3:00)

### O que mostrar na tela:
> 1. Clique no botão "Exportar Orçamento (CSV)"
> 2. Mostre o arquivo sendo baixado
> 3. Abra o arquivo CSV no Excel/Bloco de Notas para mostrar o conteúdo

### O que falar:

> "Clicando em 'Exportar CSV', o sistema gera um arquivo com todas as 12 parcelas do orçamento, incluindo o detalhamento do cálculo e as informações do contrato. Aqui está o arquivo aberto — temos os dados do cliente, o tipo de imóvel, o detalhamento dos valores e as 12 linhas com as parcelas mensais."

---

#### Subcena 3.3 — Teste com Estúdio (3:00 – 3:30)

### O que mostrar na tela:
> 1. Clique em "Novo Orçamento"
> 2. Preencha "João Santos"
> 3. Selecione "Estúdio"
> 4. Observe que os campos mudam (desaparecem quartos e garagem, aparece estacionamento)
> 5. Ative estacionamento e adicione 1 vaga extra
> 6. Gere o orçamento
> 7. Mostre o resultado

### O que falar:

> "Vou fazer mais um teste rápido. Agora com um estúdio para o cliente João Santos. Repare que ao selecionar 'Estúdio', o formulário se adapta automaticamente — os campos de quartos e garagem desaparecem e aparece a opção de estacionamento.
>
> Vou ativar o pacote de estacionamento com 2 vagas por 250 reais e adicionar mais 1 vaga extra de 60 reais. O resultado: 1.200 de base, mais 250 do estacionamento, mais 60 da vaga extra — totalizando **1.510 reais por mês**."

---

## 🔴 CENA 4 — Encerramento (3:30 – 4:00)

### O que mostrar na tela:
> Volte para o VS Code, mostrando a estrutura de pastas do projeto (visão geral).
> Ou mantenha a tela com o resultado do orçamento.

### O que falar:

> "Com esse projeto, eu pude colocar em prática os conceitos de **pensamento algorítmico** — decompondo o problema em partes menores — e de **orientação a objetos** — usando herança, polimorfismo e encapsulamento para organizar o código de forma limpa e reutilizável.
>
> A aplicação atende a todos os requisitos: calcula o aluguel com as regras de cada tipo de imóvel, aplica descontos, gera o parcelamento do contrato e exporta o orçamento em CSV.
>
> O código está disponível no meu GitHub. Muito obrigado pela atenção!"

---

## 📝 Checklist antes de gravar

- [ ] Aplicação rodando (`python app.py`)
- [ ] Navegador aberto em `http://127.0.0.1:5000`
- [ ] VS Code com os arquivos abertos
- [ ] Microfone testado
- [ ] Gravador de tela configurado (OBS Studio, Loom, etc.)
- [ ] Ensaiar as falas pelo menos 1 vez
- [ ] Verificar que a gravação não ultrapassa 4 minutos
