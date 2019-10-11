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



ibovespa = serie_ibovespa()
xticks = acha_ticks()
print(xticks)
ib = 1
pontos_ib = []
for i in range(len(ibovespa) - 1):
	pontos_ib.append((i, (ib - 1) * 100))
	ib += ib * ((ibovespa[i+1] - ibovespa[i]) / ibovespa[i])

fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
ax.set_xlabel('Tempo')
ax.set_ylabel('Retorno Acumulado (%)')
xlabels = ['Jan 2016', 'Jul 2016', 'Jan 2017', 'Jul 2017', 'Jan 2018', 'Jul 2018']
ax.set_xticklabels(xlabels)
ax.set_xticks(xticks)

x = [p[0] for p in pontos_ib]
y = [p[1] for p in pontos_ib]
ax.plot(x, y, '--', c = '#871c83', label = 'Ibovespa')

alg = argv[1]
k = argv[2]
portfolios = le_dados(alg, k)
linestyles = ['-', '--', '-.', ':']
colours = ['#70cc3c', '#5db690', '#9c3266', '#34ce19', '#472859', '#1f7332', '#9750e2', '#355074', '#7e7b93', '#8ab567',
		   '#7be104', '#4efd1f', '#3e11d0', '#8561b3', '#f2081e', '#347296', '#aba14b', '#f999c8', '#1e1cf5', '#ee83de',
		   '#2b2bc6', '#ba532c', '#b01c26', '#5d738d', '#be3aee', '#1e18df', '#2e94dc', '#f48fac', '#ad742d', '#e86fca']

# portfolios = [
# 	([31, 1, 41, 37, 23, 24, 38, 27, 25, 32, 20, 55, 2, 51, 48], [0.06545527, 0.054544732, 0.099999994, 0.04000001, 0.04, 0.10000001, 0.098589286, 0.041410718, 0.055475764, 0.06452424, 0.043125726, 0.07687428, 0.025583567, 0.09441644, 0.1]),
# 	([25, 35, 31, 24, 22, 23, 2, 48, 55, 41, 1, 20, 38, 51, 37], [0.05383934, 0.06740228, 0.07110156, 0.07589981, 0.06739663, 0.07952139, 0.05713221, 0.06618086, 0.07736758, 0.07096436, 0.06756253, 0.06155283, 0.04956666, 0.07245968, 0.062052295]),
# 	([55, 31, 40, 22, 1, 23, 60, 41, 52, 48, 24, 2, 51, 38, 9], [0.032224122, 0.087775886, 0.043484632, 0.07651538, 0.066722095, 0.05327791, 0.023219017, 0.096780986, 0.04, 0.10000001, 0.09711848, 0.042881522, 0.099999994, 0.04000001, 0.1])
# ]

# labels = ['BRKGA', 'NSGA', u'Híbrido']
# colours = ['#ff6a00', '#44b595', '#b54464']
# linestyles = ['--']

portfolios = [([23, 51, 41, 35, 55, 38, 25, 24, 2, 31, 1, 48, 37, 9, 22], [0.08114889, 0.020129543, 0.023104463, 0.020019723, 0.099981174, 0.09997313, 0.09997858, 0.099983595, 0.020185346, 0.09998089, 0.020520631, 0.099994116, 0.020040454, 0.09926883, 0.09569064])]

i = 0
for p in portfolios:
	if i == 11:		print(p)
	pontos = plot_portfolio(p[0], p[1])
	pontos = [pontos[x] * 100 for x in range(len(pontos))]
	ax.plot(list(range(len(pontos))), pontos, linestyles[i%4], c = colours[i], label = str(i))
	i += 1

# ativos, lotes = [], []
# for p in portfolios:
# 	ativos.append(p[0])
# 	lotes.append(p[1])
# plot_maior(ativos, lotes, "brkga", colours[1], '--')


###

leg = ax.legend(loc = 3)
# plt.show()
plt.savefig('com-params-15.png')
# plt.savefig(alg + '-' + k + '.png')
