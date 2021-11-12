
# def yosh_sora(ism,yosh):
#   print(f"Foydalanuvchining ismi: {ism} \n Foydalanuvchining tug'ilgan yili :{ 2021 - int(yosh)} ")


# yosh_sora('Azamat',24)
# yosh_sora('Avaz',22)




# def son_kirit(x):
#   print(f" {x} sonining kvadrati {x **2}  soniga teng")
#   print(f" {x} sonining kubi {x **3}  soniga teng")
# son_kirit(4)  


# JUFT YOKI TOQ

# def son_kirit(x):
#   if x%2 !=0:
#     print(f"Siz kiritgan {x} soni juft emas")
#   else:
#     print(f"Siz kiritgan {x} soni juft")

# son_kirit(5)    
# son_kirit(2)


# Taqqoslash

# def ikkta_son_kirit(x,y):
#   if x<y:
#     print(f"{x} soni {y} sonidan kichik")
#   elif x>y:
#     print(f"{x} soni {y} sonidan katta")
#   else:
#     print("sonlar teng")
      

# ikkta_son_kirit(55,88) 
# ikkta_son_kirit(103,88) 
# ikkta_son_kirit(88,88) 


# def daraja_ol(x,n):
#   print(f"{x} sonining {n}- darajasi {x ** n} soniga teng! ")
# daraja_ol(22,22)
# daraja_ol(2,2)  


# def son_bolamiz(x):
#   for i in range(2,20):
#     if not x%i:
#       print(f"{x} soni {i} soniga qoldiqsiz bo'linadi!!!")

# son_bolamiz(20)      



# FUNKSIYADAN ROYXAT QAYTARISH

# def oraliq(bir,ikki):
#   sonlar = []
#   while bir < ikki:
#     sonlar.append(bir)
#     bir +=1
#   return sonlar


# print(oraliq(50,200))


# user =[]

# def users(ismi, familya,t_joyi,tel,email):
#   mijoz ={
#     'ismi' : ismi,
#     'familya': familya,
#     'tugilgan yili': 2021-t_yil,
#     'manzil': t_joyi,
#     'tel' : tel,
#     'email':email,
#   }
#   return mijoz

# while True:

#   ismi = input('Ismingizni kiriting--->>>')
#   familya = input("Familyangizni kiriting--->>>")
#   t_yil = int(input("Tugilgan yilingizni kiriting--->>>"))
#   t_joyi = input('Tugilgan joyingizni kiriting--->>>')
#   tel = int(input('Tel raqamingiz--->>>'))
#   email = input("Email adressingiz--->>>")

#   user.append(users(ismi,familya,t_joyi,tel,email))

#   javob = input("Davom etasizmi? (ha/yo'q)")
#   if javob!='ha':
#     break

# print("Mijozlar:")

# for mijoz in user:
#   print(f"{mijoz['ismi'].title()}, {mijoz['familya'].title()}, telefoni: {mijoz['tel']}), {mijoz['email'].title()}")







# UCHTA SONDAN ENG KATTASINI CHIQAR




# def katta_son(x,y,z):
#   max=x 
#   if y>=max:
#     max = y
#   if z>=max:
#     max = z
#   return max

# print(katta_son(22,33,10101))


# def son(a,d,s):
#   if a>=d:
#     d=a 
#   if s>=d:
#     d=s 
#   return d

# print(katta_son(223000,222,1231))





 



# def kattasini_top(x,r,t,z):

#   """Eng kattasini aniqlovchi funksiya"""   

#   if x>=r:
#     r=x 
#   if r>=t:
#     t=r 
#   if t>=z:
#     z=t 
#   return z  


# print(kattasini_top(11,33,22,55))
# print(kattasini_top(333,200,2,55))




# def aylana_info(radius,pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*pi,
#               "yuza":pi*radius**2}
#     return aylana

# def aylana_info(radius,pi=3.14159):
#   aylana={
#     "radius":radius,
#     "diametr":2*radius,
#     "perimetr":2*radius*pi,
#     "yuza":pi*radius**2
#   }    
#   return aylana

# print(f"{aylana_info(2)}")  



# TUB SONLAR

# def tub_sonlar(a=range(2,30)):
#   if a%a==0:
#     print(f"{a} soni tub son")
#   if a%1==0:
#     print(f"{a} soni tub son")


#   return a
# tub_sonlar()    