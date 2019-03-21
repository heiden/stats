include("classe.jl")
include("fitness.jl")

function plot(fronteira, dir, arq)
	open(dir * "res-" * arq, "w") do f # append = "a"
		for ponto in fronteira
			write(f, string(ponto[1]) * " " * string(ponto[2]) * "\n")
		end
	end
end

dir = "./res/"
arqs = readdir(dir)
for arq in arqs
	println(arq)
	pontos = []
	open(dir * arq, "r") do f
		for line in eachline(f)
			risco, retorno = map(x->parse(Float32, x), split(line))
			push!(pontos, (risco => retorno))
		end
	end

	fronteiras, indices = nds(pontos)
	plot(fronteiras[1], dir, arq)
end

# for p in fronteiras[1]
# 	println(p)
# end

# println(length(fronteiras[1]))
