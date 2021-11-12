
# car={
#   'model':'nexia',
#   'rang':'oq',
#   'yil': '2020'
# }

# car1={
#   'model':'kobalt',
#   'rang':'qora',
#   'yil': '2019'
# }

# car2={
#   'model':'malibu',
#   'rang':'oq',
#   'yil': '1998'
# }

# cars = [car,car1,car2]
# for i in cars:
#   print(f"{i['model'].title()},"
#   f"{car['rang']}rang,"
#   f"{car['yil']}-yil "
#   )


coder = {
  'ali':['python','c++'],
  'vali':['java','c++'],
  'hadi':['python','JS'],
}

for ism, til in coder.items():
  print(f"\n{ism.title()}: ", end='')
  for tillar in til:
    print(f"{tillar.upper()}",end='')