import os 
os.system('cls')
import pandas as pd
import numpy as np

df = pd.read_excel('vendas_roupas1.xlsx')

categoria = df['Categoria']
quantidade_vendida = df['Quantidade Vendida']

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

quantidadevdd_organizada = df.sort_values(by='Quantidade Vendida', ascending=True)
quantidade_vendida = quantidadevdd_organizada['Quantidade Vendida']


print(categoria.unique())
print(quantidade_vendida.unique())

print(f'1º Quartil: {q1}')
print(f'2º Quartil: {q2}')
print(f'3º Quartil: {q3}')

print(f'Média: {media}')
print(f'Mediana: {mediana}')

print(quantidade_vendida.values)


