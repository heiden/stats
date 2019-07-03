set encoding utf8
set xlabel "Risco"
set ylabel "Retorno"

set xtics 0.001
set key top left box 1

plot "pontos" smooth sbezier title "current test", "pontos" with points notitle

set term pngcairo size 800, 600 
set output "portfolios.png"
replot
set output