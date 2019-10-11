#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

alg = argv[1]
fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'portfolios-' + alg
ax.set_xlabel('Risco')
ax.set_ylabel('Retorno')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

with open('{0}-3'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ed17cd', label = u'3-BL')

with open('{0}-3-params'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ff9114', label = u'3*')

with open('{0}-9'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#dbca0d', label = u'9-BL')

with open('{0}-9-params'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#34d8c5', label = u'9*')

with open('{0}-15'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ca0ddb', label = u'15-BL')

with open('{0}-15-params'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#1edb0d', label = u'15*')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '-versus.png')
