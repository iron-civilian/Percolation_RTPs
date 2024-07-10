set terminal 'wxt'

set k b

#plot '2data_L64.txt' u 1:($3/64**2) w l,'2data_L72.txt' u 1:($3/72**2) w l

#plot '2data_L64.txt' u 1:(1-$5/$4**2/3) w l,'2data_L72.txt' u 1:(1-$5/$4**2/3) w l

pc=.0296;nu=1;bn=-2+.053;gn=-2-1.915;

#plot '2data_L64.txt' u (pc-$1)*64**nu:(1-$5/$4**2/3) w l,'2data_L72.txt' u (pc-$1)*72**nu:(1-$5/$4**2/3) w l

#plot '2data_L64.txt' u (pc-$1)*64**nu:($4-$3**2)*64**gn w l,'2data_L72.txt' u (pc-$1)*72**nu:($4-$3**2)*72**gn w l

plot '2data_L64.txt' u (pc-$1)*64**nu:($3)*64**bn w l,'2data_L72.txt' u (pc-$1)*72**nu:($3)*72**bn w l


pause -1
