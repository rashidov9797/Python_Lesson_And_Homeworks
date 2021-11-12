
class Avtosalon : 
  """Avtosalon klassi"""

  def __init__(self,name):
    self.name = name
    self.avtolar = [] 


  def  __repr__(self):
    return f"{self.name} avtosaloni"  

    
  def __len__(self):
    return len(self.avtolar)


  def __getitem__(self,index): 
    return self.avtolar[index]



  def __setitem__(self,index,value):
    if isinstance(value,Avto):
      self.avtolar[index] = value 

  def __add__(self,qiymat):
      if isinstance(qiymat,AvtoSalon):
        yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")

        yangi_salon.avtolar = self.avtolar + qiymat
        return yangi_salon

      elif isinstance(qiymat,Avto):
        self.add_avto(qiymat)
      else:
        print(f"Avtosalonga {type(qiymat)} qo'shib bo'lmaydi")    



  def __call__(self,*param):
    if param:
      for avto in param:
        if isinstance(avto,Avto):
          self.avtolar.append(avto)
        else:
          print("Avto obyektini kiriting")  
  def get_list(self):
    return [avto for avto in self.avtolar]



      
