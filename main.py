import pandas as pd

# Load the data
data_names = pd.read_csv('br_ibge_nomes_brasil.csv')

data_locals = pd.read_csv('br_bd_diretorios_brasil_municipio.csv')

# Print the first 10 names
for line in range(0, 10):
    print(data_names['nome'][line])
    print(data_locals['nome'][line])
