set terminal wxt
set k t

set sty d l
plot "2data_L64.txt" u 2:(1-$5/$4**2/3) w l, "2data_L72.txt" u 2:(1-$5/$4**2/3) w l, "2data_L108.txt" u 2:(1-$5/$4**2/3) w l, "2data_L128.txt" u 2:(1-$5/$4**2/3) w l

n=1.1;bn=0.055;gn=1.89;wc=0.018;

#plot "2data_L64.txt" u (wc-$2)*64**n:(1-$5/$4**2/3)  , "2data_L72.txt" u (wc-$2)*72**n:(1-$5/$4**2/3)  , "2data_L108.txt" u (wc-$2)*108**n:(1-$5/$4**2/3)  , "2data_L128.txt" u (wc-$2)*128**n:(1-$5/$4**2/3)

#plot "2data_L64.txt" u (wc-$2)*64**n:($3)*64**(bn-2) w l , "2data_L72.txt" u (wc-$2)*72**n:($3)*72**(bn-2) w l, "2data_L108.txt" u (wc-$2)*108**n:($3)*108**(bn-2) w l,"2data_L128.txt" u (wc-$2)*128**n:($3)*128**(bn-2) w l 


#plot "2data_L64.txt" u (wc-$2)*64**n:($4-$3**2)*64**(-gn-2) w l , "2data_L72.txt" u (wc-$2)*72**n:($4-$3**2)*72**(-gn-2) w l , "2data_L108.txt" u (wc-$2)*108**n:($4-$3**2)*108**(-gn-2) w l,"2data_L128.txt" u (wc-$2)*128**n:($4-$3**2)*128**(-gn-2) w l


pause -1