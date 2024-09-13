# LogicaNebulosa: Sistema de Análise de Risco do Banco

## Descrição

O Sistema de Análise de Risco do Banco é uma aplicação que utiliza Lógica Nebulosa para avaliar o risco de crédito dos clientes com base em três variáveis: histórico de crédito, renda mensal e a dívida atual. O sistema foi feito usando a biblioteca Scikit-fuzzy.

## Objetivo

O objetivo deste sistema é fazer uma avaliação de risco do crédito para clientes de um banco, ajudando na decisões de concessão de crédito para a gerência. A avaliação foi feita em regras fuzzy que consideram a incerteza e a imprecisão inerentes à análise financeira.

## Instalação

1. Clone o repositório:

   git clone https://github.com/alvesluis311/LogicaNebulosa

2. Abra o diretório do projeto
  
3. Abra o projeto com VSCode

   Abra o terminal no diretório e digite "code ."
   
4. Instale as dependências:

   numpy
   scikit-fuzzy
   matplotlib

## Uso

1. Execute o script `EntradaBanco.py` para inserir dados e calcular o risco:

   botão direito e "run python file in terminal"

2. Insira as informações quando solicitado:

   - Histórico de crédito: um valor entre 0 e 10
   - Renda mensal: um valor entre 0 e 100000, que representa a renda mensal do cliente.
   - Dívida atual: um valor entre 0 e 100000, que representa a dívida atual do cliente.

3. O sistema calculará o risco e exibirá o resultado.

## Variáveis de Entrada

- Histórico de Crédito: Classificado como "Ruim", "Regular", "Bom" e "Excelente".
- Renda Mensal: Classificada como "Baixa", "Média" e "Alta".
- Dívida Atual: Classificada como "Baixa", "Moderada" e "Alta".

## Regras Fuzzy

O sistema utiliza as seguintes regras para determinar o risco:

- Se o histórico de crédito é "Ruim" e a dívida atual é "Alta" ou a renda é "Baixa", então o risco é "Alto".
- Se o histórico de crédito é "Bom" e a dívida é "Baixa" e a renda é "Alta", então o risco é "Baixo".
- E assim por diante para combinações de histórico de crédito "Regular", "Bom" e "Excelente".

## Saída

O sistema retorna dois valores:
- Porcentagem do Risco: Um valor entre 0 e 100 que representa a intensidade do risco.
- Tipo de Risco: Classificado como "Baixo", "Médio" ou "Alto".

## Exemplos de Uso
Exemplo 1:

Entrada:
- Histórico de crédito: 10
- Renda mensal: 60000
- Dívida atual: 20000

Saída:
- Porcentagem do Risco: 11%
- Tipo de Risco: Baixo

Exemplo 2:

Entrada:
- Histórico de crédito: 5
- Renda mensal: 50000
- Dívida atual: 50000

Saída:
- Porcentagem do Risco: 50%
- Tipo de Risco: Médio
