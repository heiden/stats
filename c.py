# p < q significa que p domina q
# p > q significa que p é dominado por q

# 			b E B | existe a E A : a < b
# c(A,B) = ------------------------------
#					   len(B)

# para cada cara em B, veja se alguem em A domina ele e divide pelo total em B

# c(A,B) eh o percentual de solucoes em B que sao dominados
# por pelo menos uma solucao em A \cite{metrica_c}

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