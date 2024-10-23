
import os 
os.system('cls')

import numpy as np


salario = [2000, 2500, 3000, 3500, 4000, 30000]

media = np.mean(salario)

print('Média: ', media)


mediana = np.median(salario)

print('Mediana: ', mediana)