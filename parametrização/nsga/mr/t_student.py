#      -tt        0        +tt
# ------|---------|---------|------
# 
# se o seu p-valor estiver entre os tts, a diferenca nao eh significativa
# se nao, existe diferenca significativa e vc deve olhar as medias pra ver quem eh o melhor
# 
# t = valor tabelado, pegar o valor na posicao a = 0.05, df = |A| + |B| - 2



import numpy as np
from sys import argv
from math import sqrt

def calcula_razoes(arq):
	pontos = []
	with open(arq, 'r') as f:
		for line in f:
			pontos.append([float(i) for i in line.split()])

	return [retorno / risco for (risco, retorno) in pontos]

arq1 = argv[1]
arq2 = argv[2]

razoes1 = calcula_razoes(arq1)
razoes2 = calcula_razoes(arq2)

x1 = np.mean(razoes1)
x2 = np.mean(razoes2)

s1 = np.std(razoes1)
s2 = np.std(razoes2)

n1 = len(razoes1)
n2 = len(razoes2)

t = (x1 - x2) / (sqrt(s1**2/n1 + s2**2/n2))
print 'df:', n1 + n2 - 2
print 'p value:', t

if x1 > x2: print arq1 
else: print arq2