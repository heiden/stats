from sys import argv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n = argv[1]
fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'portfolios-' + n
# ax.set_title(titulo)
ax.set_xlabel('Risco')
ax.set_ylabel('Retorno')
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))

with open('./res/res-brkga-' + n) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, '^', c = '#000000', label = 'BRKGA')

with open('./res/res-brknsga-' + n) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, '.', c = '#ABB7B7', label = 'BRKNSGA')

with open('./res/res-nsgam-' + n) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, '*', c = '#6C7A89', label = 'NSGA-M')

with open('./res/res-nsgal-' + n) as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#757D75', label = 'NSGA-L')

leg = ax.legend()

# plt.show()
plt.savefig(titulo + '.png')
