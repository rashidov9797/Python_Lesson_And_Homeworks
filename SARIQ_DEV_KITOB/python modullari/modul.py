import random as r 

from random import  shuffle,sample


# RANDINT ---->>>  a va b sonlar oralig'idan tasodifiy butun son qaytaradi

# son = r.randint(0,100)
# print(son)





#   CHOICE(X) ------>>>> Berilgan x argumentning ichidan tasodifiy sonni qaytaradi

# ismlar = ['olim','anvar','33','4565']

# ism = r.choice(ismlar)

# print(ism)



# x = list(range(0,100,5))
# print(x)

# print(r.choice(x))



#   SHUFFLE(X) ------>>> X ichidagi elementni tasodifiy tartibda chiqaradi

# x = list(range(12))
# print(x)
# print(r.shuffle(x))



# SAMPLE(x,k) ---- X royxat ichidan tasodifiy k ta elementni ajratish


x = list(range(0,100))
y=sample(x,k=8)
print(y)
