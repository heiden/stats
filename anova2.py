# The F value is the point such that the area of the curve
# past that point to the tail is just the p-value. Therefore:
# PR(>F) = p-value

# https://www.socscistatistics.com/tests/anova/Default2.aspx // ANOVA
# https://www.socscistatistics.com/pvalues/fdistribution.aspx // converter F-value em p-value
# p-value eh a area embaixo da curva F a partir do F-value obtido pelo ANOVA

# ANOVA 2 FATORES:
# http://vassarstats.net/anova2u.html


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./anova.csv')

# separando por cardinalidade
c3  = data.loc[data.cardinalidade ==  3].hipervolume.values
c9  = data.loc[data.cardinalidade ==  9].hipervolume.values
c15 = data.loc[data.cardinalidade == 15].hipervolume.values
n_grupos = 3

# dados de teste, ignorar
# c3  = [2, 3, 7, 2, 6]
# c9  = [10, 8, 7, 5, 10]
# c15 = [10, 13, 14, 13, 15]
# n_grupos = 3

# soma de quadrados NOS grupos
media_c3  = sum(c3)  / len(c3)
media_c9  = sum(c9)  / len(c9)
media_c15 = sum(c15) / len(c15)

ss_c3  = sum([(x - media_c3)  ** 2 for x in  c3])
ss_c9  = sum([(x - media_c9)  ** 2 for x in  c9])
ss_c15 = sum([(x - media_c15) ** 2 for x in c15])
ss_dos_grupos = ss_c3 + ss_c9 + ss_c15

# soma de quadrados da amostra
amostra = list(c3) + list(c9) + list(c15)
media_total = sum(amostra) / len(amostra)
ss_total = sum([(x - media_total)  ** 2 for x in amostra])

# soma de quadrados ENTRE grupos
ss_entre_grupos = ((media_c3 - media_total) ** 2 + (media_c9 - media_total) ** 2 + (media_c15 - media_total) ** 2) * len(c3)

# ss_total = ss_dos_grupos + ss_entre_grupos

df_numerador = n_grupos - 1
numerador = ss_entre_grupos / df_numerador

df_denominador = len(amostra) - n_grupos
denominador = ss_dos_grupos / df_denominador

print('total:', ss_total)
print('coluna: ss:', ss_dos_grupos, 'ms:', (ss_dos_grupos / df_denominador))
print('linha:  ss:', ss_entre_grupos, 'ms:', (ss_entre_grupos / df_numerador))

F = numerador / denominador
print('F(', df_numerador, ',', df_denominador, ') =', F)
print('converte F pro p-valor usando o site ;)')


# separando por algoritmo
a1 = data.loc[data.algoritmo == 'BRKGA'    ].hipervolume.values
a2 = data.loc[data.algoritmo == 'BRKNSGA'  ].hipervolume.values
a3 = data.loc[data.algoritmo == 'NSGA-L'   ].hipervolume.values
a4 = data.loc[data.algoritmo == 'NSGA-M'   ].hipervolume.values
a5 = data.loc[data.algoritmo == 'NSGA-M-AD'].hipervolume.values
n_grupos = 5

# soma de quadrados NOS grupos
media_a1 = sum(a1) / len(a1)
media_a2 = sum(a2) / len(a2)
media_a3 = sum(a3) / len(a3)
media_a4 = sum(a4) / len(a4)
media_a5 = sum(a5) / len(a5)

ss_a1  = sum([(x - media_a1)  ** 2 for x in a1])
ss_a2  = sum([(x - media_a2)  ** 2 for x in a2])
ss_a3  = sum([(x - media_a3)  ** 2 for x in a3])
ss_a4  = sum([(x - media_a4)  ** 2 for x in a4])
ss_a5  = sum([(x - media_a5)  ** 2 for x in a5])
ss_dos_grupos = ss_a1 + ss_a2 + ss_a3 + ss_a4 + ss_a5

# soma de quadrados da amostra
amostra = list(a1) + list(a2) + list(a3) + list(a4) + list(a5)
media_total = sum(amostra) / len(amostra)
ss_total = sum([(x - media_total)  ** 2 for x in amostra])

# soma de quadrados ENTRE grupos
ss_entre_grupos = ((media_a1 - media_total) ** 2 + (media_a2 - media_total) ** 2 + (media_a3 - media_total) ** 2 + (media_a4 - media_total) ** 2 + (media_a5 - media_total) ** 2) * len(c3)

# ss_total = ss_dos_grupos + ss_entre_grupos

df_numerador = n_grupos - 1
numerador = ss_entre_grupos / df_numerador

df_denominador = len(amostra) - n_grupos
denominador = ss_dos_grupos / df_denominador

print('total:', ss_total)
print('coluna: ss:', ss_dos_grupos, 'ms:', (ss_dos_grupos / df_denominador))
print('linha:  ss:', ss_entre_grupos, 'ms:', (ss_entre_grupos / df_numerador))

F = numerador / denominador
print('F(', df_numerador, ',', df_denominador, ') =', F)
print('converte F pro p-valor usando o site ;)')