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

with open('nsga-3') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ed17cd', label = '3 locl')

with open('nsga-9') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#000000', label = '9 locl')

with open('nsga-15') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ff9114', label = '15 loc')

with open('nsga-9-normal'.format(n)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#34d8c5', label = u'9 normal')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '.png')
