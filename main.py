import numpy as np
import pandas as pd
from gender_guesser_br import Genero

# Load the data
data_names = pd.read_csv('br_ibge_nomes_brasil.csv')

data_locals = pd.read_csv('br_bd_diretorios_brasil_municipio.csv')

#criar tabela que relaciona os nomes com os locais
main_df = pd.merge(data_names, data_locals, on='id_municipio')

print(main_df.loc[20, 'nome_x'])
print(main_df.loc[20, 'nome_y'])
print(main_df.loc[20, 'nome_uf'])
print(main_df.loc[20, 'nome_regiao'])
print(main_df.loc[20, 'quantidade_nascimentos_ate_2010'])

# Print the first 10 names
#for line in range(0, 10):
    # nome = data_names['nome'][line]
    # genero = Genero(nome)
    # print(nome, genero())
    # print(data_locals['nome'][line])'


