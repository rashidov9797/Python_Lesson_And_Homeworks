import datetime as dt


bugun = dt.datetime.today()


futbol = dt.datetime(2021,3,10,23,45,00)

farq = futbol - bugun

sekund = farq.seconds
minutlar = int(sekund/60)

soatlar = int(minutlar/60)

print(f"Futbol boshlanishiga {sekund} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")