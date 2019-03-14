import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
titulo = 'portfolios'
ax.set_title(titulo)
ax.set_xlabel('risco')
ax.set_ylabel('retorno')

with open('res-nsga-literatura') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#bb4444', label = 'nsga literatura')

with open('res-brkga') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#fe12fe', label = 'brkga')

with open('res-brkga-nsga') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#5f5f5f', label = 'brkga+nsga')

with open('res-meu-nsga') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#fedcba', label = 'meu nsga')

with open('res-meu-nsga-adap') as arq:
	linhas = arq.readlines()
	x = [float(linha.split()[0]) for linha in linhas]
	y = [float(linha.split()[1]) for linha in linhas]

ax.plot(x, y, 'x', c = '#cbacbf', label = 'meu nsga adap')

leg = ax.legend()

# plt.show()
plt.savefig(titulo + '.png')