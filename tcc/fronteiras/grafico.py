#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n = argv[1]
alg = argv[2]
fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'portfolios-' + alg + '-' + n
ax.set_xlabel('Risco')
ax.set_ylabel('Retorno')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

with open('../dados-sem-params/{0}-3'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ed17cd', label = u'3')

with open('../dados-com-params/{0}-3'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ff9114', label = u'3*')

with open('../dados-sem-params/{0}-9'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#dbca0d', label = u'9')

with open('../dados-com-params/{0}-9'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#34d8c5', label = u'9*')

with open('../dados-sem-params/{0}-15'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#ca0ddb', label = u'15')

with open('../dados-com-params/{0}-15'.format(alg)) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#1edb0d', label = u'15*')

# with open('hibrido-{0}''.format(n)') as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, 'x', c = '#1fc6be', label = u'Híbrido')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '-versus.png')
