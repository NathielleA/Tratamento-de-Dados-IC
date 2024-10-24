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

#create a new colunm for the gender of the names
name_location_table['genero'] = None

# associate the names to the gender
for line in range(0, len(name_location_table)):
    name = name_location_table['nome_x'][line]
    genero = Genero(name)
    name_location_table.loc[line, 'genero'] = genero()

name_location_table.to_csv('nomes_locais.csv', sep=',', index=False)

