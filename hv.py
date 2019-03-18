from sys import argv
from math import fabs
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle

def hv(arq):

	r = [-1, 0]
	# s = [[1,1], [2,3], [4,8]]
	s = []
	with open(arq) as f:
		for line in f:
			s.append([float(i) for i in line.split()])

	s.sort()
	r[0] = s[-1][0] * 1.1

	hv = 0
	for p in s:
		hv += fabs(p[0] - r[0]) * fabs(p[1] - r[1])
	return hv

if __name__ == "__main__":
	dir = 'data/'
	arq = dir + argv[1]
	print(hv(arq))

# representacao grafica
# AVISO: plot eh pesado
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('hipervolume')
# ax.set_xlabel('risco')
# ax.set_ylabel('retorno')
# ax.plot(r[0], r[1], marker = 'x', c = 'r')
# for p in s:
# 	ax.plot(p[0], p[1], marker = 'x', c = 'b')
# 	ax.add_patch(Rectangle((p[0], 0), fabs(r[0] - p[0]), p[1], color = '#000000', alpha = 0.01))
# plt.show()