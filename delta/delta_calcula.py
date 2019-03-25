from delta import delta
from os import listdir

origem = '../data/'
algs = ['brkga/', 'brknsga/', 'nsgal/', 'nsgam/']
k = ['3', '9', '15']

for a in algs:
	for i in k:
		dir = origem + a + '/' + i + '/'
		arqs = listdir(dir)
		delta_dir = []
		for arq in arqs:
			res = delta(dir + arq)
			delta_dir.append(res)
		saida = './resultados/' + a + i
		file = open('delta.csv', 'a')
		# file = open(saida, 'w')
		for d in delta_dir:
			file.write(str(d) + ',' + '"' + a[:-1] + '",' + i + '\n')
			# file.write(str(d) + '\n')
		file.close()