set terminal wxt
set k bottom

#plot "data_L64.txt" u 2:(1-$5/$4**2/3) w l, "data_L72.txt" u 2:(1-$5/$4**2/3) w l#, "data_L108.txt" u 2:(1-$5/$4**2/3) w l

n=1;bn=0.053;gn=1.896;wc=0.019;

plot "data_L64.txt" u (wc-$2)*64**n:(1-$5/$4**2/3) w l, "data_L72.txt" u (wc-$2)*72**n:(1-$5/$4**2/3) w l 

#plot "data_L64.txt" u (wc-$2)*64**n:($3)*64**(bn-2) w l, "data_L72.txt" u (wc-$2)*72**n:($3)*72**(bn-2) w l

#plot "data_L64.txt" u (wc-$2)*64**n:($4-$3**2)*64**(-gn-2) w l, "data_L72.txt" u (wc-$2)*72**n:($4-$3**2)*72**(-gn-2) w l



pause -1
