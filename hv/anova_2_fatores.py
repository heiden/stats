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

# data = data[data['Cardinalidade'] == 3]

data.boxplot('Hipervolume', by = 'Algoritmo', figsize = (12, 8), fontsize = 18, grid = False)
plt.suptitle('')
plt.savefig('hipervolume_por_algoritmo.png')

data.boxplot('Hipervolume', by = 'Cardinalidade', figsize = (12, 8), fontsize = 18, grid = False)
plt.suptitle('')
plt.savefig('hipervolume_por_cardinalidade.png')

# ANOVA
formula = 'Hipervolume ~ C(Algoritmo) + C(Cardinalidade) + C(Algoritmo):C(Cardinalidade)'
# formula = 'Hipervolume ~ Algoritmo + Cardinalidade + Algoritmo:Cardinalidade'
model = ols(formula, data).fit()
aov_table = statsmodels.stats.anova.anova_lm(model, typ = 2)
print(aov_table)

# TCC
#                                      	SS  		df      	MS    			F        p-valor
# Algoritmo                   		3.033633e-09    2.0  	1.516816e-09	21.801473  	1.755037e-09
# Cardinalidade               		1.329510e-08    2.0  	6.647550e-09	95.546383  	7.317957e-32
# Interacao  						6.679051e-09    4.0  	1.669763e-09	23.999793  	6.396302e-17
# Erro                       		1.815883e-08  261.0     6.957406e-11   	NaN         NaN


# IC
#                                  		  SS     	df			MS	        	F    	 p-valor
# Algoritmo                  		1.302472e-07    3.0		4.341573e-08	217.723477  1.690350e-79
# Cardinalidade             		1.374557e-07    2.0		6.872785e-08	344.660069  2.923880e-83
# Interacao  						4.007043e-08    6.0		6.678405e-09	33.491216   7.580074e-32
# Erro                       		6.939386e-08  348.0		1.994076e-10	NaN			NaN

# MS = SS/df, pra cada linha
# Resultado significante tanto para cardinalidade quanto para algoritmo, com nivel de confianca p < 0.05.
