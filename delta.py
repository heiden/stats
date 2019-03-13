from sys  import argv
from math import sqrt, fabs

def dist(p, q):
	return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)

file = argv[1]
pontos = []
with open(file) as f:
	for line in f:
		pontos.append([float(i) for i in line.split()])

qnt = len(pontos)
pontos.sort()
di = []
for i in range(qnt - 1):
	di.append(dist(pontos[i], pontos[i+1]))

delta = 0
db = sum(di)
for i in range(qnt - 1):
	delta += fabs(di[i] - db) / qnt

print('delta:', delta)
# for a in p:
# 	print(a)