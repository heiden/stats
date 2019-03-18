from hv import hv

dir = './data/'
k = ['3', '9', '15']
arqs = ['res-brkga-', 'res-brkga-nsga-', 'res-nsga-literatura-', 'res-meu-nsga-', 'res-meu-nsga-adap-']

for a in arqs:
	res = []
	for i in k:
		arq = dir + a + i
		res.append(hv(arq))
	td = ["%.5f" % v for v in res]
	print(*td)