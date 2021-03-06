include("classe.jl")
include("fitness.jl")

function plot(fronteira, dir, arq)
	open(dir * arq, "w") do f # append = "a"
		for ponto in fronteira
			write(f, string(ponto[1]) * " " * string(ponto[2]) * "\n")
		end
	end
end

k = ["3", "9", "15"]
algs = ["brkga", "hibrido", "nsga"]

for alg in algs
	for i in k
		pontos = []
		dir = "dados-com-busca-local/" * alg * "/" * i * "/"
		println(dir)
		arqs = readdir(dir)
		for arq in arqs
			open(dir * arq, "r") do f
				for line in eachline(f)
					risco, retorno = map(x->parse(Float32, x), split(line))
					push!(pontos, (risco => retorno))
				end
			end
		end
		fronteiras, indices = nds(pontos)
		plot(fronteiras[1], "fronteiras/", alg * "-" * i)
	end
end
