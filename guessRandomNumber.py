import random

import random
a= random.randint(1,100)
while(1):
    n=int(input("guess: "))
    if  n==a:
        print("correct")
        break
    elif n>a:
        print("large")
    elif 0<n<a:
        print("small")
    else:
        break
