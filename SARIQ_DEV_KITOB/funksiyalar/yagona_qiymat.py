
# def toliq_ism(ism, familya):
#   """To'liq ism familya qaytaruvchi funksiya"""
#   toliq_ism = f"{ism} {familya}"
#   return toliq_ism


# talaba=toliq_ism('Azamat','Rashidov')  
# talaba1=toliq_ism('Avaz','Karimov') 

# print(f"Talabalarimiz {talaba} hamda {talaba1}  aka-uka")

# def avto_info(model,rang,narh,yili):
#   avto = {
#     'model':  model,
#     'rang' : rang,
#     'narh' : narh,
#     'yili'  : yili
#   }

#   return avto

# avto = avto_info('Malibu','Oq','19_000','2021') 
# avto2=avto_info('Neksiya','Qora','25_000','2021') 

# avtolar = [avto,avto2]

# for car in avtolar:
#   if car['narh']:
#     narh = car['narh']
#   else:
#     narh = 'Nomalum'

#   print(f"{car['model']} {car['rang']} {car['narh']} {car['yili']}")    




# AVTO INFO


def avto_info(model,rang,narh,yili):
  avto = {
    'model':  model,
    'rang' : rang,
    'narh' : narh,
    'yili'  : yili
  }

  return avto


def avto_kirit():
  avtolar = []

  while True:

    print("\n Quyidagii ma'lumotlarni kiriting-->> \n", end='' )

    model = input('Modeli -->>')
    rang = input('Rangi-->>')
    narh = input("Narhi --->>>")
    yili = input("yili--->>>")
    avtolar.append(avto_info(model,rang,yili,narh))



    javob = input("Yana avto qo'shasizmi?  (xa/yoq)")

    if javob =='yoq':
      break


def avto_info_print(avto_info):
  """Avtomobillar haqida ma'lumotni chiqaramiz"""
  print(f"{avto_info['model'].upper()} {avto_info['rang'].title()} "
  f"{avto_info['narh']} $"
  f"{avto_info['yili'].upper()}")






