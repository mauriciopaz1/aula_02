import os 
os.system('cls')
import pandas as pd
import numpy as np

df = pd.read_excel('vendas_eletos_eletronicos2.xlsx')

quantidade_vendida = df['Total']
mediana = np.median(quantidade_vendida)

print(df)
