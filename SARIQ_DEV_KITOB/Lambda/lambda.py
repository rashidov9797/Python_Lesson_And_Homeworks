import math 
from math import sqrt

# uzunlik = lambda pi,r : 2*pi*r 
# print(uzunlik(math.pi,10))


# def daraja(n):
#   return lambda x : x**n 

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga teng")
# print(f"3-ning kubi {kub(3)} ga teng")

# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))\




sonlar = list(range(11))

def daraja(x):
  """Berilgan sonning kvadratini qaytar"""
  return x*x

print(list(map(daraja,sonlar)))



# MAP da bir nechta royxat

# a=[4,5,7,8]
# b=[44,2,12,4]

# a_plus_b = list(map(lambda x,y: x+y,a,b ))
# print(a_plus_b)


# ismlar =['Hasan','Husan','Azamat']
# print(list(map(lambda matn : matn.upper(),ismlar)))

# Lambdaga matn degan funksiya yaratib olib, yozuvlarni upper orqali katta qilib, ismlarni chiqardik