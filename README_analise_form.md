# Análise do Formulário RAT

Este script analisa os dados do formulário RAT e gera diferentes relatórios baseados nas respostas dos participantes.

## Arquivos de Entrada

- `RAT_Respostas_Formulario_1.csv`: Arquivo CSV contendo as respostas do formulário

## Arquivos de Saída

Todos os arquivos de saída são salvos na pasta `form_analises/`:

1. **resultado_percentual.csv**: Percentual geral de respostas "Sim" vs "Não"
2. **resultados_por_linha.csv**: Análise individual de cada participante (PM 1 Sim ou All não)
3. **soma_por_linha.csv**: Soma dos valores das colunas 26-33 (primeiro dígito de cada valor)
4. **tabela_filtrada_formatada.csv**: Dados demográficos formatados e abreviados

## Como Executar

```bash
python analise_form_organizado.py
```

## Funcionalidades

### 1. Análise Percentual (PM 1 Sim)
- Analisa as colunas 15-26 (excluindo coluna 22)
- Calcula percentual de participantes que responderam pelo menos um "Sim"
- Exclui valores "Não" e vazios

### 2. Análise por Linha
- Analisa cada participante individualmente
- Classifica como "PM 1 Sim" (pelo menos um "Sim") ou "All não" (todos "Não")

### 3. Soma do Formulário
- Soma o primeiro dígito de cada valor nas colunas 26-33
- Útil para análise de pontuação

### 4. Dados Demográficos
- Processa e formata dados demográficos (idade, gênero, escolaridade, etc.)
- Aplica abreviações para facilitar análise
- Remove linhas de cabeçalho

## Estrutura do Código

- `carregar_dados()`: Carrega o arquivo CSV
- `percentual_PM_1_Sim()`: Calcula percentuais
- `PM_1_Sim()`: Analisa linha por linha
- `soma_form()`: Calcula somas
- `processar_dados_demograficos()`: Formata dados demográficos
- `main()`: Função principal que executa todas as análises

## Configurações

No início do arquivo, você pode modificar:
- `INPUT_FILE`: Nome do arquivo de entrada
- `OUTPUT_DIR`: Pasta onde salvar os resultados

## Requisitos

- Python 3.x
- pandas
- os (biblioteca padrão)

## Instalação das Dependências

```bash
pip install pandas
``` 