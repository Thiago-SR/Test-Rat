import csv
import os
import glob
import pandas as pd

def get_available_ids():
    """Função para obter automaticamente todos os IDs disponíveis na pasta Data"""
    if not os.path.exists("Data"):
        print("Pasta Data não encontrada!")
        return []
    
    # Lista todas as pastas na pasta Data
    pastas = [d for d in os.listdir("Data") if os.path.isdir(os.path.join("Data", d))]
    
    # Filtra apenas pastas que são números
    ids_disponiveis = []
    for pasta in pastas:
        try:
            id_num = int(pasta)
            ids_disponiveis.append(id_num)
        except ValueError:
            # Se não for um número, ignora
            continue
    
    # Ordena os IDs para processamento consistente
    ids_disponiveis.sort()
    return ids_disponiveis

def etapa_1():
    # Cria a pasta de output se não existir
    output_dir = "output_teste"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Caminho do arquivo de saida
    caminho_output = os.path.join(output_dir, "dados_etapa_01.csv")
    cabecalho = ["ID", "corr", "rt"]

    with open(caminho_output, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cabecalho)

    # Obtém automaticamente todos os IDs disponíveis
    ids_disponiveis = get_available_ids()
    print(f"IDs encontrados: {ids_disponiveis}")
    
    output = []
    for id in ids_disponiveis:
        #caminhos das pastas de arquivo de entrada
        pasta = f"Data/{id}/"
        corr = 0
        rt = 0

        #busca os arquivos csv da pasta
        padrao = os.path.join(pasta, "*.csv")
        arquivos_csv = glob.glob(padrao)
        try:

            if arquivos_csv:
                #abre o primeiro arquivo csv
                df = pd.read_csv(arquivos_csv[0])
                df = df.dropna()#remove as linhas vazias
                for index, row in df.iterrows():
                    corr += row['corr']
                    rt += row['rt']
                rt = round(rt/len(df),2)
                output.append([id, corr, rt])
            else:
                print(f"Nenhum arquivo CSV encontrado na pasta {pasta}.")

        except Exception as e:
            print(f"Erro ao processar o arquivo {id}: {e}")
    
    #salva os dados no arquivo de saida
    with open(caminho_output, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(output)
    
    print(f"Arquivo salvo em: {caminho_output}")


def etapa_2():
    # Cria a pasta de output se não existir
    output_dir = "output_teste"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Obtém automaticamente todos os IDs disponíveis
    ids_disponiveis = get_available_ids()
    print(f"IDs encontrados: {ids_disponiveis}")
    
    # Monta a lista dos arquivos CSV
    arquivos_csv = []
    for id in ids_disponiveis:
        try:
            # Define o caminho da pasta de entrada para cada id
            pasta = f"Data/{id}/"
            padrao = os.path.join(pasta, "*.csv")
            arquivos_pasta = glob.glob(padrao)
            # Adiciona o primeiro arquivo encontrado na lista
            if arquivos_pasta:
                arquivos_csv.append(arquivos_pasta[0])
        except Exception as e:
            print(f"Erro ao processar pasta {id}: {e}")
            pass

    #Lê todos os arquivos e os armazena em uma lista de dataframes
    lista_df = []
    for arquivo in arquivos_csv:
        try:
            df = pd.read_csv(arquivo)
            lista_df.append(df)
        except Exception as e:
            print(f"Erro ao ler arquivo {arquivo}: {e}")

    # Junta todos os DataFrames em um único
    dados = pd.concat(lista_df, ignore_index=True)

    dados_exp = dados[dados['corranswer'] == 'ARARA']

    # Exibe o DataFrame filtrado
    print(dados_exp)

    #Agrupa os dados pela coluna 'corranswer'
    resultado = dados.groupby('corranswer').agg(
        tentativas=('corr', 'count'),  # total de tentativas para cada palavra correta
        acertos=('corr', 'sum')          # soma dos acertos
    ).reset_index()

    # Calcula as porcentagens de acertos e de erros
    resultado['porcentagem_acertos'] = round((resultado['acertos'] / resultado['tentativas']) * 100, 2)
    resultado['porcentagem_erros'] = round(((resultado['tentativas'] - resultado['acertos']) / resultado['tentativas']) * 100, 2)

    #Função para obter informações extras por grupo
    def get_extra_info(grupo):
        #Filtra as tentativas onde o usuário errou (corr == 0) e a resposta não é "<NO_RESPONSE>"
        wrongs = grupo[(grupo['corr'] == 0) & (grupo['answer'] != "<NO_RESPONSE>")]
        if not wrongs.empty:
            mode_wrong = wrongs['answer'].mode()
            if not mode_wrong.empty:
                palavra_errada = mode_wrong.iloc[0]
            else:
                palavra_errada = None
        else:
            palavra_errada = None

        #Calcula a porcentagem de respostas que foram "<NO_RESPONSE>"
        total = len(grupo)
        no_response_count = (grupo['answer'] == "<NO_RESPONSE>").sum()
        porcentagem_noreponse = (no_response_count / total) * 100 if total > 0 else 0

        return pd.Series({
            'palavra_errada_mais_comum': palavra_errada,
            'porcentagem_noreponse': round(porcentagem_noreponse, 2)
        })

    # Aplica a função em cada grupo (agrupado pela palavra correta)
    extra_info = dados.groupby('corranswer', group_keys=False).apply(get_extra_info).reset_index()

    #Mescla as informações extras com os resultados já calculados
    resultado_final = resultado.merge(extra_info, on='corranswer', how='left')

    #Salva o DataFrame final em um arquivo CSV
    caminho_output = os.path.join(output_dir, "resultado_final.csv")
    resultado_final.to_csv(caminho_output, index=False, encoding="utf-8")
    print(f"Arquivo salvo em: {caminho_output}")


# Função principal para executar ambas as etapas
def main():
    print("Executando Etapa 1...")
    etapa_1()
    print("\nExecutando Etapa 2...")
    etapa_2()
    print("\nProcessamento concluído!!")


if __name__ == "__main__":
    main()



