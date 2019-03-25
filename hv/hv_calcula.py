from hv import hv
from os import listdir

origem = '../data/'
algs = ['brkga/', 'brknsga/', 'nsgal/', 'nsgam/']
k = ['3', '9', '15']

for a in algs:
	for i in k:
		dir = origem + a + '/' + i + '/'
		arqs = listdir(dir)
		hv_dir = []
		for arq in arqs:
			res = hv(dir + arq)
			hv_dir.append(res)
		saida = './resultados/' + a + i
		file = open(saida, 'w')
		# file = open('lol.csv', 'a')
		for h in hv_dir:
			file.write(str(h) + ',' + '"' + a[:-1] + '",' + i + '\n')
		file.close()