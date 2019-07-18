import seaborn
import pandas as pd
from sys import argv
import matplotlib.pyplot as plt

path = './'
file = argv[1]
# nomes = ['BRKGA', 'BRKNSGA', 'NSGA-M', 'NSGA-L']
nomes = ['100', '200', '300', '400', '500']
dataset = pd.read_csv(path + file, names = nomes)
print(dataset.values)

# x = dataset.corr()
plt.subplots(figsize = (10, 10))
seaborn.heatmap(dataset, cmap = 'coolwarm', annot = True, yticklabels = nomes, fmt = '.5f')
plt.savefig(file[:-4] + '.png')