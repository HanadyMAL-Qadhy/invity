import numpy as np

z=np.zeros(10)
print(z)

o=np.ones(10)
print(o)

o=np.ones(10)
print(o+4)

array=np.arange(10,51)
print(array)

array=np.arange(12,51,2)
print(array)

u=np.arange(0,9)
shape=u.reshape(3,3)
print(shape)

e=np.eye(3)
print(e)

r=np.random.rand(1)
print(r)

'''r=np.random.randn(25)
print(r)

r=np.random.randn(2)
print(r)'''

r=np.random.randn(20)
r.sort()
print(r)

array=np.arange(0.01,1.01,0.01).reshape(10,10)
print(array)

array=np.linspace(0,1,20)
print(array)
