# Test-RAT: Sistema de Análise de Dados de Testes RAT

## 📋 Descrição do Projeto

O **Test-RAT** é um sistema automatizado de análise de dados desenvolvido para processar e analisar resultados de testes RAT (Remote Associates Test). O projeto combina análise de dados comportamentais com processamento estatístico para gerar insights sobre o desempenho dos participantes em diferentes tipos de testes cognitivos.

## 🎯 Objetivos

- **Análise Automatizada**: Processar automaticamente múltiplos arquivos CSV de dados de teste
- **Análise Estatística**: Calcular correlações, tempos de resposta e percentuais de acerto
- **Consolidação de Dados**: Integrar dados de diferentes fontes em uma única tabela final
- **Geração de Relatórios**: Criar arquivos CSV formatados para análise posterior

## 🏗️ Arquitetura do Sistema

O projeto está organizado em módulos especializados que executam diferentes etapas do processamento:

### 📁 Estrutura de Diretórios

```
Test-Rat/
├── Data/                           # Dados de entrada (excluído do git)
├── analise_dados_teste.py         # Módulo principal de análise de dados
├── analise_form.py                # Análise de formulários e questionários
├── analise_percentual_form.py     # Análise percentual detalhada
├── script_final.py                # Script de consolidação final
├── output_teste/                  # Resultados intermediários
├── resultado_final/               # Resultados finais consolidados
├── form_analises/                 # Análises de formulários
└── analise_percentual_form/       # Análises percentuais detalhadas
```

## 🔧 Módulos Principais

### 1. `analise_dados_teste.py` - Módulo Principal
**Função**: Processa dados de teste RAT e calcula métricas de desempenho

**Funcionalidades**:
- **Etapa 1**: Calcula correlação (`corr`) e tempo de resposta (`rt`) para cada participante
- **Etapa 2**: Analisa padrões de resposta, incluindo:
  - Contagem de tentativas por palavra
  - Percentual de acertos e erros
  - Palavras erradas mais comuns
  - Percentual de respostas sem resposta (`<NO_RESPONSE>`)

**Entrada**: Arquivos CSV na pasta `Data/` com colunas:
- `corr`: Indicador de acerto (0 ou 1)
- `rt`: Tempo de resposta
- `corranswer`: Palavra correta esperada
- `answer`: Resposta fornecida pelo participante

**Saída**: 
- `dados_etapa_01.csv`: Métricas por participante
- `resultado_final.csv`: Análise agregada por palavra

### 2. `analise_form.py` - Análise de Formulários
**Função**: Processa respostas de questionários e calcula percentuais

**Funcionalidades**:
- Análise de respostas "Sim/Não" em colunas específicas
- Cálculo de percentuais por linha de resposta
- Geração de tabelas filtradas e formatadas

**Entrada**: `Excel RAT ref - Respostas do Formulário 1.csv`

**Saída**: Múltiplos arquivos CSV com análises percentuais

### 3. `analise_percentual_form.py` - Análise Percentual Detalhada
**Função**: Gera análises percentuais para variáveis demográficas e comportamentais

**Funcionalidades**:
- Análise de faixas etárias
- Análise de gênero
- Análise de estado civil
- Análise de escolaridade
- Análise de renda familiar e pessoal

**Saída**: Arquivos CSV individuais para cada variável analisada

### 4. `script_final.py` - Consolidação Final
**Função**: Integra todos os resultados em uma única tabela

**Processo**:
1. Carrega resultados de todos os módulos
2. Realiza merge por ID do participante
3. Gera tabela final consolidada

**Saída**: `tabela_final.csv` com todos os dados integrados

## 🚀 Como Usar

### Pré-requisitos
```bash
pip install pandas
```

### Execução
1. **Análise de Dados de Teste**:
   ```bash
   python analise_dados_teste.py
   ```

2. **Análise de Formulários**:
   ```bash
   python analise_form.py
   ```

3. **Análise Percentual**:
   ```bash
   python analise_percentual_form.py
   ```

4. **Consolidação Final**:
   ```bash
   python script_final.py
   ```

### Fluxo de Processamento Recomendado
```bash
# Execute na ordem para garantir dependências
python analise_dados_teste.py
python analise_form.py
python analise_percentual_form.py
python script_final.py
```

## 📊 Formato dos Dados de Entrada

### Estrutura da Pasta Data/
```
Data/
├── 1/
│   ├── RAT-byresp-1.csv
│   └── RAT-FINAL-1.csv
├── 2/
│   ├── RAT-byresp-2.csv
│   └── RAT-FINAL-2.csv
└── ...
```

### Colunas Esperadas nos CSVs
- **Dados de Teste**: `corr`, `rt`, `corranswer`, `answer`
- **Formulários**: Colunas numeradas com respostas de questionário
- **Dados Demográficos**: `Idade`, `Gênero`, `Estado Civil`, etc.

## 📈 Resultados e Saídas

### Arquivos Intermediários
- `output_teste/dados_etapa_01.csv`: Métricas por participante
- `output_teste/resultado_final.csv`: Análise por palavra
- `form_analises/`: Múltiplos arquivos de análise de formulário
- `analise_percentual_form/`: Análises percentuais por variável

### Arquivo Final
- `resultado_final/tabela_final.csv`: Tabela consolidada com todos os dados

## 🔒 Segurança e Privacidade

- **Dados Sensíveis**: A pasta `Data/` e arquivos CSV de entrada são excluídos do controle de versão
- **Gitignore**: Configurado para não rastrear dados pessoais ou sensíveis
- **Outputs**: Resultados agregados não contêm informações identificáveis individuais

## 🛠️ Manutenção e Extensibilidade

### Adicionando Novas Variáveis
1. Edite `analise_percentual_form.py`
2. Adicione nova função de análise
3. Atualize a função principal

### Modificando Análises
1. Identifique o módulo relevante
2. Modifique a lógica de processamento
3. Atualize as funções de saída conforme necessário

## 📝 Logs e Debugging

O sistema inclui logging detalhado para facilitar debugging:
- Logs de carregamento de dados
- Logs de processamento por etapa
- Logs de erros e exceções
- Logs de salvamento de arquivos

## 🤝 Contribuição

Para contribuir com o projeto:
1. Mantenha a estrutura modular
2. Documente novas funcionalidades
3. Teste com dados de exemplo
4. Atualize este README conforme necessário

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique os logs de execução
2. Confirme o formato dos dados de entrada
3. Verifique se todas as dependências estão instaladas

---

**Desenvolvido para análise de dados de testes RAT com foco em pesquisa cognitiva e comportamental.**

