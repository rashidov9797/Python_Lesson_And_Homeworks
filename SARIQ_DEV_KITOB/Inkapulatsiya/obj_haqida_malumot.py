

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


  def __repr__(self):
    """Obyektimiz haqida to'liq ma'lumot"""

    return f"Avto : Model : {self.model} Yili: {self.yil} Rangi: {self.tang} Narxi: {self.narx} million so'm "

    # Agar object ichiga __repr__ yoki str metodini yozmasak to'g'ridan to'g'ri murojaat etilganda ma'lumot chiqarmaydi
    


  def get_km(self):
    return self.__km



  def add_km(self,km):
    """Km ga yana km qo'shish"""
    if km>=0:
      self.__km += km
    else:
      return "Mashinani km ni qaytarib bo'lmaydi"  


avto = Avto("GM","Malibu","Oq","2021","248.000",10.000)

print(avto)