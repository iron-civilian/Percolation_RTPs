set terminal wxt 

set key bottom

#plot "data_L48.txt" u 2:($3/48**2) w l, "data_L64.txt" u 2:($3/64**2) w l


plot "data_L24.txt" u 2:(1-$5/$4**2/3) w l, "data_L32.txt" u 2:(1-$5/$4**2/3) w l, "data_L48.txt" u 2:(1-$5/$4**2/3) w l, "data_L64.txt" u 2:(1-$5/$4**2/3) w l, "data_L72.txt" u 2:(1-$5/$4**2/3) w l lc -1



pause -1
