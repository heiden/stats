# di - distancia euclidiana entre duas solucoes consecutivas nao dominadas
# db - media de todas as distancias // sum(i=1:n) di/n 
# df - distancia entre os pontos extremos do conjunto nao dominado
# dl - distancia entre os pontos extremos do espaco de busca
# n  - numero de solucoes nao dominadas

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

df = dist(pontos[0], pontos[-1])
db = sum(di) / len(di)

soma = 0
for i in range(qnt - 1):
	soma += fabs(di[i] - db)

delta = (df + soma) / (df + (qnt-1)*db)

print('df:', df)
print('delta:', delta)
# for a in p:
# 	print(a)