#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

lol
lol
lol
lol
lol
lol
lol

fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'test'
ax.set_xlabel('Risco')
ax.set_ylabel('Retorno')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

with open('p100') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#16a4f7', label = '100')

with open('p200') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#b3f716', label = '200')

with open('p300') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#f75916', label = '300')

with open('p400') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#f7ca16', label = '400')

with open('p500') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#f716ec', label = '500')

leg = ax.legend(loc = 4)


with open('p600') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#b013db', label = '600')

leg = ax.legend(loc = 4)


with open('p700') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#c12e66', label = '700')

leg = ax.legend(loc = 4)


with open('p800') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#13dbd7', label = '800')

leg = ax.legend(loc = 4)


with open('p900') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#c18b2e', label = '900')

leg = ax.legend(loc = 4)


with open('p1000') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#f4cf92', label = '1000')

leg = ax.legend(loc = 4)

# plt.show()
plt.savefig(titulo + '.png')
