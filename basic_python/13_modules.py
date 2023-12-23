## modules ##
import math
import time
import my_module

my_module.sum_value(5,3,1)
my_module.print_value("Hola ELiot!")

from my_module import sum_value, print_value

sum_value(5,4,32)
print_value("Hello Word")

print(time.strftime("%c"))

print(math.pi)
print(math.pow(2,8))

from math import pi as pi_value
print(pi_value)