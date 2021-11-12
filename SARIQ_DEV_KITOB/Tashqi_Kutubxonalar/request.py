
import requests
from pprint import pprint

manzil= "https://github.com/"
r = requests.get(manzil)
pprint(r.text)