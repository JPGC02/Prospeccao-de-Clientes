import pandas as pd
import os
import glob

# Diretório onde estão os arquivos CSV
path_csv = 'S:\Projetos\Programacao\Prospeccao de Clientes'

# Diretório onde o arquivo Excel será salvo
path_excel = 'S:\Projetos\Programacao\Prospeccao de Clientes\Excel'

# Lista de todos os arquivos CSV no diretório
csv_files = glob.glob(os.path.join(path_csv, '*.csv'))

# Lista de dataframes dos arquivos CSV
df_list = [pd.read_csv(file) for file in csv_files]

# Concatenar todos os dataframes em um único dataframe
merged_df = pd.concat(df_list)

# Salvar o dataframe mesclado em um arquivo Excel
merged_df.to_excel(os.path.join(path_excel, 'arquivo_mesclado.xlsx'), index=False)
