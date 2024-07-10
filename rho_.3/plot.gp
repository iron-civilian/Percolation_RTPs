set terminal wxt

#plot 'data_32.txt' u 3:($4/32**2) w l,'data_48.txt' u 3:($4/48**2) w l,'data_64.txt' u 3:($4/64**2) w l,'data_72.txt' u 3:($4/72**2) w l


#plot 'data_32.txt' u 3:($5-$4**2)/32**2 w l,'data_48.txt' u 3:($5-$4**2)/48**2 w l,'data_64.txt' u 3:($5-$4**2)/64**2 w l,'data_72.txt' u 3:($5-$4**2)/72**2 w l

plot 'data_32.txt' u 3:(1-$6/$5**2/3) w l,'data_48.txt' u 3:(1-$6/$5**2/3) w l,'data_64.txt' u 3:(1-$6/$5**2/3) w l,'data_72.txt' u 3:(1-$6/$5**2/3) w l


pause -1
