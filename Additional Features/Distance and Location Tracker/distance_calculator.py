from math import cos, asin, sqrt, pi, sin, atan2
from bs4 import BeautifulSoup
import requests, json
import pyttsx3

engine = pyttsx3.init()



def distance(lat1, lon1, lat2, lon2):
	R = 6371
	p = pi/180
	dLat = (lat2-lat1)*p
	dLon = (lon2-lon1)*p
	a = sin(dLat/2) * sin(dLat/2) +cos((lat1)*p) * cos(p*(lat2)) * sin(dLon/2) * sin(dLon/2)
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	d = R * c # Distance in km
	engine.say("Distance between you and target is:"+str(d)+"kilometres")

def guest_tracker(my_ip, other_ip):
	url = "https://ipinfo.io/"+str(my_ip)+"/json"
	response = requests.get(url, timeout=20000)
	content = BeautifulSoup(response.content,"html.parser")
	c = [x.strip() for x in str(content).split('\n')]
	location = []
	for i in c:
		location.append([x.strip() for x in str(i).split(':')])
	#print(location)
	for i in range(1,(len(location)-1)):
		l = location[i]
		for j in range(0,2):
			string = l[j]
			location[i][j]=string.replace("\"","")
			#location[i][j]=location[i][j].replace(",","")
	del location[0]
	del location[(len(location))-1]
	loc = {}
	for i in location:
		loc.update({i[0]:i[(len(i))-1]})
	coord = loc['loc'].split(",")
	my_lat = coord[0]
	my_long = coord[1]
	city = loc['city']
	engine.say("Your current location is in "+str(city))

	url = "https://ipinfo.io/"+str(other_ip)+"/json"
	response = requests.get(url, timeout=20000)
	content = BeautifulSoup(response.content,"html.parser")
	c = [x.strip() for x in str(content).split('\n')]
	location = []
	for i in c:
		location.append([x.strip() for x in str(i).split(':')])
	#print(location)
	for i in range(1,(len(location)-1)):
		l = location[i]
		for j in range(0,2):
			string = l[j]
			location[i][j]=string.replace("\"","")
			#location[i][j]=location[i][j].replace(",","")
	del location[0]
	del location[(len(location))-1]
	loc = {}
	for i in location:
		loc.update({i[0]:i[(len(i))-1]})
	coord = loc['loc'].split(",")
	other_lat = coord[0]
	other_long = coord[1]
	city = loc['city']
	engine.say("Target current location is in "+str(city))

	distance(float(my_lat),float(my_long),float(other_lat),float(other_long))

my_ip="<ip?"
home_ip = "<ip>"

guest_tracker(my_ip,home_ip)
engine.runAndWait()
