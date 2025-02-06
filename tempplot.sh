#!/bin/bash
rm -f temp.gnu
echo "set xdata time
set timefmt '%Y%m%d-%H:%M:%S'
set format x '%H:%M'
set timefmt '%Y%m%d-%H:%M:%S'
set y2tics 0,10
set logscale y2
set format y2 '10^{%L}'
set ytics nomirror
set xlabel 'Time'
set ylabel 'Temp (K)'
set y2label 'mbar'
set timestamp
plot '$1' u 1:2 w l axis x1y1 tit 'T1', '$1' u 1:3 w l axis x1y1 tit 'T2','$1' u 1:4 w l axis x1y1 tit 'T3','$1' u 1:5 w l axis x1y1 tit 'T4', '$1' u 1:6 w l axis x1y2 tit 'Pirani',  '$1' u 1:7 w l axis x1y2 tit 'Cold cathode gauge' lt -1
while(1){
	pause 10
	replot
}">>temp.gnu
sleep 1
gnuplot temp.gnu
