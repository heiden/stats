import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
# titulo = 'portfolios-'
# ax.set_title(titulo)
ax.set_xlabel('Delta')
ax.set_ylabel('Cardinalidade')
ax.set_yticks([3, 9, 15])

# 3: 
media3 = 0.0001841
std3 =  0.0002394
# 9:  
media9 =  0.0003037
std9 = 0.0002909
# 15: 
media15 =  0.0004134
std15 =  0.0003841

c = [3,9,15]
hv = [0.0001841, 0.0003037, 0.0004134]

x1, y1 = [media3 - std3, media3 + std3], [3, 3]
x2, y2 = [media9 - std9, media9 + std9], [9, 9]
x3, y3 = [media15 - std15, media15 + std15], [15, 15]
ax.plot(x1, y1, '-', c = '#000000')
ax.plot(x2, y2, '-', c = '#000000')
ax.plot(x3, y3, '-', c = '#000000')
ax.plot(hv, c, 'x', c = '#757D75')
plt.show()
