import pandas as pd
import matplotlib.pyplot as plt
from os import listdir

def serie_ibovespa():
	arq = "./ibovespa.csv"
	data = pd.read_csv(arq)
	return data.Adj_Close.values

def serie_ativo(n):
	dir = './ativos/'
	arqs = listdir(dir)
	arq = arqs[n]
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
	return [serie_ativo(i-1) for i in ativos]

def gera_pontos(series, lotes):
	val = 1
	pontos = []
	for i in range(len(series[0]) - 1):
		pontos.append((i, val))
		for j in range(len(series)):
			val += lotes[j] * ((series[j][i+1] - series[j][i]) / series[j][i]) * 100
	return pontos


ibovespa = serie_ibovespa()
xticks = acha_ticks()
print(xticks)
ib = 1
pontos_ib = []
for i in range(len(ibovespa) - 1):
	pontos_ib.append((i, ib))
	ib += ((ibovespa[i+1] - ibovespa[i]) / ibovespa[i]) * 100

fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111)
ax.set_xlabel('Tempo')
ax.set_ylabel('Retorno Acumulado (%)')
xlabels = ['Jan 2016', 'Jul 2016', 'Jan 2017', 'Jul 2017', 'Jan 2018', 'Jul 2018']
ax.set_xticklabels(xlabels)
ax.set_xticks(xticks)

x = [p[0] for p in pontos_ib]
y = [p[1] for p in pontos_ib]
ax.plot(x, y, '--', c = '#871c83', label = 'IBovespa')

###

# series = []
# for i in ativos:
# 	series.append(serie_ativo(i-1))

ativos_nsgam = [7, 35, 44]
lotes_nsgam = [0.30, 0.20, 0.50]
series = gera_series(ativos_nsgam)
pontos_nsgam = gera_pontos(series, lotes_nsgam)

ax = fig.add_subplot(111)
x = [p[0] for p in pontos_nsgam]
y = [p[1] for p in pontos_nsgam]
ax.plot(x, y, '--', c = '#abc321', label = 'NSGA-M')

ativos_nsgal = [1, 2, 3]
lotes_nsgal = [0.30, 0.20, 0.50]
series = gera_series(ativos_nsgal)
pontos_nsgal = gera_pontos(series, lotes_nsgal)

ax = fig.add_subplot(111)
x = [p[0] for p in pontos_nsgal]
y = [p[1] for p in pontos_nsgal]
ax.plot(x, y, '--', c = '#fec555', label = 'NSGA-L')

ativos_brknsga = [10, 11, 41]
lotes_brknsga = [0.30, 0.20, 0.50]
series = gera_series(ativos_brknsga)
pontos_brknsga = gera_pontos(series, lotes_brknsga)

ax = fig.add_subplot(111)
x = [p[0] for p in pontos_brknsga]
y = [p[1] for p in pontos_brknsga]
ax.plot(x, y, '--', c = '#666666', label = 'BRKNSGA')

ativos_brkga = [54, 12, 60]
lotes_brkga = [0.30, 0.20, 0.50]
series = gera_series(ativos_brkga)
pontos_brkga = gera_pontos(series, lotes_brkga)

ax = fig.add_subplot(111)
x = [p[0] for p in pontos_brkga]
y = [p[1] for p in pontos_brkga]
ax.plot(x, y, '--', c = '#babaca', label = 'BRKGA')

###

leg = ax.legend()
# plt.show()
plt.savefig('sample.png')
