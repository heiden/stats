set encoding utf8
set xlabel "Risco"
set ylabel "Retorno"

set key top left box 1
set xtics 0.001

plot "res" smooth sbezier title "NSGA", "res" with points notitle

set term pngcairo size 800, 600 
set output "resultado.png"
replot
set output