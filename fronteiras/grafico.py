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

# with open('./res/' + n + '/res-brkga-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '^', c = '#000000', label = 'BRKGA')

# with open('./res/' + n + '/res-brknsga-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '.', c = '#ABB7B7', label = 'BRKNSGA')

# with open('./res/' + n + '/res-nsgam-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, '*', c = '#6C7A89', label = 'NSGA-M')

# with open('./res/' + n + '/res-nsgal-' + n) as arq:
# 	linhas = arq.readlines()
# 	x = [float(linha.split()[0]) for linha in linhas]
# 	y = [float(linha.split()[1]) for linha in linhas]

# ax.plot(x, y, 'x', c = '#757D75', label = 'NSGA-L')

with open('./res/3/res-' + n + '-3') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, '.', c = '#ABB7B7', label = '3')

with open('./res/9/res-' + n + '-9') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, '^', c = '#000000', label = '9')

with open('./res/15/res-' + n + '-15') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#757D75', label = '15')

leg = ax.legend()

# plt.show()
plt.savefig(titulo + '.png')
