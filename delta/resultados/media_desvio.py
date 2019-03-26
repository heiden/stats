import numpy as np
from sys import argv

x = []
arq = argv[1]
with open(arq) as f:
	for line in f:
		x.append(float(line))

print('media{} = '.format(arq[0:len(arq)-2]), np.mean(x))
print('desvio{} = '.format(arq[0:len(arq)-2]), np.std(x))