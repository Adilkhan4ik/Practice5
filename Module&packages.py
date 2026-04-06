import mymodule

print(mymodule.greet("Ali"))  # Hello Ali
print(mymodule.pi)            # 3.1415


from mymodule import greet, pi

print(greet("Dana"))
print(pi)


import mymodule as mm

print(mm.greet("Zara"))


from my_package import math_utils, string_utils

print(math_utils.add(5, 3))          # 8
print(string_utils.greet("Ali"))     # Hello Ali


from my_package.tools import calc

print(calc.add(10, 20))

