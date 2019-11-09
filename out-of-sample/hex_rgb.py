from sys import argv
from random import randint

colours = []
for i in range(int(argv[1])):
	n = randint(0, 16777215)
	rgb = str(hex(n))
	rgb = '#' + rgb[2:]
	colours.append(rgb)


print(colours)