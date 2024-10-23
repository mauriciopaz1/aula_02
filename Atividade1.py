import os 
os.system('cls')

import numpy as np

vendas = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000, ]

media = np.mean(vendas)

print('Valor médio das casas R$', media, 'o que pode representar uma distoção do valor real das vendas.')


mediana = np.median(vendas)

print('Valor mediano das casas R$', mediana, 'o que representa um valor mais representativo em relação aos valores praticados.')





