import pandas as pd
import os

# Configurações
INPUT_FILE = "Respostas_do_Formulario_1.csv"
OUTPUT_DIR = "form_analises"

# Criar diretório de saída se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

def carregar_dados():
    """Carrega o arquivo CSV de entrada"""
    try:
        df = pd.read_csv(INPUT_FILE, header=None)
        print(f"Dados carregados com sucesso: {df.shape[0]} linhas, {df.shape[1]} colunas")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo {INPUT_FILE} não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def percentual_PM_1_Sim(colunas_desejadas):
    """
    Calcula a porcentagem de respostas 'Sim' e 'Não' para as colunas 15-26
    (excluindo coluna 22)
    """
    # Obtendo o número de linhas
    n_linhas = colunas_desejadas.shape[0]
    contador_sim = 0

    # Iterando sobre as linhas
    for i in range(1, n_linhas):
        # Pegando os dados dessa linha nas colunas selecionadas
        linha = colunas_desejadas.iloc[i]

        for idx, valor in linha.items():
            # Verificar se o valor não é NaN
            if not pd.isna(valor):
                # Remover espaços apenas se o valor não for NaN
                valor = str(valor).strip()

                # Excluindo a coluna 22 e verificando as condições de "não"
                if idx + 1 != 22:  # Exclui a coluna 22 (índice 21)

                    # Verifica se o valor não é "Não" (ignorando maiúsculas/minúsculas) e não é vazio
                    if valor.lower() != "não" and valor != "":
                        contador_sim += 1
                        break  # Para o loop interno após encontrar o primeiro valor válido

    # Ajustando o número de linhas para ignorar o cabeçalho
    n_linhas = n_linhas - 1  # removendo a contagem da linha do cabeçalho

    # Calcular a porcentagem de "sim" e "não"
    porcentagem_sim = round((contador_sim / n_linhas) * 100, 2)
    porcentagem_não = round(((n_linhas - contador_sim) / n_linhas) * 100, 2)

    # Criar um DataFrame com o resultado
    resultado = pd.DataFrame({
        'PM 1 Sim': [porcentagem_sim],
        'All não': [porcentagem_não]
    })

    # Salvar no CSV
    output_path = os.path.join(OUTPUT_DIR, "resultado_percentual.csv")
    resultado.to_csv(output_path, index=False, encoding="utf-8")

    # Exibir o resultado
    print("=== Resultado Percentual ===")
    print(resultado)
    print(f"Arquivo salvo em: {output_path}")

def PM_1_Sim(colunas_desejadas):
    """
    Analisa cada linha individualmente para determinar se tem pelo menos um 'Sim'
    """
    # Obtendo o número de linhas
    n_linhas = len(colunas_desejadas)  # Número total de linhas
    resultados = []  # Lista para armazenar os resultados

    # Iterando sobre as linhas
    for i in range(1, n_linhas):
        # Pegando os dados dessa linha nas colunas selecionadas
        linha = colunas_desejadas.iloc[i]

        valor_valido_encontrado = False  # Flag para indicar se um valor válido foi encontrado

        for idx, valor in linha.items():
            # Verificar se o valor não é NaN
            if not pd.isna(valor):
                # Remover espaços apenas se o valor não for NaN
                valor = str(valor).strip()

                # Excluindo a coluna 22 e verificando as condições de "não"
                if idx + 1 != 22:  # Exclui a coluna 22 (índice 21)

                    # Verifica se o valor não é "Não" (ignorando maiúsculas/minúsculas) e não é vazio
                    if valor.lower() != "não" and valor != "":
                        valor_valido_encontrado = True
                        break  # Para o loop interno após encontrar o primeiro valor válido

        # Determina se a linha teve "sim" ou "não"
        if valor_valido_encontrado:
            resultado = 'PM 1 Sim'  # Pelo menos um "Sim"
        else:
            resultado = 'All não'  # Todos "Não"

        # Adiciona o resultado na lista
        resultados.append([i , resultado])  # ID da linha é i (porque começa do índice 0)

    # Criar um DataFrame com os resultados
    resultado_df = pd.DataFrame(resultados, columns=['ID', 'Resultado'])

    # Salvar no CSV
    output_path = os.path.join(OUTPUT_DIR, "resultados_por_linha.csv")
    resultado_df.to_csv(output_path, index=False, encoding="utf-8")

    # Exibir o resultado
    print("=== Resultados por Linha ===")
    print(resultado_df.head(10))  # Mostra apenas as primeiras 10 linhas
    print(f"Arquivo salvo em: {output_path}")

def soma_form(colunas_desejadas):
    """
    Soma os valores das colunas 26-33 (primeiro dígito de cada valor)
    """
    # Criar lista para armazenar os resultados
    resultados = []

    # Iterar sobre as linhas
    for i in range(1, len(colunas_desejadas)):
        soma = 0  # Inicializa a soma para a linha atual

        for valor in colunas_desejadas.iloc[i]:
            # Verifica se o valor não é NaN
            if pd.notna(valor):
                valor = str(valor).strip()  # Converte para string e remove espaços

                # Verifica se o primeiro caractere é um número antes de tentar converter
                if valor and valor[0].isdigit():
                    soma += int(valor[0])  # Adiciona o primeiro caractere como número

        # Adiciona o ID da linha e a soma à lista de resultados
        resultados.append([i , soma])  # O ID da linha começa em 1

    # Criar DataFrame com os resultados
    resultado_df = pd.DataFrame(resultados, columns=['ID', 'Soma'])

    # Salvar no CSV
    output_path = os.path.join(OUTPUT_DIR, "soma_por_linha.csv")
    resultado_df.to_csv(output_path, index=False, encoding="utf-8")

    # Exibir o resultado
    print("=== Soma por Linha ===")
    print(resultado_df.head(10))  # Mostra apenas as primeiras 10 linhas
    print(f"Arquivo salvo em: {output_path}")

def processar_dados_demograficos(df):
    """
    Processa e formata os dados demográficos (colunas 3, 4, 5, 7, 8, 10, 11)
    """
    # Selecionar as colunas desejadas (baseado em índices que começam em 0)
    colunas_desejadas = df.iloc[:, [3, 4, 5, 7, 8, 10, 11]].copy()

    # Dicionários de substituição para abreviação
    map_genero = {
        "Masculino (M)": "M",
        "Femnino (F)": "F",
        "Não Binário (NB)": "NB"
    }

    map_escolaridade = {
        "Superior incompleto": "SI",
        "Médio completo": "MC",
        "Médio incompleto": "MI",
        "Mestrado incompleto": "MeI",
        "Superior completo": "SC",
        "Mestrado completo": "MeC"
    }

    map_estado_civil = {
        "Solteiro": "S",
        "Casado": "C",
        "Separado": "Sep"
    }

    map_renda = {
        "Até 2 salários mínimos": "≤2 SM",
        "Até 3 salários mínimos": "≤3 SM",
        "De 3 a 5 salários mínimos": "3-5 SM",
        "De 4 a 6 salários mínimos": "4-6 SM",
        "De 6 a 10 salários mínimos": "6-10 SM",
        "De 7 a 11 salários mínimos": "7-11 SM",
        "Acima de 10 salários mínimos": ">10 SM",
        "Acima de 11 salários mínimos": ">11 SM"
    }

    # Aplicar as substituições
    colunas_desejadas.iloc[:, 1] = colunas_desejadas.iloc[:, 1].replace(map_genero)
    colunas_desejadas.iloc[:, 2] = colunas_desejadas.iloc[:, 2].replace(map_escolaridade)
    colunas_desejadas.iloc[:, 4] = colunas_desejadas.iloc[:, 4].replace(map_estado_civil)
    colunas_desejadas.iloc[:, 5] = colunas_desejadas.iloc[:, 5].replace(map_renda)
    colunas_desejadas.iloc[:, 6] = colunas_desejadas.iloc[:, 6].replace(map_renda)

    # Remover as linhas que contêm apenas títulos de perguntas
    colunas_desejadas = colunas_desejadas[~colunas_desejadas.iloc[:, 1].str.contains("Gênero", na=False)]
    colunas_desejadas = colunas_desejadas[~colunas_desejadas.iloc[:, 2].str.contains("Qual sua escolaridade?", na=False)]
    colunas_desejadas = colunas_desejadas[~colunas_desejadas.iloc[:, 4].str.contains("Estado civil:", na=False)]
    colunas_desejadas = colunas_desejadas[~colunas_desejadas.iloc[:, 5].str.contains("Renda Familiar", na=False)]
    colunas_desejadas = colunas_desejadas[~colunas_desejadas.iloc[:, 6].str.contains("Renda pessoal", na=False)]

    # Definindo os cabeçalhos conforme solicitado
    colunas_desejadas.columns = ['Idade', 'Gênero', 'Escolaridade','Área', 'Estado Civil', 'Renda Familiar', 'Renda Pessoal']

    # Adicionar uma coluna de ID
    colunas_desejadas.insert(0, 'ID', range(1, len(colunas_desejadas) + 1))

    # Salvar o novo DataFrame filtrado e formatado com os cabeçalhos atualizados
    output_path = os.path.join(OUTPUT_DIR, "tabela_filtrada_formatada.csv")
    colunas_desejadas.to_csv(output_path, index=False, encoding="utf-8")

    # Exibir as primeiras linhas para verificar
    print("=== Dados Demográficos ===")
    print(colunas_desejadas.head())
    print(f"Arquivo salvo em: {output_path}")

def main():
    """Função principal que executa todas as análises"""
    print("=== Análise do Formulário RAT ===")
    print(f"Arquivo de entrada: {INPUT_FILE}")
    print(f"Diretório de saída: {OUTPUT_DIR}")
    print()

    # Carregar dados
    df = carregar_dados()
    if df is None:
        return

    # Análise 1: Percentual PM 1 Sim (colunas 15-26)
    print("\n1. Analisando percentual PM 1 Sim...")
    colunas_15_26 = df.iloc[:, 14:26]  # A partir da coluna 15 até a 26 (baseado em zero)
    percentual_PM_1_Sim(colunas_15_26)

    # Análise 2: PM 1 Sim por linha (colunas 15-26)
    print("\n2. Analisando PM 1 Sim por linha...")
    PM_1_Sim(colunas_15_26)

    # Análise 3: Soma do formulário (colunas 26-33)
    print("\n3. Calculando soma do formulário...")
    colunas_26_33 = df.iloc[:, 26:33]  # A partir da coluna 26 até a 33 (baseado em zero)
    soma_form(colunas_26_33)

    # Análise 4: Dados demográficos
    print("\n4. Processando dados demográficos...")
    processar_dados_demograficos(df)

    print("\n=== Análise concluída! ===")
    print(f"Todos os arquivos foram salvos em: {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 