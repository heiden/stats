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

data = pd.read_csv('./delta.csv')

# print(data)
data.boxplot('Delta', by = 'Algoritmo', figsize = (12, 8), fontsize = 18, grid = False)
plt.suptitle('')
plt.savefig('delta_por_algoritmo.png')

data.boxplot('Delta', by = 'Cardinalidade', figsize = (12, 8), fontsize = 18, grid = False)
plt.suptitle('')
plt.savefig('delta_por_cardinalidade.png')

# ANOVA
formula = 'Delta ~ C(Algoritmo) + C(Cardinalidade) + C(Algoritmo):C(Cardinalidade)'
# formula = 'Delta ~ Algoritmo + Cardinalidade + Algoritmo:Cardinalidade'
model = ols(formula, data).fit()
aov_table = statsmodels.stats.anova.anova_lm(model, typ = 2)
print(aov_table)

# TCC
#                                          SS     	 df      		  MS	    	F        p-valor
# C(Algoritmo)                   1.432380e-06    	2.0  	7.161900e-07	58.097326  	1.348295e-21
# C(Cardinalidade)               2.430169e-06    	2.0  	1.215084e-06	98.567628  	1.293917e-32
# C(Algoritmo):C(Cardinalidade)  9.636850e-07    	4.0  	2.409212e-07	19.543530  	4.404311e-14
# Residual                       3.217456e-06  	  261.0  	1.232742e-08		  NaN	         NaN

# IC
#                                   	SS     df  			MS         			 F       p-valor
# Algoritmo                 	  0.000019    3.0  		6.33e-06		200.972122  1.298555e-75
# Cardinalidade               	  0.000003    2.0   	1.50e-06		50.828452   4.299798e-20
# Interacao					 	  0.000005    6.0   	8.33e-07		26.454463   6.227172e-26
# Erro                       	  0.000011  348.0		3.160920e-08

# MS = SS/df, pra cada linha
# Resultado significante tanto para cardinalidade quanto para algoritmo, com nivel de confianca p < 0.05.
