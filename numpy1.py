import numpy as np
import numpy.random as rd

a = [1,2,3,4]
b = np.array(a,dtype='float64')
print(b.size,b.shape,b.ndim,b.dtype)

array_one = np.ones([10,10])
array_zero = np.zeros([10,10])
print(array_zero)
print(array_one)

rand1 = rd.rand(10,10)
rand_float = rd.uniform(0,100)
rand_int = rd.randint(0,100)
print(rand1)
print(rand_float)
print(rand_int)

norm1 = rd.normal(1.75,0.1,(4,5))
print(norm1)
print(norm1[1:3,2:4])
norm2 = norm1.reshape([10,2])
print(norm2)

n = np.arange(0,30,2)
print(n.reshape([3,5]))
o = np.linspace(0,30,16)
o = o.reshape([4,4])
print(o)

print(np.eye(3))
print(np.diag([3,4,5]))