set terminal wxt
set k b

plot "4finaldata_64.txt" u 1:(1-$5/$4**2/3) w l, "4finaldata_72.txt" u 1:(1-$5/$4**2/3) w l, "4finaldata_108.txt" u 1:(1-$5/$4**2/3) w l,"4finaldata_128.txt" u 1:(1-$5/$4**2/3) w l

n=1;bn=0.08;gn=1.895;pc=0.04;


#plot "4finaldata_64.txt" u (pc-$1)*64**n:(1-$5/$4**2/3) w l , "4finaldata_72.txt" u (pc-$1)*72**n:(1-$5/$4**2/3) w l , "4finaldata_108.txt" u (pc-$1)*108**n:(1-$5/$4**2/3)  w l

#plot "4finaldata_64.txt" u (pc-$1)*64**n:($3)*64**(bn-2) w l , "4finaldata_72.txt" u (pc-$1)*72**n:($3)*72**(bn-2) w l, "4finaldata_108.txt" u (pc-$1)*108**n:($3)*108**(bn-2) w l 

#plot "4finaldata_64.txt" u (pc-$1)*64**n:($4-$3**2)*64**(-gn-2) w l, "4finaldata_72.txt" u (pc-$1)*72**n:($4-$3**2)*72**(-gn-2) w l, "4finaldata_108.txt" u (pc-$1)*108**n:($4-$3**2)*108**(-gn-2) w l


#set sty d lp

pause -1
