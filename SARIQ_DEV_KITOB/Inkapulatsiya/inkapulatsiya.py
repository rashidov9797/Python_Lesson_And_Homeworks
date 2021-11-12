from uuid import  uuid4

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
    self.__id = uuid4()

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




avto = Avto("Wolkswagen","Lamborgini","Oq","2021","435.000",10.000)

print(avto.get_km())
print(avto.get_id())
avto.add_km(1800)
print(f" Avtomashina {avto.get_km()} km yurgan")
print(Avto.num_avto)

