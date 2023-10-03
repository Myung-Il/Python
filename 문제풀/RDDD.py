from math import sqrt

for i in range(1,31):
    print(i if sqrt(i).is_integer() else '')