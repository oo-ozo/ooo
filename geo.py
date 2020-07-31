import requests
import style
from os import *

print(style.square("ip tracker", "red"))
print(" ")
print(style.line())
print(style.color("green"))
p = input("ip :")

system("clear")
print(style.color("green"))

print(style.big("made by"))
print(style.big("Tricker"))

i = str(p)

ip = requests.get("https://ipinfo.io/"+i+"/ip")
city = requests.get("https://ipinfo.io/"+i+"/city")
region = requests.get("https://ipinfo.io/"+i+"/region")
country = requests.get("https://ipinfo.io/"+i+"/country")
loc = requests.get("https://ipinfo.io/"+i+"/loc")
time = requests.get("https://ipinfo.io/"+i+"/timezone")

print(style.color("blue"))
print("ip :",ip.text)
print("city :",city.text)
print("region :", region.text)
print("country :",country.text)
print("loc :",loc.text)
print("timezone :",time.text)

