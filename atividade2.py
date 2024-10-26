import os 
os.system('cls')

import pandas as pd
import numpy as np

df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')

quantidade_vendida = df['Total']
mediana = np.median(quantidade_vendida)
media = np.mean(quantidade_vendida)

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)  
q3 = np.quantile(quantidade_vendida, 0.75)

topvendas = df[df['Total']> q3].sort_values(by='Total',ascending=True)
vendas = df[df['Total']< q3].sort_values(by='Total',ascending=True)

print(30* '=')

print("Valores Médios:")
print("Resultado do valor médio:", media, "peço usa a linha do relatório abaixo como padrão em relação a valores médios.")
print("Resultado do valor mediano das venda:", mediana,)

print(30* '=')

print("Percentuais das Vendas:")
print("Valor correspondente a (25%) do total das vendas:", q1,)
print("Valor correspondente a (50%) do total das vendas:", q2,)
print("Valor correspondente a (75%) do total das vendas:", q3,)

print(30* '=')

print("Top Produtos Vendidos")
print(topvendas[["Nome do Produto","Vendas (unidades)","Total"]])

print(30* '=')

# print(vendas[["Nome do Produto","Total"]])

