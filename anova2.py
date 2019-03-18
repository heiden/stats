# The F value is the point such that the area of the curve
# past that point to the tail is just the p-value. Therefore:
# PR(>F) = p-value

import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

data = pd.read_csv('./anova.csv')

# separando por cardinalidade
x = data.loc[data.cardinalidade == 3].hipervolume.values
print(x)
