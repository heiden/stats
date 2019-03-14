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

# nomes = ['claims', 'payment']
data = pd.read_csv('./anova.csv')

print(data)
# data.boxplot('delta', by = 'card')
# plt.show()

# formula = 'delta ~ C(alg) + C(card) + C(alg):C(card)'
# model = ols(formula, data).fit()
# aov_table = statsmodels.stats.anova.anova_lm(model, typ=2)
# print(aov_table)