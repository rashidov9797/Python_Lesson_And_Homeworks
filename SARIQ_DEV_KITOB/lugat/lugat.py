
car = {}


# car['model'] = 'Mazda'
# car['color'] = 'red'
# car['price']='230_000'

# print(f"{car['color']}, {car['model']}, {car ['price']} $")


python = {'integer': 'butun sonlar', 'float':'onlik sonlar', 'string':'matn',
'if-else': 'taqqoslash operatori','tuples':'ozgarmas, () ishlatiladi'}

soz=str(input('Iltimos sozni kiriting--->>>'))


for i in python:
  
  if soz.upper() == i:
    print(f" Siz izlagan  {i} sozi lugatda mavjud")

  else:
    print(f" Siz izlagan  {i} sozi lugatda mavjud emas")

  


