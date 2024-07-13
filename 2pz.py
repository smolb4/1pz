import math

x=-15.246
y=4.642*10**(-2)
z=21

first = y **(-(math.sqrt(abs(x))))
second = math.log(first)
third = x - (y/2)
fourth = second * third
fifth = math.atan(z)
sixth = math.sin(third)**2

s = fourth + sixth
print(s)