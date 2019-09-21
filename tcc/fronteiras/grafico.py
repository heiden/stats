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

ax.plot(x, y, 'x', c = '#000000', label = 'BRKGA')

with open('nsga-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#93f413', label = 'NSGA')

with open('hibrido-{0}'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#55a7ba', label = u'Híbrido')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '.png')
