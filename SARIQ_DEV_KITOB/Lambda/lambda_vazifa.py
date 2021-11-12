
import random as r

from random import sample

# kopaytma = lambda x: x*10
# print(kopaytma(2)) 

# sonlar = lambda x,y: x+y

# print(sonlar(2,4))




x=list(range(0,20))
son = sample(x,k=10)

print(son)



# Sonni kvadratini hisobladim


kvadrat_hisobla = list(map(lambda y: y*y,son))

print(kvadrat_hisobla)


# Filter orqali toq sonlarni ajratdim


toq_sonlar = list(filter(lambda a: a%2==1,son))
print(f"Ro'yxatdagi toq sonlar shularda iborat \n {toq_sonlar}")






