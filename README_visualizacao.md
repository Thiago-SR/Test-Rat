# 📊 Visualizações de Dados RAT - Versão Unificada

Este diretório contém um **script único e inteligente** para criar visualizações gráficas dos dados de teste RAT. O sistema detecta automaticamente as dependências disponíveis e se adapta para oferecer a melhor experiência possível.

## 🎯 **Script Unificado: `visualizacao_unificada.py`**

**Características principais:**
- ✅ **Detecção automática** de bibliotecas disponíveis
- 🎨 **Adaptação inteligente** baseada nas dependências
- 🚀 **Múltiplos modos** de execução
- 📊 **Fallback automático** para funcionalidades disponíveis
- 💡 **Sugestões automáticas** de instalação

## 🔧 **Modos de Execução**

### 🎯 **Modo "auto" (Padrão)**
```bash
python visualizacao_unificada.py
```
- Detecta automaticamente o que está disponível
- Escolhe o melhor modo baseado nas bibliotecas instaladas

### 📊 **Modo "minimo"**
```bash
python visualizacao_unificada.py --modo minimo
```
- Apenas resumos estatísticos em CSV
- Funciona sem dependências externas

### 🎨 **Modo "basico"**
```bash
python visualizacao_unificada.py --modo basico
```
- Gráficos estáticos com matplotlib
- Visualizações essenciais

### 🚀 **Modo "completo"**
```bash
python visualizacao_unificada.py --modo completo
```
- Todas as funcionalidades disponíveis
- Gráficos estáticos + interativos

## 📦 **Instalação de Dependências**

### 🟢 **Instalação Mínima (Funcionalidade Básica)**
```bash
pip install pandas numpy
```

### 🟡 **Instalação Recomendada (Gráficos Estáticos)**
```bash
pip install pandas numpy matplotlib
```

### 🟠 **Instalação Avançada (Estilos Melhorados)**
```bash
pip install pandas numpy matplotlib seaborn
```

### 🔴 **Instalação Completa (Todas as Funcionalidades)**
```bash
pip install -r requirements_visualizacao.txt
```

## 📈 **Tipos de Visualizações**

### 📊 **Desempenho Geral** (requer matplotlib)
1. **Distribuição de Acertos**: Histograma por participante
2. **Boxplot de Acertos**: Distribuição estatística
3. **Distribuição de Tempo**: Histograma de tempos de resposta
4. **Acertos vs Tempo**: Scatter plot com linha de tendência

### 📝 **Análise de Palavras** (requer matplotlib)
1. **Top 10 Palavras**: Ranking de maior taxa de acerto
2. **Acertos vs Erros**: Comparação lado a lado
3. **Respostas Sem Resposta**: Análise de não respostas

### 👥 **Análise Demográfica** (requer matplotlib + dados)
1. **Distribuição por Idade**: Gráfico de barras por faixa
2. **Distribuição por Gênero**: Gráfico de pizza
3. **Distribuição por Escolaridade**: Gráfico de barras

### 🎯 **Visualizações Interativas** (requer plotly)
1. **Scatter Plot Interativo**: Acertos vs tempo com hover
2. **Dashboard de Palavras**: 4 gráficos em uma visualização

## 🚀 **Como Executar**

### **1. Execução Simples (Recomendado)**
```bash
python visualizacao_unificada.py
```

### **2. Execução com Modo Específico**
```bash
# Para apenas gráficos básicos
python visualizacao_unificada.py --modo basico

# Para funcionalidade completa
python visualizacao_unificada.py --modo completo
```

### **3. Execução em Ambientes Diferentes**

#### **Jupyter Notebook**
```python
from visualizacao_unificada import VisualizadorRATUnificado

visualizador = VisualizadorRATUnificado(modo="auto")
visualizador.gerar_relatorio_completo()
```

#### **Script Python**
```python
import visualizacao_unificada
visualizacao_unificada.main()
```

## 📁 **Estrutura de Saída**

```
visualizacoes/
├── desempenho_geral.png              # (se matplotlib disponível)
├── correlacao_acertos_tempo.png      # (se matplotlib disponível)
├── top_palavras_acerto.png          # (se matplotlib disponível)
├── acertos_vs_erros.png             # (se matplotlib disponível)
├── alta_taxa_sem_resposta.png       # (se matplotlib disponível)
├── distribuicao_idade.png            # (se matplotlib + dados demográficos)
├── distribuicao_genero.png           # (se matplotlib + dados demográficos)
├── distribuicao_escolaridade.png     # (se matplotlib + dados demográficos)
├── acertos_vs_tempo_interativo.html # (se plotly disponível)
├── dashboard_palavras_interativo.html # (se plotly disponível)
├── resumo_estatistico_teste.csv     # (sempre gerado)
└── resumo_estatistico_palavras.csv  # (sempre gerado)
```

## 🎨 **Detecção Automática de Recursos**

O script detecta automaticamente:

| Biblioteca | Funcionalidade | Status |
|------------|----------------|---------|
| **pandas** | Carregamento de dados | ✅ Obrigatória |
| **numpy** | Cálculos estatísticos | ✅ Obrigatória |
| **matplotlib** | Gráficos estáticos | 🟡 Recomendada |
| **seaborn** | Estilos avançados | 🟠 Opcional |
| **plotly** | Gráficos interativos | 🔴 Opcional |

## 🔧 **Personalização**

### **Modificar Cores**
```python
# No script, altere as cores dos gráficos
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
```

### **Alterar Tamanhos**
```python
# Modifique o tamanho das figuras
plt.rcParams['figure.figsize'] = (15, 10)
```

### **Adicionar Novos Gráficos**
```python
def novo_grafico(self):
    """Adicione sua nova visualização aqui"""
    if not MATPLOTLIB_AVAILABLE:
        print("❌ Matplotlib não disponível")
        return
        
    plt.figure(figsize=(10, 6))
    # Seu código aqui
    plt.savefig(f"{self.output_dir}/novo_grafico.png")
    plt.show()
```

## 📊 **Interpretação dos Gráficos**

### **Distribuição de Acertos**
- **Pico à direita**: Maioria dos participantes teve bom desempenho
- **Pico à esquerda**: Maioria teve dificuldade
- **Distribuição normal**: Desempenho equilibrado

### **Acertos vs Tempo**
- **Correlação negativa**: Quem acerta mais, responde mais rápido
- **Correlação positiva**: Quem acerta mais, demora mais
- **Sem correlação**: Não há relação clara

### **Taxa de Acerto por Palavra**
- **Palavras fáceis**: Taxa > 70%
- **Palavras médias**: Taxa 30-70%
- **Palavras difíceis**: Taxa < 30%

## 🐛 **Solução de Problemas**

### **Erro: "No module named 'matplotlib'"**
```bash
pip install matplotlib
```

### **Erro: "No module named 'plotly'"**
```bash
pip install plotly
```

### **Gráficos não aparecem**
- Verifique se está executando em ambiente com interface gráfica
- Use `plt.savefig()` para salvar sem exibir
- Execute em Jupyter Notebook ou similar

### **Dados não carregam**
- Verifique se os arquivos CSV existem
- Confirme os caminhos dos arquivos
- Execute primeiro os scripts de análise

## 📚 **Recursos Adicionais**

### **Documentação das Bibliotecas**
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [Pandas](https://pandas.pydata.org/)

### **Exemplos de Uso**
- [Galeria Matplotlib](https://matplotlib.org/gallery/)
- [Exemplos Plotly](https://plotly.com/python/plotly-fundamentals/)

## 🤝 **Contribuição**

Para adicionar novas visualizações:
1. Crie uma nova função no script
2. **SEMPRE** verifique se as dependências estão disponíveis
3. Adicione chamada na função principal
4. Documente o novo gráfico
5. Teste com diferentes conjuntos de dados

## 💡 **Vantagens da Abordagem Unificada**

1. **✅ Simplicidade**: Um único script para todas as necessidades
2. **🎯 Inteligência**: Detecta automaticamente o que está disponível
3. **🚀 Flexibilidade**: Funciona em diferentes ambientes
4. **📊 Adaptabilidade**: Se adapta aos recursos disponíveis
5. **💡 Orientação**: Sugere instalações quando necessário
6. **🔧 Manutenção**: Mais fácil de manter e atualizar

---

**🎉 Agora você tem um sistema de visualização inteligente que se adapta automaticamente ao seu ambiente!**
