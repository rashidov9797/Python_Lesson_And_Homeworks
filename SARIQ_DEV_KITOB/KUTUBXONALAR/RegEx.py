

# Andoza yordamida matn izlash

import re 


# word1 = 'azamat'
# word2 = 'nodir'
# word4 = 'bahodir'


# andoza = 'a....t'

# print(re.match(andoza,word1))
# print(re.match(andoza,word2))
# print(re.match(andoza,word4))



# Email ajratamiz


# matn = """Maqolalar 2020-yilning sentyabr oyiga qadar azikrashidov1103@gmail.com elektron manzili orqali qabul qilinadi"""


# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# email = re.findall(andoza,matn)
# print(email)





# Kuchli parolni tekshiramiz


# andoza = ' ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$ '

# azik = "Yangi parolni kiriting ---->>> \n"

# azik += "(Kamida : 8 xona, 1 ta lotin bosh va 1 ta kichik) \n"

# azik += "1 ta son va maxsus belgi bo'lishi kerak \n"


# while  True:
#   password = input(azik)

#   if re.match(andoza,password):
#     print("Maxfiy so'z qabul qilindi")
#     break
#   else:
#     print("Maxfiy so'z talabga javob bermaydi, iltimos qayta urinib ko'ring :(")  



# Telefon 


andoza = '/[0-9]/'

tel = "Tel raqamni kiriting-->>>\n"
tel += 'Faqat raqamlarni kiriting --->>>'

while True:
  telefon = input(tel)

  if re.match(andoza,telefon):
    print("Telefon raqam saqlandi")
    break
  else:
    print("qayta urinib koring")

    