#Nama File: sa

import random
import math


t = 1000
tampung  = []

while t > 9 :
    x1= (random.uniform(-10, 10))  
    x2= (random.uniform(-10, 10))
    f1 = ((4-(2.1*x1**2) + (x1**4/3))*x1**2+ x1*x2 + (-4+(4*x2**2))*x2**2)
    print("nilai fungsi : ", f1)
    
    z1=  (random.uniform(-10, 10))
    z2= (random.uniform(-10, 10))
    f2 = ((4-(2.1 * z1**2) + (z1**4/3))*z1**2+ z1*z2 + (-4+(4*z2**2))*z2**2)
    print("nilai fungsi : ", f2)
    
    
    if (f2<f1) :
        f1 = f2
    elif (math.exp(-(f2-f1)/t) > random.uniform(0,1)) :
        f1 = f2
    else :
        f1 = f1
        
   
    t = (0.9*t)  
    tampung.append(f1)
    
print("nilai minimum dari fungsi : ", min(tampung))
            
     
     




     

