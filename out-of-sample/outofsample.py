#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from sys import argv

def serie_ibovespa():
	arq = "./ibovespa.csv"
	data = pd.read_csv(arq)
	return data.Adj_Close.values

def serie_cdi():
	arq = "./cdi.csv"
	data = pd.read_csv(arq)
	return data.Adj_Close.values

def serie_ativo(n):
	dir = './ativos/'
	arqs = listdir(dir)
	arq = arqs[n-1]
	data = pd.read_csv(dir + arq)
	return data['Adj Close'].values

def acha_ticks():
	arq = "./ibovespa.csv"
	data = pd.read_csv(arq)
	dias = list(data.Date.values)
	cunt = 0
	ticks = []
	for d in dias:
		ano, mes, dia = map(int, d.split('-'))
		if (mes == 1 or mes == 7) and (dia > 11 and dia < 18):
			ticks.append(cunt)
			dias.pop(cunt)
			dias.pop(cunt)
			dias.pop(cunt)
			dias.pop(cunt)
		cunt += 1
	return ticks

def gera_series(ativos):
	return [serie_ativo(i) for i in ativos]

def gera_pontos(series, lotes):
	val = lotes
	pontos = []
	for i in range(len(series[0]) - 1):
		pontos.append((i, (sum(val) - 1) * 100))
		for j in range(len(series)):
			val[j] += lotes[j] * ((series[j][i+1] - series[j][i]) / series[j][i])
	return pontos

def gera_medias(pontos):
	medias = []
	for i in range(len(pontos[0])):
		tam = len(pontos)
		p = [0, 0]
		for j in range(tam):
			# print(i, j)
			p[0] += pontos[j][i][0]
			p[1] += pontos[j][i][1]
		p[0] /= tam
		p[1] /= tam
		medias.append(p)
	return medias

def plot_media(ativos, lotes, alg, cor):
	tam = len(ativos)
	series = [gera_series(ativos[i]) for i in range(tam)]
	pontos = [gera_pontos(series[i], lotes[i]) for i in range(tam)]
	pontos_grafico = gera_medias(pontos)

	ax = fig.add_subplot(111)
	x = [p[0] for p in pontos_grafico]
	y = [p[1] for p in pontos_grafico]
	ax.plot(x, y, '--', c = cor, label = alg)

def plot_maior(ativos, lotes, alg, cor, style):
	# se quiser descobrir qual o maior
	tam = len(ativos)
	series = [gera_series(ativos[i]) for i in range(tam)]
	pontos = [gera_pontos(series[i], lotes[i]) for i in range(tam)]
	retornos = []
	for i in range(len(pontos)):
		r = 0
		for j in range(len(pontos[i])):
			r += pontos[i][j][1]
		# retornos.append(r)
		retornos.append((r, i))
	
	idx = retornos.index(max(retornos))

	retornos.sort()
	idx = retornos[-1][1]
	print(idx)
	series = gera_series(ativos[idx])

	pontos_grafico = gera_pontos(series, lotes[0])

	ax = fig.add_subplot(111)
	x = [p[0] for p in pontos_grafico]
	y = [p[1] for p in pontos_grafico]
	ax.plot(x, y, style, c = cor, label = alg)

def plot_portfolio(ativos, lotes):
	retorno_total = 0
	todos_os_pontos = []
	for i in range(len(ativos)):
		retorno_ativo = 0
		pontos_por_ativo = []
		serie = serie_ativo(ativos[i])
		for j in range(len(serie) - 1):
			retorno_ativo += (serie[j+1] - serie[j]) / serie[j]
			pontos_por_ativo.append(retorno_ativo * lotes[i])
		retorno_total += retorno_ativo * lotes[i]
		todos_os_pontos.append(pontos_por_ativo)

	return np.sum(todos_os_pontos, axis = 0)

def le_dados(alg, k):
	portfolios = []
	arq = 'portfolios-nsga-busca-local/' + alg + '/' + 'portfolios' + k
	with open(arq, 'r') as f:
		for i in range(30):
			ativos = map(int, f.readline().split())
			lotes  = map(float, f.readline().split())
			f.readline()
			portfolios.append((ativos, lotes))


	return portfolios



xticks = acha_ticks()
print(xticks)
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
ax.set_xlabel('Tempo')
ax.set_ylabel('Retorno Acumulado (%)')
xlabels = ['Jan 2016', 'Jul 2016', 'Jan 2017', 'Jul 2017', 'Jan 2018', 'Jul 2018']
ax.set_xticklabels(xlabels)
ax.set_xticks(xticks)

ibovespa = serie_ibovespa()
ib = 1
pontos_ib = []
for i in range(len(ibovespa) - 1):
	pontos_ib.append((i, (ib - 1) * 100))
	ib += ib * ((ibovespa[i+1] - ibovespa[i]) / ibovespa[i])

x = [p[0] for p in pontos_ib]
y = [p[1] for p in pontos_ib]
ax.plot(x, y, '--', c = '#871c83', label = 'Ibovespa')

cdi = serie_cdi()
c = 1
pontos_cdi = []
for i in range(len(cdi) - 1):
	pontos_cdi.append((i, (c-1)*100))
	c *= cdi[i]

x = [p[0] for p in pontos_cdi]
y = [p[1] for p in pontos_cdi]
ax.plot(x, y, '--', c = '#4fd15c', label = 'CDI')

# alg = argv[1]
# k = argv[2]
# portfolios = le_dados(alg, k)
# linestyles = ['-', '--', '-.', ':']
# colours = ['#70cc3c', '#5db690', '#9c3266', '#34ce19', '#472859', '#1f7332', '#9750e2', '#355074', '#7e7b93', '#8ab567',
# 		   '#7be104', '#4efd1f', '#3e11d0', '#8561b3', '#f2081e', '#347296', '#aba14b', '#f999c8', '#1e1cf5', '#ee83de',
# 		   '#2b2bc6', '#ba532c', '#b01c26', '#5d738d', '#be3aee', '#1e18df', '#2e94dc', '#f48fac', '#ad742d', '#e86fca']

portfolios = [
	([9, 55, 24], [0.34, 0.34000003, 0.32000002]),
	([24, 48, 9], [0.365938, 0.215991, 0.418072]),
	([24, 31, 9], [0.33695894, 0.26304108, 0.4])
]

labels = ['BRKGA', 'NSGA-II + BL', u'Híbrido']
colours = ['#054bfc', '#ff6a00', '#fc83ad']
linestyles = ['--']

# portfolios = [([24, 48, 9], [0.365938, 0.215991, 0.418072])]

i = 0
for p in portfolios:
	if i == 28:		print(p)
	pontos = plot_portfolio(p[0], p[1])
	pontos = [pontos[x] * 100 for x in range(len(pontos))]
	ax.plot(list(range(len(pontos))), pontos, linestyles[0], c = colours[i], label = labels[i])
	i += 1

# ativos, lotes = [], []
# for p in portfolios:
# 	ativos.append(p[0])
# 	lotes.append(p[1])
# plot_maior(ativos, lotes, "brkga", colours[1], '--')


###

leg = ax.legend(loc = 4)
# plt.show()
plt.savefig('test.png')
# plt.savefig(alg + '-' + k + '.png')
