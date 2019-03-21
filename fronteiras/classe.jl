using CSV
using Random
using StatsBase
using DataFrames
using Distributions
using RandomNumbers

mutable struct Individuo

	ativos  :: Vector{Int32}
	lotes   :: Vector{Float32}

	Individuo(a, l) = new(a, l)

end

mutable struct NSGA

	cx :: Float32
	mr :: Float32

	μ :: Vector{Float32}
	σ :: Vector{Float32}
	
	tam_populacao :: Int32
	cardinalidade :: Int32

	populacao :: Vector{Individuo}

	# custodia 	:: Float32
	# corretagem  :: Float32
	# emolumentos :: Float32
	# capital		:: Vector{Float32}

	NSGA(cx, mr, μ, σ, tam, k, pop) = new(cx, mr, μ, σ, tam, k, pop)

end