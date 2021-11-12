

class User:

  """User nomli klass yaratdim"""

  def __init__(self,ismi,fam,tyil,email):
    self.ismi = ismi
    self.fam = fam
    self.tyil = tyil
    self.email = email

  def Email_adress(self):
    print(f"Mening email addressim {self.email}")

  def Ism_Fam(self):
    print(f"Men {self.fam} {self.ismi}")

  def get_age(self,yili):
    return yili-self.tyil

  def Toliq_malumot_ber(self):
    print(f"Men {self.fam} {self.ismi} {self.tyil} yilda tug'ilganman.  "
    f"Mening email manzilim {self.email}")  



user1 = User("Azamat",'Rashidov', 1997, 'azikrashidov1103@gmail.com')



user1.Ism_Fam()
user1.Email_adress()
print(user1.get_age(2021))
user1.Toliq_malumot_ber()

