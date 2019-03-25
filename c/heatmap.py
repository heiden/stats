import seaborn
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt

path = './'
file = 'c' + argv[1] + '.csv'
nomes = ['BRKGA', 'BRKNSGA', 'NSGA-M', 'NSGA-L']
dataset = pd.read_csv(path + file, names = nomes)
print(dataset.values)

# x = dataset.corr()
plt.subplots(figsize = (10, 10))
seaborn.heatmap(dataset, cmap = 'coolwarm', annot = True, yticklabels = nomes, fmt = '.5f')
plt.savefig(file + '.png')