
class Talaba:
  def __init__(self,ism,familya,tyili):
    self.ism = ism
    self.familya = familya
    self.tyili = tyili
    self.bosqich = 1

  def get_info(self):
    return f"{self.ism} {self.familya} {self.bosqich} - bosqich talabasi"  

talaba1=Talaba("Azamat",'Rashidov',1997) 
talaba1.bosqich =3
print(talaba1.get_info())   



class  Fan():

  def __init__(self,nomi):
    self.nomi = nomi
    self.talabalar_soni = 0
    self.talabalar =[]


  def add_student(self,talaba):
    """Fanga talaba qo'shamiz"""

    self.talabalar.append(talaba)
    self.talabalar_soni +=1  


  def get_studets(self):
    return [talaba.get_info() for talaba in self.talabalar]  

    # self.talabalar ichidagi har bir talaba uchun get_info() metodini chiqar


matem = Fan("Oliy Matematika")  

student1=Talaba("Azamat", 'Rashidov',1997)
student2=Talaba("Ahmad", 'Karimov',1990)
student3=Talaba("Avaz", 'Rashidov',2002)

matem.add_student(student1)
matem.add_student(student2)
print(f"Oliy Matematika kursimizga yozilgan talabalar soni {matem.talabalar_soni} nafarni tashkil etadi")


print(matem.talabalar)


mate_talaba = matem.get_studets()
print(mate_talaba)


print(talaba1.__dict__)


# DIR funksiyasi yordamida istalgan obyekt yoki klassning metodlarini korib olishimiz mumkin :

# print(dir(Talaba))


# ___ ___ chiziqchalar bilan boshlanadigan mwtodlarga dunder metodlar deb ataladi


# ___ dic___ Metodi ------===--  Ushbu metod OBYEKtNING xususiyatlarini lug'at ko'rinishida qaytaradi



