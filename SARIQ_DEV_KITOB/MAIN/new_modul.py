
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

