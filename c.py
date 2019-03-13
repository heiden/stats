# p < q significa que p domina q
# p > q significa que p é dominado por q

# 			b E B | existe a E A : a < b
# c(A,B) = ------------------------------
#					   len(B)

# para cada cara em B, veja se alguem em A domina ele e divide pelo total em B

# c(A,B) eh o percentual de solucoes em B que sao dominados
# por pelo menos uma solucao em A \cite{metrica_c}

# se c(A,B) = 1, todas as solucoes de B sao dominadas por alguma em A // B eh lixo
# se c(A,B) = 0, nenhuma solucao de B eh dominada por solucoes em A   // B eh top
# c(A,B) nao necessariamente eh igual a 1 - c(B,A) \cite{metrica_c}

#     A      B

# A   -    c(A,B)

# B  c(B,A)  -

# aij - quanto o metodo da linha i domina o metodo da coluna j

# adicionar essa citacao
# @book{metrica_c,
#   title={Multi-objective memetic algorithms},
#   author={Goh, Chi-Keong and Ong, Yew-Soon and Tan, Kay Chen},
#   volume={171},
#   year={2008},
#   publisher={Springer}
# }

from sys import argv

def domina(a, b):
	if a[0] < b[0] and a[1] > b[1]: # [risco, retorno]
		return True
	else:
		return False

file_a = argv[1]
file_b = argv[2]

A = []
with open(file_a) as f:
	for line in f:
		A.append([float(i) for i in line.split()])

B = []
with open(file_b) as f:
	for line in f:
		B.append([float(i) for i in line.split()])

c = 0
for b in B:
	for a in A:
		if domina(a, b):
			c += 1
			break

c /= float(len(B))
print('c(A,B):', c)