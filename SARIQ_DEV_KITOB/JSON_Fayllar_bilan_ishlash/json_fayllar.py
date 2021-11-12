import json





bemor = {

  'ism' : 'Azamat Rashiodov',
  'yosh' : 30,
  'oila' : True,
  'farzandlar': 'avaz',

  'dorilar': [ 
    {"nomi" : 'Analgin', 'miqdori': 0.5},
    {'nomi': 'Panadol', 'miqdori': 0.9}
   ]
}

bemor_json = json.dumps(bemor)

bemor = json.loads(bemor_json)  

print(bemor)



filename = 'bemor.json' 

with open (filename) as f:
  bemor = json.load(f)


print(type(bemor))