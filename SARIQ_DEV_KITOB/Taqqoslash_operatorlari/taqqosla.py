class Avto:
  """Avtomobil klassi"""

  num_avto = 0
  
  def __init__(self,make,model,tang,yil,narx,km=0):
    """Avtomobil xususiyatlari"""

    self.make = make
    self.model = model
    self.tang = tang
    self.yil = yil
    self.narx =narx
    self.__km = km


    Avto.num_avto += 1
    # Xar gal yangi moshina obyekti yaratilganda qiymatni bittaga oshirib boradi

    


  def get_km(self):
    return self.__km

  def get_id(self):
    return self.__id

  def add_km(self,km):
    """Km ga yana km qo'shish"""
    if km>=0:
      self.__km += km
    else:
      return "Mashinani km ni qaytarib bo'lmaydi"  


class Avtosalon:
  def __init__(self,name):
    self.name = name
    self.avtolar = []


  def __repr__(self):
    return f"{self.name} avtosaloni "

  def add_avto(self,avto):
    if isinstance(avto,Avto):
      self.avtolar.append(avto)
    else:
      print("Avto obyektini kiriting")    

  def __len__(self):
    return len(self.avtolar)    


# INDEX qaytaruvchi metod
  def __getitem__(self,index):
    return self.avtolar[index]


# OBJECTga o'zgartirish kiritish

  def __setitem__(self,index,value):
    if isinstance(value,Avto):
      self.avtolar[index] = value

avto2 = Avto("Gm","Malibu","oq","2020","230999")

avto1 = Avto("Hyundai","Equnic","oq","2020","10")
salon = Avtosalon("AzikAvto")
print(salon)

for avto in [avto1,avto2]:
  salon.add_avto(avto)

print(salon)





#  Qo'shish metodi   ---- __add__

#  Ayirish metodi   ---- __sub__

#  Kopaytirish metodi   ---- __mul__


#  Daraja metodi   ---- __pow__


#  Bo'lish metodi   ---- __div__




#    CALL parametrlarni chaqirish