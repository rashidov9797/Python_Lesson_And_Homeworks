import random as r


# JUFT SONLARNI FILTERDA CHIQARISH

# sonlaf = r.sample(range(100),10)

# def juftmi(x):
#   """Juxt bolsa True toq bolsa False qaytaramiz"""
#   return x%2 ==0 

# juft_sonlar = list(filter(juftmi,sonlaf))
# print(sonlaf)
# print(juft_sonlar)




# JUFT SONLARNI LAMBDADA CHIQARISH

# sonlar = r.sample(range(200),20)

# juft_sonlar = list(filter(lambda son: son%2==0,sonlar ))

# print(sonlar)
# print(juft_sonlar)





# sonlar = r.sample(range(500),10)

# jusftlar = list(filter(lambda number: number%2==0,sonlar))

# Lambdada number degan ozgaruvxhi yaratdim, shartini berib, ikkinchisiga royxatimni kiritdim

# print(sonlar)
# print(jusftlar)




#  A xarfi bilan boshlanadimi yoki yo'q shuni tekshiramiz


mevalar = ['olma','anor','amjir','shaftoli']

# mvA = list(filter(lambda meva : meva.startswith('a'),mevalar))

# print(mvA)



# Mevalar nomi 4 xarfli yoki undan kam tekshiramiz

# mevalar2 = list(filter(lambda meva: len(meva)<=4 , mevalar))
# print(mevalar2)