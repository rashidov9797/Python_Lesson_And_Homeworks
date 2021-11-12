
import pickle

talaba1= {'ism': 'azamat', 'familya': 'rashidov', 'tyil':'1997','kurs':'4'}
talaba2= {'ism': 'ahmad', 'familya': 'karimov', 'tyil':'1997','kurs':'3'}



with open('info','rb') as file:
  talaba1 = pickle.load(file)
  talaba2 = pickle.load(file)

print(talaba1)  
