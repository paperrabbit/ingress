# -*- coding: utf-8 -*-
#Author: rayman.mobile@gmail.com
#Create:2013-03-09
#Last:2013-03-09
#
#ingress intel config



cookie=''

commdb='/home/ingress/comm.db'
mapdb='/home/ingress python/map.db'
kmlloc='/var/www/html/ingress_dg.kml'


import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)

minLat=31500000
maxLat=31750000
minLng=119880000
maxLng=120530000

#add 3 random number
mapid='01321223%s%s%s'%(a,b,c)




