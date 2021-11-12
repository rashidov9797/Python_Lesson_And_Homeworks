
from  vorislik import Shaxs,Manzil


class Admin(Shaxs):
  def __init__(self,ism,familya,passport,tyil,manzil):
    super().__init__(ism,familya,passport,tyil)

  def get_info_admin(self):
    return f"{self.ism}{self.familya} \n {self.passport}{self.tyil}"  


manzil1 = Manzil("Toshkent","Chirchiq","Yangi")
admin = Admin("Azamat","Rashidov","123867",1997,manzil1)

print(admin.get_info_admin())

