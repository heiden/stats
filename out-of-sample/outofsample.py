import pandas as pd
import matplotlib.pyplot as plt

def serie_ibovespa():
	arq = "./ibovespa.csv"
	data = pd.read_csv(arq)
	return data.Adj_Close.values
	
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

ibovespa = serie_ibovespa()
xticks = acha_ticks()
print(xticks)
capital = 1
pontos = []
for i in range(len(ibovespa) - 1):
	pontos.append((i, capital))
	capital += ((ibovespa[i+1] - ibovespa[i]) / ibovespa[i]) * 100

print(len(pontos))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('Tempo')
ax.set_ylabel('Retorno Acumulado (%)')
xlabels = ['Jan 2016', 'Jul 2016', 'Jan 2017', 'Jul 2017', 'Jan 2018', 'Jul 2018']
ax.set_xticklabels(xlabels)
ax.set_xticks(xticks)

x = [p[0] for p in pontos]
y = [p[1] for p in pontos]
ax.plot(x, y, '--', c = '#871c83', label = 'IBovespa')

leg = ax.legend()
plt.show()
# plt.savefig(titulo + '.png')
