

# AVTO KLASS


class Avto:
  def __init__(self,model,rang,karobka,narhi,yili):
    self.model = model
    self.rang = rang
    self.karobka =karobka
    self.narhi = narhi
    self.yili = yili
    self.kilometr = 0

  def get_model(self):
    return self.model 
  def get_rang(self):
    print(f"Ushbu avtomobil {self.rang} ragda")  

  def get_info(self):
    print(f" Ushbu {self.model} avtomobili {self.rang} rangda  "
          f" {self.karobka} karobka. \n  Narhi : {self.narhi} $. {self.yili} yilda ishlab chiqarilgan" 
          f"Hozirda {self.kilometr} kilometr yurgan" )

  def set_km(self,kilometr):
    """Kilometr yangilash"""
    self.kilometr = kilometr  
    kilometr +=1      





# avto1= Avto('Malibu','Oq','Avtomat','22.000','2021')
# avto1.kilometr = 2000 

# print(avto1.get_model())
# avto1.get_rang()
# avto1.get_info()




class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")
    
    def __call__(self,*param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def add_avto(self,*qiymat):
        for avto in qiymat: 
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def get_list(self):
        return [avto for avto in self.avtolar]
