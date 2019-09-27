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

with open('brkga-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#c61f7b', label = u'BRKGA Original 3')

with open('sem-params/brkga-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#1fc6be', label = u'BRKGA Parametrizado 3')

with open('brkga-9'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#000000', label = u'BRKGA Original 9')

with open('sem-params/brkga-9'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#93f413', label = u'BRKGA Parametrizado 9')

with open('brkga-15'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#e0e04c', label = u'BRKGA Original 15')

with open('sem-params/brkga-15'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#e04c4c', label = u'BRKGA Parametrizado 15')

# with open('nsga-{0}'.format(n)) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, 'x', c = '#93f413', label = 'NSGA')

# with open('hibrido-{0}'.format(n)) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, 'x', c = '#1fc6be', label = u'Híbrido')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '.png')
