from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

e = (x**2-1)/(x-1)

print(e.factor())
print(e.expand())
print(e.simplify())

f = sin(x)/cos(x)
print(y.trigsimp())

a = Symbol('a')
b = Symbol('b')
g = x**a*x**b
print(g.powsimp())

print(solve([y+x/4,x-13-4*z,4*x-y+z-1],[x,y,z]))
