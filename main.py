import numpy as np
import pandas as pd
from gender_guesser_br import Genero

# Load the data
data_names = pd.read_csv('br_ibge_nomes_brasil.csv')
data_locals = pd.read_csv('br_bd_diretorios_brasil_municipio.csv')

# create table that relates names and locals by the id_municipio
names_locals_df = pd.merge(data_names, data_locals, on='id_municipio')

# select only the columns that are needed for the final table
name_location_table = names_locals_df[['nome_x', 'nome_y', 'nome_uf', 'nome_regiao', 'quantidade_nascimentos_ate_2010']]

# Agrupar por 'nome' e 'nome_regiao', e somar a coluna 'quantidade_nascimentos'
grouped_df = name_location_table.groupby(['nome_x', 'nome_regiao'])['quantidade_nascimentos_ate_2010'].sum().reset_index()

# Para cada nome, encontra o índice da linha com o maior valor de 'quantidade_nascimentos'
indices = grouped_df.groupby('nome_x')['quantidade_nascimentos_ate_2010'].idxmax()

# Selecionando as linhas com base nos índices encontrados
final_df = grouped_df.loc[indices].reset_index(drop=True)

#create a new colunm for the gender of the names
final_df['genero'] = None

# associate the names to the gender
for line in range(0, len(final_df)):
    name = final_df['nome_x'][line]
    genero = Genero(name)
    final_df.loc[line, 'genero'] = genero()

final_df.to_csv('nomes_locais.csv', sep=',', index=False)

