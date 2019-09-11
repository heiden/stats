#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n = argv[1]
fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'portfolios-' + n
ax.set_xlabel('Risco')
ax.set_ylabel('Retorno')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

# with open('./res/' + n + '/res-brkga-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '^', c = '#000000', label = 'BRKGA')

# with open('./res/' + n + '/res-brknsga-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '.', c = '#ABB7B7', label = 'BRKNSGA')

# with open('./res/' + n + '/res-nsgam-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '*', c = '#6C7A89', label = 'NSGA-M')

# with open('./res/' + n + '/res-nsgal-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, 'x', c = '#757D75', label = 'NSGA-L')

with open('./res/{0}/res-brkga-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#f4e513', label = 'BRKGA')

with open('./res/{0}/res-nsgal-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#93f413', label = 'NSGA-L')

with open('./res/{0}/res-nsgam-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ba5584', label = 'NSGA-M')

with open('./res/{0}/res-brknsga-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#55a7ba', label = u'Híbrido')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '.png')
