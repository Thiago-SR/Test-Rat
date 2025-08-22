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
├── visualizacao_unificada.py      # Sistema de visualização unificado
├── analise_form.py                # Análise de formulários e questionários
├── analise_percentual_form.py     # Análise percentual detalhada
├── script_final.py                # Script de consolidação final
├── output_teste/                  # Resultados intermediários
├── resultado_final/               # Resultados finais consolidados
├── form_analises/                 # Análises de formulários
├── analise_percentual_form/       # Análises percentuais detalhadas
└── visualizacoes/                 # Gráficos e visualizações gerados
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

### 2. `visualizacao_unificada.py` - Sistema de Visualização
**Função**: Cria visualizações gráficas profissionais dos dados analisados

**Funcionalidades**:
- **Detecção Automática**: Detecta bibliotecas disponíveis (matplotlib, seaborn, plotly)
- **Múltiplos Modos**: `auto`, `minimo`, `basico`, `completo`
- **Visualizações Estáticas**: Histogramas, boxplots, scatter plots, gráficos de barras
- **Visualizações Interativas**: Gráficos HTML interativos (se plotly disponível)
- **Análise Demográfica**: Gráficos de idade, gênero, escolaridade
- **Análise de Desempenho**: Correlações, distribuições, rankings

**Tipos de Gráficos Gerados**:
- 📊 **Desempenho Geral**: 4 gráficos em 1 (acertos, tempo, correlação)
- 📝 **Análise de Palavras**: Top 10 acertos, acertos vs erros, sem resposta
- 👥 **Análise Demográfica**: Distribuição por idade, gênero, escolaridade
- 🎯 **Gráficos Interativos**: Scatter plots e dashboards HTML

**Saída**: Pasta `visualizacoes/` com arquivos PNG, HTML e CSV

### 3. `analise_form.py` - Análise de Formulários
**Função**: Processa respostas de questionários e calcula percentuais

**Funcionalidades**:
- Análise de respostas "Sim/Não" em colunas específicas
- Cálculo de percentuais por linha de resposta
- Geração de tabelas filtradas e formatadas

**Entrada**: `Excel RAT ref - Respostas do Formulário 1.csv`

**Saída**: Múltiplos arquivos CSV com análises percentuais

### 4. `analise_percentual_form.py` - Análise Percentual Detalhada
**Função**: Gera análises percentuais para variáveis demográficas e comportamentais

**Funcionalidades**:
- Análise de faixas etárias
- Análise de gênero
- Análise de estado civil
- Análise de escolaridade
- Análise de renda familiar e pessoal

**Saída**: Arquivos CSV individuais para cada variável analisada

### 5. `script_final.py` - Consolidação Final
**Função**: Integra todos os resultados em uma única tabela

**Processo**:
1. Carrega resultados de todos os módulos
2. Realiza merge por ID do participante
3. Gera tabela final consolidada

**Saída**: `tabela_final.csv` com todos os dados integrados

## 🚀 Como Usar

### Pré-requisitos
```bash
# Dependências básicas (obrigatórias)
pip install pandas

# Dependências para visualizações (recomendadas)
pip install matplotlib seaborn

# Dependências para gráficos interativos (opcionais)
pip install plotly

# Ou instale tudo de uma vez
pip install -r requirements_visualizacao.txt
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

5. **Geração de Visualizações**:
   ```bash
   # Modo automático (recomendado)
   python visualizacao_unificada.py
   
   # Modo básico (apenas gráficos estáticos)
   python visualizacao_unificada.py --modo basico
   
   # Modo completo (gráficos estáticos + interativos)
   python visualizacao_unificada.py --modo completo
   ```

### Fluxo de Processamento Recomendado
```bash
# Execute na ordem para garantir dependências
python analise_dados_teste.py
python analise_form.py
python analise_percentual_form.py
python script_final.py

# Gere visualizações após ter todos os dados
python visualizacao_unificada.py
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

### Visualizações Geradas
- `visualizacoes/desempenho_geral.png`: 4 gráficos de desempenho em 1
- `visualizacoes/correlacao_acertos_tempo.png`: Correlação acertos vs tempo
- `visualizacoes/top_palavras_acerto.png`: Top 10 palavras com maior acerto
- `visualizacoes/acertos_vs_erros.png`: Comparação acertos vs erros por palavra
- `visualizacoes/alta_taxa_sem_resposta.png`: Análise de respostas sem resposta
- `visualizacoes/distribuicao_idade.png`: Distribuição por faixa etária
- `visualizacoes/distribuicao_genero.png`: Distribuição por gênero
- `visualizacoes/distribuicao_escolaridade.png`: Distribuição por escolaridade
- `visualizacoes/resumo_estatistico_teste.csv`: Resumo estatístico dos dados de teste
- `visualizacoes/resumo_estatistico_palavras.csv`: Resumo estatístico das palavras

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

## 📊 Sistema de Visualização

### 🎯 Características Principais
- **Inteligente**: Detecta automaticamente bibliotecas disponíveis
- **Adaptativo**: Se ajusta aos recursos do sistema
- **Unificado**: Um único script para todas as necessidades
- **Profissional**: Gráficos de alta qualidade para apresentações

### 🔧 Modos de Execução
- **`auto`**: Detecta automaticamente o melhor modo disponível
- **`minimo`**: Apenas resumos estatísticos em CSV
- **`basico`**: Gráficos estáticos com matplotlib
- **`completo`**: Todas as funcionalidades (estáticas + interativas)

### 📈 Tipos de Visualizações
1. **Análise de Desempenho**: Distribuições, correlações, boxplots
2. **Análise de Palavras**: Rankings, comparações, taxas de acerto
3. **Análise Demográfica**: Idade, gênero, escolaridade
4. **Gráficos Interativos**: Dashboards HTML com plotly

### 💡 Dicas de Uso
- Execute primeiro os scripts de análise para ter os dados
- Use `--modo basico` para gráficos estáticos rápidos
- Use `--modo completo` para apresentações profissionais
- Os gráficos são salvos automaticamente na pasta `visualizacoes/`

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
4. Para problemas de visualização, verifique se matplotlib está instalado

---

**Desenvolvido para análise de dados de testes RAT com foco em pesquisa cognitiva e comportamental.**

