# Sistema de Análise de Eventos Ambientais

Este projeto consiste em uma aplicação Python desenvolvida para o registro e análise estatística de eventos ambientais (como queimadas, desmatamentos e inundações). O programa foca no processamento de dados usando estruturas de **listas e sublistas** sem o auxílio de bibliotecas externas como Pandas.

## Funcionalidades

O sistema é dividido em três etapas principais (ETL simplificado):

1.  **Entrada (INPUT):**
    * Coleta de dados geográficos e métricas de impacto.
    * **Validação de Texto:** Garante que campos como País e Cidade contenham apenas letras.
    * **Validação Numérica:** Área deve ser `> 0` e Intensidade deve estar entre `1 e 10`.
    * **Confirmação de Dados:** Permite ao usuário revisar e confirmar os dados de cada evento antes de salvá-los.

2.  **Processamento (TRANSFORM):**
    * Cálculo da área total e média de intensidade.
    * Identificação da região com maior frequência de ocorrências.
    * Cálculo da densidade média (Ocorrências/Área).
    * Identificação do **Evento Mais Crítico** baseado no nível de intensidade.

3.  **Saída (LOAD):**
    * Exibição de um relatório formatado com separadores visuais e resumo estatístico completo.

##  Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Estruturas de Controle:** Loops `while` para validação e `for` para processamento de dados.
* **Estrutura de Dados:** Lista principal contendo sublistas (cada sublista representa um evento completo).

## Como Executar o Programa

1.  Certifique-se de ter o Python instalado.
2.  Salve o código em um arquivo, por exemplo: `analise_eventos.py`.
3.  Execute via terminal:
    ```bash
    python analise_eventos.py
    ```

## Exemplo de Saída

```text
========================================
        RELATÓRIO DE ANÁLISE
========================================
Total de eventos registrados: 2

----------------------------------------
Resumo Geral
----------------------------------------
Área total afetada: 22.00 km²
Média de intensidade: 3.5
----------------------------------------

----------------------------------------
Análises
----------------------------------------
Região com maior número de ocorrências: Norte
Quantidade de eventos acima da média: 1
Densidade média de ocorrências: 1.77 ocorr/km²

----------------------------------------
Evento Mais Crítico
----------------------------------------
Tipo: Queimada
Local: Belém, Norte, Brasil
Intensidade: 6/10
Área: 19.00 km²
========================================
Total de desastres registrados: 2
