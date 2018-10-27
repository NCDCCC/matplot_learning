from sympy import *
from sympy.abc import a,b
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

e = (x**2-1)/(x-1)

pprint(e.factor())
pprint(e.expand())
pprint(e.simplify())

f = sin(x)/cos(x)
pprint(y.trigsimp())

g = x**a*x**b
pprint(g.powsimp())

pprint(solve([y+x/4,x-13-4*z,4*x-y+z-1],[x,y,z]))

h = 2*x**2*(x-(sin(x))**2*cos(x**2)*E**sin(x))
pprint(series(h))

i = x/(x-1)
pprint(series(i),x,2)

q = x**2*log(x)
pprint(series(q,x,1))

for i in range(1,6):
	pprint(diff(q,x,i))

p = x - (a+b*cos(x))*sin(x)
pprint(series(p,x,0))