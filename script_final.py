import os
import pandas as pd

# Garante que a pasta de saída exista
output_dir = "resultado_final"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "tabela_final.csv")

# Leitura dos arquivos CSV
# Cada DataFrame representa uma etapa do processamento
# Os arquivos devem conter a coluna 'ID' para o merge funcionar corretamente

df1 = pd.read_csv("form_analises/tabela_filtrada_formatada.csv")
df2 = pd.read_csv("output_teste/dados_etapa_01.csv")
df3 = pd.read_csv("form_analises/resultados_por_linha.csv")
df4 = pd.read_csv("form_analises/soma_por_linha.csv")

# Realiza os merges de forma encadeada, preservando todos os IDs
# O método 'outer' garante que nenhum dado seja perdido por ausência em algum arquivo

df_merge_1 = pd.merge(df1, df2, on="ID", how="outer")
df_merge_2 = pd.merge(df_merge_1, df3, on="ID", how="outer")
df_final = pd.merge(df_merge_2, df4, on="ID", how="outer")

# Exibe o DataFrame final para conferência
print(df_final)

# Salva o resultado na pasta resultado_final
# O parâmetro index=False evita salvar o índice como coluna no CSV

df_final.to_csv(output_path, index=False)
