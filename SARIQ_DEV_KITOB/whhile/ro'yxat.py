# ismlar=[]

# print("Yaqin do'stlaringiz ro'yxatini tuzing")
# n=1 
# while  True:
#   savol = f"{n}-do'stingiz ismini kiriting--->>>"
#   ism=input(savol)
#   ismlar.append(ism)
#   javob = input("Yana ism qo'shasizmi ? (xa/yoq)")

#   if javob == 'xa':
#     n+=1
#     continue
#   else:
#     break
# print(f"{ismlar} dan iborat ro'yxat tuzildi!")  


# print("Do'stlaringiz ismlari:")

# for i in ismlar:
#   print(i.title())


# print("Do'stlarimiz yoshini saqlaymiz")
# dostlar={} 
# ishora =True

# while ishora:
#   ism = input("Dostingizni ismini kiriting--->>>")
#   yosh=input("Dostingizni yoshini kiriting--->>>")
#   dostlar[ism] = int(yosh)


#   javob = input("Yana malumot qoshasizmi?  (xa/yoq) --->>>")
#   if javob == 'yoq':
#     ishora = False

# for ism,yosh in dostlar.items():
#   print(f"{ism.title()} {yosh} yoshda")    



# ELEMENT KOCHIRISH

# talabalar = ['aziz','nodir','bahodir','olim']
# baholanmagan={}
# while talabalar:
#   talaba=talabalar.pop()
#   baho=input(f'Talaba {talaba} bahosini kiriting--->>>')
#   print(f"{talaba.title()} baholandi")
#   baholanmagan[talaba]=baho

# talabalar = ['Azamat',"murod","fazli",'Olimjon','Avazbek']
# baholangan ={}
# while  talabalar:
#   talaba = talabalar.pop()
#   baho=(input(f"Talaba {talaba} ning bahosini kiriting--->>>"))
#   print(f"Talaba {talaba} ning bahosi {baho}")
#   baholangan[talaba]= baho
# print(baholangan)  