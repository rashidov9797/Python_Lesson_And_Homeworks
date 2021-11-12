class Shaxs:
  """Shaxslar haqida ma'lumot"""
  def __init__(self,ism,familya,passport,tyil):
    self.ism = ism
    self.familya = familya
    self.passport = passport
    self.tyil = tyil
   


  def get_info(self):
    """Shaxslar haqida ma'lumot"""
    info = f"{self.ism} {self.familya} \n"
    info += f"Passport : {self.passport} \n {self.tyil}-yilda tug'ilgan" 

    return info

  def get_age(self,yil= 2021):
    """Shaxsning yoshini qaytaruvchi metod"""


  def get_no_diplom(self):
    return self.no_diplom
    

    return yil - self.tyil

inson = Shaxs("Azamat","Rashidov","AA4433399",1997)

print(inson.get_age())
print(inson.get_info())

class Manzil():
  """Manzil saqlash uchun klassi"""

  def __init__(self,viloyat,tuman,mahalla):
    self.viloyat = viloyat
    self.tuman = tuman
    self.mahalla = mahalla

  def get_manzil(self):
    """Manzilni ko'rish"""
    
    manzil = f"{self.viloyat} viloyati {self.tuman} tumani, "
    manzil += f"{self.mahalla} mahallasi"

    return manzil



class Tala(Shaxs):
  """Talaba klassi"""
  __talaba_soni=0

  def __init__(self,ism,familya,passport,tyil,id,manzil):
    super().__init__(ism,familya,passport,tyil)
    self.idraqam = id
    self.bosqich =1
    self.manzil = manzil
    Tala.__talaba_soni +=1

  def get_id(self):
    """Talabaning ID raqami"""
    return self.idraqam
  def get_bosqich(self):
    return self.bosqich    

  def get_info(self):
    """Talabaning ma'lumotlarini qaytar"""
    info = f"{self.ism} {self.familya}."
    info += f"{self.get_bosqich()} - bosqich . \n ID: {self.idraqam}" 

    return info 

  @classmethod
  def get_num_talaba(cls):
    return cls.__talaba_soni  




manzil = Manzil("Surxondaryo","Sariosiyo","Chilonzor")
talaba = Tala("Avaz","Karimob","Fa632852869",2002,'20210098',manzil)


print(talaba.manzil.tuman)
print(talaba.manzil.get_manzil())



print(f"Hozirda mavjud talabalar soni {Tala.get_num_talaba()} nafar")
