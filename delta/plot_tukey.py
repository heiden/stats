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
m = [0.00047612609126731456, 0.00019155621480413353, 0.0006676823060714481]

x1, y1 = [0.0002329472571504425, 0.0007193049253841866], [3, 3]
x2, y2 = [-2.2345922677263535e-05, 4.161148480295022e-05], [9, 9]
x3, y3 = [-0.0002004153405818023, 0.0003498997351321556], [15, 15]
ax.plot(x1, y1, '-', c = '#000000')
ax.plot(x2, y2, '-', c = '#000000')
ax.plot(x3, y3, '-', c = '#000000')
ax.plot(m, c, 'x', c = '#757D75')
plt.show()
