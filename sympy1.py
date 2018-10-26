from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

e = (x**2-1)/(x-1)

pprint(e.factor())
pprint(e.expand())
pprint(e.simplify())

f = sin(x)/cos(x)
pprint(y.trigsimp())

a = Symbol('a')
b = Symbol('b')
g = x**a*x**b
pprint(g.powsimp())

pprint(solve([y+x/4,x-13-4*z,4*x-y+z-1],[x,y,z]))

h = 2*x**2*(x-(sin(x))**2*cos(x**2)*E**sin(x))
pprint(series(h))