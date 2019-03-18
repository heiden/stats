import matplotlib.pyplot as plt

pts = [[3, 0.17414], [9, 0.03147], [15, 0.00205],
      [3, 0.44928], [9, 0.05726], [15, 0.00446],
	  [3, 0.14127], [9, 0.00374], [15, 0.00136],
	  [3, 0.48377], [9, 0.00715], [15, 0.00237],
	  [3, 0.44405], [9, 0.01558], [15, 0.00882]]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('dados')
ax.set_xlabel('cardinalidade')
ax.set_ylabel('hipervolume')
for p in pts:
	ax.plot(p[0], p[1], marker = 'x', c = 'b')
plt.show()