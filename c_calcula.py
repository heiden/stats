from c import c
from sys import argv

k = argv[1]
arqs = ['res-brkga-' + k, 'res-brkga-nsga-' + k, 'res-nsga-literatura-' + k, 'res-meu-nsga-' + k, 'res-meu-nsga-adap-' + k]

m = [[0 for x in range(len(arqs))] for y in range(len(arqs))]
for i in range(len(arqs)):
	for j in range(len(arqs)):
		if i != j:
			res = c(arqs[i], arqs[j])
			print(i, j, res)
			m[i][j] = res

for i in range(len(m)):
	td = ["%.5f" % v for v in m[i]]
	print(*td)