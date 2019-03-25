import numpy as np
from sys import argv

x = []
arq = argv[1]
with open(arq) as f:
	for line in f:
		x.append(float(line))

print('media: ', np.mean(x))
print('desvio: ', np.std(x))