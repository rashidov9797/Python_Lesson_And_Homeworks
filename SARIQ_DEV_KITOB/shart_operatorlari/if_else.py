# avtolar = ['audi','bmw','volvo','gm','mazda']

# print(avtolar)
# for i in avtolar:
#   if i != 'gm':
#     print(i.title())
#   else:
#     print(i.upper())





# admin = 'azamat'

# ism = input('Iltimos ismingizni kiriting ...')


# if ism.lower() != 'admin':
#   print(f"Xush kelibsiz janob {ism}")
# else:
#   print(f"Xush kelibsiz {ism} Xayrli kun !")  
    



# a = input('Iltimos birinchi sonni  kiriting ...')

# b = input('Iltimos ikkinchi sonni  kiriting ...')

# if a == b:
#   print(f"{a} va {b} sonlar o'zaro teng")
# else:
#   print('Sonlar ozaro teng emas ')  





# a = int(input('Iltimos  sonni  kiriting ...'))



# if a <= 0: 
#   print(f"{a}  soni toq")
# else:
#   print(f'Siz kiritgan {a} soni juft son') 




# yosh = int(input('Yoshingiznki kiriting..'))

# if yosh <= 4:
#   price = 0
# elif  yosh<12:
#   price = 5000
# else:
#   price =12000
# print(f"Sizga kirish {price} so'm")  




# ----== AND OR OPERATORLARI ---====

#kun = input('Bugun kun nima ? >>>>')

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#   print(f"Bugun {kun}. Dam olish kuningiz maroqli o'tsin")
# else:
#   print(f"Bugun {kun}. Sugoheyooong!!!") 



# kun = input('Bugun qanday kun ?')
# harorat = float(input("Havo harorati qanday ?"))

# if kun.lower() == 'shanba' and harorat>=30:
#   print("Akang kuchaydi uje, ketdik dam olgani!")

# elif kun.lower() == 'shanba' and  harorat<30:
#   print("Akang bugun dam oladi")  




# narx = 15000

# choy = True
# salat = False

# if choy and  salat:
#   narx = narx+1000
# elif choy or salat:
#   narx = narx+5000
# print(f"Jami {narx} som")   
# 
# 
# 


# --===== In  - Ro'yxatni tarkibini tekshiradi


# menyu = ['osh','somsa','tandir','qozonkabob']
# ovqat = input('Nima ovqat buyurtma qilasiz ? ---->')

# if ovqat.lower() in menyu:
#   print(f"{ovqat} buyurtmangiz qabul qilindi!")
# else:
#   print("Afsuski hozir bunday taom yo'q!!!")  


# IKKI ro'yxatni solishtirish


# menyu = ['osh','somsa','tandir','qozonkabob']

# zakas = ['osh','tandir','manti']

# if zakas:
#   for taom in zakas:
#     if taom in menyu:
#       print(f"{taom} buyurtmangiz qabul qilindi!")
#     else:
#       print(f"{taom} buyurtmangiz hozirda mavjud emas!")

# else:
#   print("Savatchangiz bo'sh")      
        
  