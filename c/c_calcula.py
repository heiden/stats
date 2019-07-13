from c import c
from sys import argv
from os import listdir

k = argv[1]
# dir = '../fronteiras/res/' + str(k) + '/' # resultados
dir = './lul/'
arqs = listdir(dir)

m = [[0 for x in range(len(arqs))] for y in range(len(arqs))]
for i in range(len(arqs)):
	for j in range(len(arqs)):
		if i != j:
			res = c(dir + arqs[i], dir + arqs[j])
			print(i, j, res)
			m[i][j] = res

print(arqs)
for i in range(len(m)):
	td = ["%.5f" % v for v in m[i]]
	print(*td)