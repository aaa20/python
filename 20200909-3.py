from datetime import *
import time
import random 

ldates = []

d1 = date(2016, 8, 12)
d2 = date(2018, 7, 12)
d3 = date(2017, 7, 12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()


time.sleep(random.randint(3, 10))

for d in ldates:
    print(d)