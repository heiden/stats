include("classe.jl")
include("fitness.jl")

function plot(fronteira)
	file = "res"
	open(file, "w") do f # append = "a"
		for ponto in fronteira
			write(f, string(ponto[1]) * " " * string(ponto[2]) * "\n")
		end
	end
	# run(`gnuplot res.gnu`)
	# run(`display portfolios.png`)
end

file = ARGS[1]
pontos = []
open(file, "r") do f
	for line in eachline(f)
		risco, retorno = map(x->parse(Float32, x), split(line))
		push!(pontos, (risco => retorno))
	end
end

fronteiras, indices = nds(pontos)

for p in fronteiras[1]
	println(p)
end

println(length(fronteiras[1]))

# geral = []
# for fr in fronteiras
# 	for f in fr
# 		push!(geral, f)
# 	end
# end

# plot(geral)
plot(fronteiras[1])