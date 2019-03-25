# The F value is the point such that the area of the curve
# past that point to the tail is just the p-value. Therefore:
# PR(>F) = p-value

import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('./hipervolume.csv')

# print(data)
data.boxplot('Hipervolume', by = 'Algoritmo')
plt.savefig('hipervolume_por_algoritmo.png')

data.boxplot('Hipervolume', by = 'Cardinalidade')
plt.savefig('hipervolume_por_cardinalidade.png')

# ANOVA
formula = 'Hipervolume ~ C(Algoritmo) + C(Cardinalidade) + C(Algoritmo):C(Cardinalidade)'
# formula = 'Hipervolume ~ Algoritmo + Cardinalidade + Algoritmo:Cardinalidade'
model = ols(formula, data).fit()
aov_table = statsmodels.stats.anova.anova_lm(model, typ = 2)
print(aov_table)

#                                  	sum_sq       df           F        p-valor
# Algoritmo                  		0.000654    3.0   14.012397   1.208370e-08
# Cardinalidade             		0.015055    2.0  484.013436  3.038930e-101
# Interacao  						0.000342    6.0    3.660914   1.540434e-03
# Erro                       		0.005412  348.0

# Resultado significante tanto para cardinalidade quanto para algoritmo, com nivel de confianca p < 0.05.
