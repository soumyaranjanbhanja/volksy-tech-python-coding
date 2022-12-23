#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a=number-1
for i in range(10000):
            if i%2 == 0 or i>5:
                 print("{} is greater than {}".format(number,5))
            elif i == 0:
                  print("{} and is 0".format(number))
            else:
                  print("{} and is less than 6 and not zero".format(number))
          
