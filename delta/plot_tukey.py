import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
# titulo = 'portfolios-'
# ax.set_title(titulo)
ax.set_xlabel('Delta')
ax.set_ylabel('Cardinalidade')
# ax.set_yticks([3, 9, 15])

# media5 =  0.00023693699622553328
# desvio5 =  6.214176979728275e-05
# media3 =  9.389232349464667e-05
# desvio3 =  4.479112597948399e-06
# media9 =  0.00012741713937333997
# desvio9 =  1.74297224737753e-05



# c = [3,9,15]
# m = [media3, media9, media5]

# x1, y1 = [media3 - desvio3, media3 + desvio3], [3, 3]
# x2, y2 = [media9 - desvio9, media9 + desvio9], [9, 9]
# x3, y3 = [media5 - desvio5, media5 + desvio5], [15, 15]

ax.set_yticks([1,2,3,4])
ax.set_yticklabels(['BRKGA', 'BRKNSGA', 'NSGA-M', 'NSGA-L'])

mediabrknsga =  0.0002786103289414
desviobrknsga =  5.208703732707201e-05
mediabrkga =  0.0007587211974290665
desviobrkga =  0.00017135123804833637
mediansgam =  4.992824609479332e-05
desvionsgam =  1.1105510862540179e-05
mediansgal =  0.00012741713937333997
desvionsgal =  1.74297224737753e-05


c = [1,2,3,4]
m = [mediabrkga, mediabrknsga, mediansgam, mediansgal]

x1, y1 = [mediabrkga - desviobrkga, mediabrkga + desviobrkga], [1, 1]
x2, y2 = [mediabrknsga - desviobrknsga, mediabrknsga + desviobrknsga], [2, 2]
x3, y3 = [mediansgam - desvionsgam, mediansgam + desvionsgam], [3, 3]
x4, y4 = [mediansgal - desvionsgal, mediansgal + desvionsgal], [4, 4]

ax.plot(x1, y1, '-', c = '#000000')
ax.plot(x2, y2, '-', c = '#000000')
ax.plot(x3, y3, '-', c = '#000000')
ax.plot(x4, y4, '-', c = '#000000')
ax.plot(m, c, 'x', c = '#757D75')
plt.savefig('test.png')
# plt.show()
