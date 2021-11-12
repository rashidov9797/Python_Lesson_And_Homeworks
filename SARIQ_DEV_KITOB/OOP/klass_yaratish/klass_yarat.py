


class Talaba:
  def __init__(self,ism,familya,tyili):
    self.ism = ism
    self.familya = familya
    self.tyili = tyili

  def tanishtir(self):
    print(f"Ismim {self.ism} \n Familyam : {self.familya} \n  Tugilgan yilim : {self.tyili} ")  

  #ISM QAYTAR

  def Ismi(self):
    return self.ism

  #FAMILYA QAYTAR

  def Familya(self):
    return self.familya 



talaba1 = Talaba("Azamat",'Rashidov','1997')
print(talaba1.Familya())





