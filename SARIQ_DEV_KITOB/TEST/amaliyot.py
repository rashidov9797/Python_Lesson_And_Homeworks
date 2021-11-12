

# def son_kirit(a,d,f):

#   katta = a 

#   if d>=katta:
#     katta = d
#   if f>= katta:
#     katta = f
#   return f" {katta} soni eng kattasi "    


    

# print(son_kirit(22,113,4)) 




sonlar = [22,4,66,4445,6667889,99,9,78,443]

juft = []
toq = []

def juftlarni_ol(son):
  for i in son:
    if i %2 ==0:
      juft.append(i)
    else:
      toq.append(i)


print(juftlarni_ol(sonlar)) 
print(juft)
print(toq)

      








