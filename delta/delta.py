# di - distancia euclidiana entre duas solucoes consecutivas nao dominadas
# db - media de todas as distancias // sum(i=1:n) di/n 
# n  - numero de solucoes nao dominadas

# Quanto menor é o valor da métrica delta, mais bem espalhadas as soluções 
# estão e, portanto, mais diversificadas elas são, sendo que o valor zero indica 
# que o espaçamento entre todas as soluções consecutivas é exatamente o mesmo.

from sys  import argv
from math import sqrt, fabs

def dist(p, q):
	return sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)

def delta(arq):
	pontos = []
	with open(arq) as f:
		for line in f:
			pontos.append([float(i) for i in line.split()])

	qnt = len(pontos)
	pontos.sort()
	di = []
	for i in range(qnt - 1):
		di.append(dist(pontos[i], pontos[i+1]))

	media_di = sum(di) / len(di)

	soma = 0
	for i in range(qnt - 1):
		soma += (fabs(di[i] - media_di)) / (qnt - 1)

	return soma

if __name__ == '__main__':
	arq = argv[1]
	print(delta(arq))