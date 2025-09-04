import pandas as pd
import numpy as np
import os
from pathlib import Path

# Detecção automática de dependências
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
    print("✅ Matplotlib disponível - Gráficos estáticos habilitados")
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("⚠️  Matplotlib não encontrado - Gráficos estáticos desabilitados")

try:
    import seaborn as sns
    SEABORN_AVAILABLE = True
    print("✅ Seaborn disponível - Estilos avançados habilitados")
except ImportError:
    SEABORN_AVAILABLE = False
    print("⚠️  Seaborn não encontrado - Usando estilos básicos")

try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
    print("✅ Plotly disponível - Gráficos interativos habilitados")
except ImportError:
    PLOTLY_AVAILABLE = False
    print("⚠️  Plotly não encontrado - Gráficos interativos desabilitados")

class VisualizadorRATUnificado:
    def __init__(self, modo="auto"):
        """
        Inicializa o visualizador unificado
        
        Args:
            modo (str): "auto" (detecta automaticamente), "basico", "completo", "interativo"
        """
        self.output_dir = "visualizacoes"
        self.modo = modo
        self.criar_diretorio_saida()
        self.configurar_estilos()
        
    def criar_diretorio_saida(self):
        """Cria o diretório de saída para as visualizações"""
        Path(self.output_dir).mkdir(exist_ok=True)
        
    def configurar_estilos(self):
        """Configura estilos baseado nas bibliotecas disponíveis"""
        if MATPLOTLIB_AVAILABLE:
            plt.rcParams['figure.figsize'] = (12, 8)
            plt.rcParams['font.size'] = 10
            
            if SEABORN_AVAILABLE:
                try:
                    plt.style.use('seaborn-v0_8')
                    sns.set_palette("husl")
                    print("🎨 Estilos Seaborn aplicados")
                except:
                    plt.style.use('default')
                    print("🎨 Estilos padrão do Matplotlib aplicados")
            else:
                plt.style.use('default')
                print("🎨 Estilos básicos do Matplotlib aplicados")
    
    def carregar_dados(self):
        """Carrega todos os dados necessários para visualização"""
        try:
            # Dados de teste (obrigatórios)
            self.dados_teste = pd.read_csv("output_teste/dados_etapa_01.csv")
            self.resultado_final = pd.read_csv("output_teste/resultado_final.csv")
            
            # Dados opcionais
            self.dados_carregados = {
                'teste': True,
                'formulario': False,
                'demografico': False
            }
            
            # Tentar carregar dados de formulário
            try:
                self.resultado_percentual = pd.read_csv("form_analises/resultado_percentual.csv")
                self.tabela_filtrada = pd.read_csv("form_analises/tabela_filtrada_formatada.csv")
                self.dados_carregados['formulario'] = True
            except:
                print("⚠️  Dados de formulário não encontrados")
            
                        # Tentar carregar dados demográficos
            try:
                self.idade = pd.read_csv("analise_percentual_form/idade.csv")
                print(f"✅ Dados de idade carregados: {len(self.idade)} registros")
                
                self.genero = pd.read_csv("analise_percentual_form/Gênero.csv")
                print(f"✅ Dados de gênero carregados: {len(self.genero)} registros")
                
                self.escolaridade = pd.read_csv("analise_percentual_form/escolaridade.csv")
                print(f"✅ Dados de escolaridade carregados: {len(self.escolaridade)} registros")
                
                # Tentar carregar dados opcionais
                try:
                    self.estado_civil = pd.read_csv("analise_percentual_form/Estado_civil.csv")
                    print(f"✅ Dados de estado civil carregados: {len(self.estado_civil)} registros")
                except:
                    print("⚠️  Dados de estado civil não encontrados")
                    
                try:
                    self.graduacao = pd.read_csv("analise_percentual_form/Graduação.csv")
                    print(f"✅ Dados de graduação carregados: {len(self.graduacao)} registros")
                except:
                    print("⚠️  Dados de graduação não encontrados")
                    
                try:
                    self.renda_familiar = pd.read_csv("analise_percentual_form/Renda_familiar.csv")
                    print(f"✅ Dados de renda familiar carregados: {len(self.renda_familiar)} registros")
                except:
                    print("⚠️  Dados de renda familiar não encontrados")
                    
                try:
                    self.renda_pessoal = pd.read_csv("analise_percentual_form/Renda_pessoal.csv")
                    print(f"✅ Dados de renda pessoal carregados: {len(self.renda_pessoal)} registros")
                except:
                    print("⚠️  Dados de renda pessoal não encontrados")
                
                self.dados_carregados['demografico'] = True
                print("✅ Todos os dados demográficos principais foram carregados com sucesso!")
                
                # Mostrar informações sobre as colunas disponíveis
                print("\n📊 ESTRUTURA DOS DADOS DEMOGRÁFICOS:")
                print(f"Idade: {list(self.idade.columns)}")
                print(f"Gênero: {list(self.genero.columns)}")
                print(f"Escolaridade: {list(self.escolaridade.columns)}")
                
            except Exception as e:
                print(f"⚠️  Erro ao carregar dados demográficos: {e}")
                print("⚠️  Visualizações demográficas serão desabilitadas")
            
            print("✅ Dados básicos carregados com sucesso!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
            return False
    
    def visualizacao_desempenho_geral(self):
        """Cria visualizações do desempenho geral dos participantes"""
        if not MATPLOTLIB_AVAILABLE:
            print("❌ Matplotlib não disponível para gráficos estáticos")
            return
            
        print("📊 Criando visualizações de desempenho geral...")
        
        # 1. Distribuição de acertos
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Histograma de acertos
        axes[0, 0].hist(self.dados_teste['corr'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribuição de Acertos por Participante', fontsize=14, fontweight='bold')
        axes[0, 0].set_xlabel('Número de Acertos')
        axes[0, 0].set_ylabel('Frequência')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Boxplot de acertos
        axes[0, 1].boxplot(self.dados_teste['corr'], patch_artist=True, 
                           boxprops=dict(facecolor='lightgreen', alpha=0.7))
        axes[0, 1].set_title('Boxplot de Acertos', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Número de Acertos')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Distribuição de tempo de resposta
        axes[1, 0].hist(self.dados_teste['rt'], bins=20, alpha=0.7, color='salmon', edgecolor='black')
        axes[1, 0].set_title('Distribuição de Tempo de Resposta', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('Tempo de Resposta (ms)')
        axes[1, 0].set_ylabel('Frequência')
        axes[1, 0].grid(True, alpha=0.3)
        
        # Scatter plot: Acertos vs Tempo
        axes[1, 1].scatter(self.dados_teste['corr'], self.dados_teste['rt'], 
                           alpha=0.6, color='purple', s=50)
        axes[1, 1].set_title('Acertos vs Tempo de Resposta', fontsize=14, fontweight='bold')
        axes[1, 1].set_xlabel('Número de Acertos')
        axes[1, 1].set_ylabel('Tempo de Resposta (ms)')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/desempenho_geral.png", dpi=300, bbox_inches='tight')
        plt.show()
        
        # 2. Gráfico de correlação entre acertos e tempo
        corr_coef = np.corrcoef(self.dados_teste['corr'], self.dados_teste['rt'])[0, 1]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(self.dados_teste['corr'], self.dados_teste['rt'], 
                           c=self.dados_teste['corr'], cmap='viridis', alpha=0.7, s=60)
        ax.set_title(f'Correlação entre Acertos e Tempo de Resposta\n(r = {corr_coef:.3f})', 
                    fontsize=16, fontweight='bold')
        ax.set_xlabel('Número de Acertos', fontsize=12)
        ax.set_ylabel('Tempo de Resposta (ms)', fontsize=12)
        ax.grid(True, alpha=0.3)
        
        # Adicionar linha de tendência
        z = np.polyfit(self.dados_teste['corr'], self.dados_teste['rt'], 1)
        p = np.poly1d(z)
        ax.plot(self.dados_teste['corr'], p(self.dados_teste['corr']), "r--", alpha=0.8, linewidth=2)
        
        plt.colorbar(scatter, ax=ax, label='Número de Acertos')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/correlacao_acertos_tempo.png", dpi=300, bbox_inches='tight')
        plt.show()
    
    def visualizacao_palavras(self):
        """Cria visualizações específicas para análise das palavras"""
        if not MATPLOTLIB_AVAILABLE:
            print("❌ Matplotlib não disponível para gráficos estáticos")
            return
            
        print("📝 Criando visualizações de análise de palavras...")
        
        # 1. Top 10 palavras com maior taxa de acerto
        top_acertos = self.resultado_final.nlargest(10, 'porcentagem_acertos')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.barh(top_acertos['corranswer'], top_acertos['porcentagem_acertos'], 
                       color='lightgreen', alpha=0.8, edgecolor='black')
        ax.set_title('Top 10 Palavras com Maior Taxa de Acerto', fontsize=16, fontweight='bold')
        ax.set_xlabel('Taxa de Acerto (%)', fontsize=12)
        ax.set_ylabel('Palavra', fontsize=12)
        ax.grid(True, alpha=0.3, axis='x')
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                   f'{width:.1f}%', ha='left', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/top_palavras_acerto.png", dpi=300, bbox_inches='tight')
        plt.show()
        
        # 2. Comparação entre acertos e erros por palavra
        fig, ax = plt.subplots(figsize=(14, 10))
        
        x = np.arange(len(self.resultado_final))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, self.resultado_final['porcentagem_acertos'], 
                       width, label='Acertos (%)', color='lightgreen', alpha=0.8)
        bars2 = ax.bar(x + width/2, self.resultado_final['porcentagem_erros'], 
                       width, label='Erros (%)', color='lightcoral', alpha=0.8)
        
        ax.set_title('Comparação: Acertos vs Erros por Palavra', fontsize=16, fontweight='bold')
        ax.set_xlabel('Palavras', fontsize=12)
        ax.set_ylabel('Percentual (%)', fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(self.resultado_final['corranswer'], rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/acertos_vs_erros.png", dpi=300, bbox_inches='tight')
        plt.show()
        
        # 3. Análise de respostas sem resposta
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Filtrar palavras com alta taxa de "sem resposta"
        high_no_response = self.resultado_final[self.resultado_final['porcentagem_noreponse'] > 20]
        
        bars = ax.bar(high_no_response['corranswer'], high_no_response['porcentagem_noreponse'], 
                       color='orange', alpha=0.8, edgecolor='black')
        ax.set_title('Palavras com Alta Taxa de "Sem Resposta" (>20%)', fontsize=16, fontweight='bold')
        ax.set_xlabel('Palavra', fontsize=12)
        ax.set_ylabel('Percentual de "Sem Resposta" (%)', fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/alta_taxa_sem_resposta.png", dpi=300, bbox_inches='tight')
        plt.show()
    
    def visualizacao_demografica(self):
        """Cria visualizações demográficas se os dados estiverem disponíveis"""
        if not MATPLOTLIB_AVAILABLE:
            print("❌ Matplotlib não disponível para gráficos estáticos")
            return
            
        if not self.dados_carregados['demografico']:
            print("⚠️  Dados demográficos não disponíveis")
            return
            
        print("👥 Criando visualizações demográficas...")
        
        try:
            # 1. Distribuição por idade
            if 'faixa_idade' in self.idade.columns and 'contagem' in self.idade.columns:
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(self.idade['faixa_idade'], self.idade['contagem'], 
                               color='skyblue', alpha=0.8, edgecolor='black')
                ax.set_title('Distribuição de Participantes por Faixa Etária', fontsize=16, fontweight='bold')
                ax.set_xlabel('Faixa Etária', fontsize=12)
                ax.set_ylabel('Número de Participantes', fontsize=12)
                ax.grid(True, alpha=0.3, axis='y')
                
                # Adicionar percentuais nas barras se disponível
                if 'porcentagem' in self.idade.columns:
                    for i, bar in enumerate(bars):
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                               f'{self.idade.iloc[i]["porcentagem"]:.1f}%', 
                               ha='center', va='bottom', fontweight='bold')
                
                plt.tight_layout()
                plt.savefig(f"{self.output_dir}/distribuicao_idade.png", dpi=300, bbox_inches='tight')
                plt.show()
                print("✅ Gráfico de idade criado com sucesso")
            else:
                print("⚠️  Colunas necessárias para gráfico de idade não encontradas")
            
            # 2. Distribuição por gênero
            if 'Gênero' in self.genero.columns and 'contagem' in self.genero.columns:
                fig, ax = plt.subplots(figsize=(8, 8))
                colors = ['lightpink', 'lightblue', 'lightgreen']
                wedges, texts, autotexts = ax.pie(self.genero['contagem'], 
                                                 labels=self.genero['Gênero'],
                                                 autopct='%1.1f%%',
                                                 colors=colors,
                                                 startangle=90)
                ax.set_title('Distribuição de Participantes por Gênero', fontsize=16, fontweight='bold')
                
                # Estilizar textos
                for autotext in autotexts:
                    autotext.set_color('white')
                    autotext.set_fontweight('bold')
                
                plt.tight_layout()
                plt.savefig(f"{self.output_dir}/distribuicao_genero.png", dpi=300, bbox_inches='tight')
                plt.show()
                print("✅ Gráfico de gênero criado com sucesso")
            else:
                print("⚠️  Colunas necessárias para gráfico de gênero não encontradas")
            
            # 3. Distribuição por escolaridade
            if 'escolaridade' in self.escolaridade.columns and 'contagem' in self.escolaridade.columns:
                fig, ax = plt.subplots(figsize=(12, 8))
                bars = ax.bar(self.escolaridade['escolaridade'], self.escolaridade['contagem'], 
                               color='lightcoral', alpha=0.8, edgecolor='black')
                ax.set_title('Distribuição de Participantes por Escolaridade', fontsize=16, fontweight='bold')
                ax.set_xlabel('Nível de Escolaridade', fontsize=12)
                ax.set_ylabel('Número de Participantes', fontsize=12)
                ax.grid(True, alpha=0.3, axis='y')
                
                # Rotacionar labels para melhor legibilidade
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig(f"{self.output_dir}/distribuicao_escolaridade.png", dpi=300, bbox_inches='tight')
                plt.show()
                print("✅ Gráfico de escolaridade criado com sucesso")
            else:
                print("⚠️  Colunas necessárias para gráfico de escolaridade não encontradas")
                
        except Exception as e:
            print(f"❌ Erro durante criação de visualizações demográficas: {e}")
            print("💡 Verifique se os arquivos CSV têm as colunas esperadas")
    
    def visualizacao_interativa(self):
        """Cria visualizações interativas usando Plotly se disponível"""
        if not PLOTLY_AVAILABLE:
            print("❌ Plotly não disponível para gráficos interativos")
            return
            
        print("🎯 Criando visualizações interativas...")
        
        # 1. Gráfico interativo de acertos vs tempo
        fig = px.scatter(self.dados_teste, x='corr', y='rt', 
                        color='corr', size='corr',
                        title='Acertos vs Tempo de Resposta (Interativo)',
                        labels={'corr': 'Número de Acertos', 'rt': 'Tempo de Resposta (ms)'},
                        hover_data=['ID'])
        
        fig.update_layout(
            title_font_size=16,
            title_font_color='darkblue',
            showlegend=True
        )
        
        fig.write_html(f"{self.output_dir}/acertos_vs_tempo_interativo.html")
        print(f"✅ Gráfico interativo salvo em: {self.output_dir}/acertos_vs_tempo_interativo.html")
        
        # 2. Dashboard interativo de palavras
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Taxa de Acerto por Palavra', 'Taxa de Erro por Palavra',
                           'Tentativas por Palavra', 'Respostas Sem Resposta'),
            specs=[[{"type": "bar"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "bar"}]]
        )
        
        # Taxa de acerto
        fig.add_trace(
            go.Bar(x=self.resultado_final['corranswer'], 
                   y=self.resultado_final['porcentagem_acertos'],
                   name='Taxa de Acerto', marker_color='lightgreen'),
            row=1, col=1
        )
        
        # Taxa de erro
        fig.add_trace(
            go.Bar(x=self.resultado_final['corranswer'], 
                   y=self.resultado_final['porcentagem_erros'],
                   name='Taxa de Erro', marker_color='lightcoral'),
            row=1, col=2
        )
        
        # Tentativas
        fig.add_trace(
            go.Bar(x=self.resultado_final['corranswer'], 
                   y=self.resultado_final['tentativas'],
                   name='Tentativas', marker_color='lightblue'),
            row=2, col=1
        )
        
        # Sem resposta
        fig.add_trace(
            go.Bar(x=self.resultado_final['corranswer'], 
                   y=self.resultado_final['porcentagem_noreponse'],
                   name='Sem Resposta', marker_color='orange'),
            row=2, col=2
        )
        
        fig.update_layout(
            title_text="Dashboard de Análise de Palavras RAT",
            title_font_size=20,
            height=800,
            showlegend=False
        )
        
        fig.write_html(f"{self.output_dir}/dashboard_palavras_interativo.html")
        print(f"✅ Dashboard interativo salvo em: {self.output_dir}/dashboard_palavras_interativo.html")
    
    def resumo_estatistico(self):
        """Gera um resumo estatístico dos dados"""
        print("📋 Gerando resumo estatístico...")
        
        # Resumo dos dados de teste
        resumo_teste = self.dados_teste.describe()
        
        # Resumo das palavras
        resumo_palavras = self.resultado_final.describe()
        
        # Salvar resumos
        resumo_teste.to_csv(f"{self.output_dir}/resumo_estatistico_teste.csv")
        resumo_palavras.to_csv(f"{self.output_dir}/resumo_estatistico_palavras.csv")
        
        print("✅ Resumos estatísticos salvos!")
        
        # Exibir resumos
        print("\n📊 RESUMO ESTATÍSTICO - DADOS DE TESTE:")
        print(resumo_teste)
        
        print("\n📊 RESUMO ESTATÍSTICO - ANÁLISE DE PALAVRAS:")
        print(resumo_palavras)
        
        # Estatísticas adicionais
        print(f"\n🎯 ESTATÍSTICAS ADICIONAIS:")
        print(f"Total de participantes: {len(self.dados_teste)}")
        print(f"Total de palavras analisadas: {len(self.resultado_final)}")
        print(f"Média de acertos por participante: {self.dados_teste['corr'].mean():.2f}")
        print(f"Desvio padrão de acertos: {self.dados_teste['corr'].std():.2f}")
        print(f"Palavra com maior taxa de acerto: {self.resultado_final.loc[self.resultado_final['porcentagem_acertos'].idxmax(), 'corranswer']}")
        print(f"Palavra com menor taxa de acerto: {self.resultado_final.loc[self.resultado_final['porcentagem_acertos'].idxmin(), 'corranswer']}")
    
    def gerar_relatorio_completo(self):
        """Gera todas as visualizações disponíveis baseado nas dependências"""
        print("🚀 VISUALIZADOR UNIFICADO DE DADOS RAT")
        print("=" * 60)
        
        # Detectar modo automaticamente se não especificado
        if self.modo == "auto":
            if PLOTLY_AVAILABLE and MATPLOTLIB_AVAILABLE:
                self.modo = "completo"
            elif MATPLOTLIB_AVAILABLE:
                self.modo = "basico"
            else:
                self.modo = "minimo"
        
        print(f"🎯 Modo selecionado: {self.modo}")
        print(f"📊 Dependências: Matplotlib={MATPLOTLIB_AVAILABLE}, Plotly={PLOTLY_AVAILABLE}, Seaborn={SEABORN_AVAILABLE}")
        
        if not self.carregar_dados():
            print("❌ Não foi possível carregar os dados. Verifique se os arquivos existem.")
            return
        
        # Gerar visualizações baseado no modo
        if self.modo in ["completo", "basico"]:
            self.visualizacao_desempenho_geral()
            self.visualizacao_palavras()
            
            if self.dados_carregados['demografico']:
                self.visualizacao_demografica()
        
        if self.modo == "completo" and PLOTLY_AVAILABLE:
            self.visualizacao_interativa()
        
        # Sempre gerar resumo estatístico
        self.resumo_estatistico()
        
        # Resumo do que foi gerado
        print(f"\n🎉 Relatório gerado com sucesso!")
        print(f"📁 Todas as visualizações foram salvas em: {self.output_dir}/")
        
        if MATPLOTLIB_AVAILABLE:
            print(f"📊 Gráficos estáticos: .png")
        if PLOTLY_AVAILABLE:
            print(f"🎯 Gráficos interativos: .html")
        print(f"📋 Resumos estatísticos: .csv")
        
        # Sugestões de instalação
        if not MATPLOTLIB_AVAILABLE:
            print(f"\n💡 Para gráficos estáticos: pip install matplotlib")
        if not PLOTLY_AVAILABLE:
            print(f"💡 Para gráficos interativos: pip install plotly")
        if not SEABORN_AVAILABLE:
            print(f"💡 Para estilos avançados: pip install seaborn")

def main():
    """Função principal com opções de modo"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Visualizador Unificado de Dados RAT')
    parser.add_argument('--modo', choices=['auto', 'minimo', 'basico', 'completo'], 
                       default='auto', help='Modo de visualização')
    
    args = parser.parse_args()
    
    visualizador = VisualizadorRATUnificado(modo=args.modo)
    visualizador.gerar_relatorio_completo()

if __name__ == "__main__":
    main()
