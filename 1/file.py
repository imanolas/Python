import math
a1 = float(input('a1= '))
a2 = float(input('a2= '))
b1 = float(input('b1= '))
b2 = float(input('b2= '))

ab = a1*b1+a2*b2

a = math.sqrt(a1**2+a2**2)
b = math.sqrt(b1**2+b2**2)

costh = ab/(a*b)

goniatheta = math.degrees(math.acos(a/b))

print('costh= ', costh)
print('goniatheta= ', goniatheta)
