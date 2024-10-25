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


print(topvendas[["Nome do Produto","Total"]])


# print(q1)
# print(q2)
# print(q3)


