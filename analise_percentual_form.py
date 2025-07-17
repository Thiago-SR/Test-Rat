import pandas as pd
import os
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurações centralizadas
CONFIG = {
    'arquivo_entrada': "Excel RAT ref - Respostas do Formulário 1.csv",
    'pasta_destino': "analise_percentual_form",
    'encoding': "utf-8",
    'casas_decimais': 2
}

def criar_pasta_destino():
    """Cria a pasta de destino se não existir."""
    pasta = Path(CONFIG['pasta_destino'])
    pasta.mkdir(exist_ok=True)
    logger.info(f"Pasta de destino criada/verificada: {pasta}")

def carregar_dados():
    """Carrega os dados do arquivo CSV."""
    try:
        df = pd.read_csv(CONFIG['arquivo_entrada'])
        logger.info(f"Dados carregados com sucesso. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {CONFIG['arquivo_entrada']}")
        raise
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        raise

def dados_idade(df):
    """
    Analisa e categoriza dados de idade em faixas etárias.
    
    Args:
        df: DataFrame com os dados
    """
    try:
        # Verificar se a coluna existe
        if 'Idade ' not in df.columns:
            logger.error("Coluna 'Idade ' não encontrada no DataFrame")
            return
        
        # Remover valores nulos
        df_limpo = df.dropna(subset=['Idade '])
        
        bins = [18, 23, 28, 33, 38, 43, 48, 53]
        labels = ['18-23', '24-28', '29-33', '34-38', '39-43', '44-48', '49-53']
        
        # Cria uma coluna temporária para categorizar as idades
        df_limpo['faixa_idade'] = pd.cut(df_limpo['Idade '], bins=bins, labels=labels, right=True)

        # Contar quantos registros estão em cada faixa de idade
        contagem = df_limpo['faixa_idade'].value_counts().sort_index()
        porcentagem = round((contagem / contagem.sum()) * 100, CONFIG['casas_decimais'])

        resultado_idade = pd.DataFrame({
            'faixa_idade': contagem.index,
            'contagem': contagem.values,
            'porcentagem': porcentagem.values
        })

        arquivo_saida = Path(CONFIG['pasta_destino']) / "idade.csv"
        resultado_idade.to_csv(arquivo_saida, index=False, encoding=CONFIG['encoding'])
        logger.info(f"Análise de idade salva em: {arquivo_saida}")
        
    except Exception as e:
        logger.error(f"Erro na análise de idade: {e}")

def gerar_percentual(df, nome_coluna, coluna_nova, nome_arquivo):
    """
    Gera análise percentual para uma coluna específica.
    
    Args:
        df: DataFrame com os dados
        nome_coluna: Nome da coluna no DataFrame original
        coluna_nova: Nome da coluna no resultado
        nome_arquivo: Nome do arquivo de saída
    """
    try:
        # Verificar se a coluna existe
        if nome_coluna not in df.columns:
            logger.warning(f"Coluna '{nome_coluna}' não encontrada. Pulando...")
            return
        
        # Remover valores nulos
        df_limpo = df.dropna(subset=[nome_coluna])
        
        contagem = df_limpo[nome_coluna].value_counts()
        porcentagens = round((contagem / contagem.sum()) * 100, CONFIG['casas_decimais'])
        
        resultado = pd.DataFrame({
            coluna_nova: contagem.index,
            'contagem': contagem.values,
            'porcentagem': porcentagens.values
        })

        arquivo_saida = Path(CONFIG['pasta_destino']) / f"{nome_arquivo}.csv"
        resultado.to_csv(arquivo_saida, index=False, encoding=CONFIG['encoding'])
        logger.info(f"Análise de '{nome_coluna}' salva em: {arquivo_saida}")
        
    except Exception as e:
        logger.error(f"Erro na análise de '{nome_coluna}': {e}")

def main():
    """Função principal que executa todas as análises."""
    try:
        # Criar pasta de destino
        criar_pasta_destino()
        
        # Carregar dados
        df = carregar_dados()
        
        # Executar análises
        logger.info("Iniciando análises...")
        
        # Análise de idade
        dados_idade(df)
        
        # Análises percentuais
        analises = [
            ('Qual sua escolaridade?', 'escolaridade', 'escolaridade'),
            ('Gênero ', 'Gênero', 'Gênero'),
            ('Área de graduação do ensino superior (se houver): ', 'Graduação', 'Graduação'),
            ('Estado civil: ', 'Estado civil', 'Estado_civil'),
            ('Renda pessoal total mensal: ', 'Renda pessoal', 'Renda_pessoal'),
            ('Renda Familiar (de todos da casa) total mensal: ', 'Renda familiar', 'Renda_familiar')
        ]
        
        for nome_coluna, coluna_nova, nome_arquivo in analises:
            gerar_percentual(df, nome_coluna, coluna_nova, nome_arquivo)
        
        logger.info("Todas as análises foram concluídas com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro na execução principal: {e}")
        raise

if __name__ == "__main__":
    main()
