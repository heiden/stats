# cardinalidade: 3 tratamentos -> 3.31 
# algoritmo: 	 4 tratamentos -> 3.63

# The difference between the two means is designated as significant if its
# test statistic q is LARGER than the critical q value from the table.

from math import sqrt, fabs

origem = './resultados/'
algs = ['brkga', 'brknsga', 'nsgal', 'nsgam']
k = ['3', '9', '15']

q = 3.31 # cardinalidade
se = sqrt(3.160920e-08 / 30.0)
hsd = q * se

# cardinalidade
for i in k:
	print(i, '============')
	tukey, medias = [], []
	for a in algs:
		arq = origem + a  + '/' + i
		d = []
		with open(arq) as f:
			for line in f:
				d.append(float(line))
		medias.append(sum(d) / len(d))
	# print(medias)
	for x in range(len(medias)):
		for y in range(x+1, len(medias)):
			if fabs(medias[x] - medias[y]) > hsd:
				print(algs[x], algs[y], 'significante')
			else:
				print(algs[x], algs[y], 'insignificante')

# algoritmo
q = 3.63 # algoritmo
se = sqrt(3.160920e-08 / 30.0)
hsd = q * se
for a in algs:
	print(a, '============')
	tukey, medias = [], []
	for i in k:
		arq = origem + a  + '/' + i
		d = []
		with open(arq) as f:
			for line in f:
				d.append(float(line))
		medias.append(sum(d) / len(d))
	# print(medias)
	for x in range(len(medias)):
		for y in range(x+1, len(medias)):
			if fabs(medias[x] - medias[y]) > hsd:
				print(k[x], k[y], 'significante')
			else:
				print(k[x], k[y], 'insignificante')