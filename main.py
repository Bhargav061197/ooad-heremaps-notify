
from notify_run import Notify
notify=Notify()

import requests
from flask import Flask,request,render_template

import json

visited={"vadapalani purvika signal":0,"vadapalani HDFC signal":0,"arumbakkam metro signal":0}

def signals(loc):
	l={"vadapalani purvika signal":[13.0502556,80.2123292],"vadapalani HDFC signal":[13.0525288,80.212219],"arumbakkam metro signal":[13.0568557,80.2128307]}
	global visited
	dist=9999999990
	approach=""
	for i in l.keys():
		l1=str(l[i][0])
		la1=str(l[i][1])
		count=0
		if distance(l1,la1,str(loc[0]),str(loc[1]))<dist and visited[i]==0 and count<3:
			count+=1
			dist=distance(l1,la1,str(loc[0]),str(loc[1]))
			visited[i]=1
			approach=i
	if(approach!=""):

		l1 = str(l[approach][0])
		la1 = str(l[approach][1])
		return ("Ambulance approaching "+approach+". Vechile is "+str(distance(l1,la1,str(loc[0]),str(loc[1])))+" metres away.")
	else:
		return ""





def distance(l1,la1,l2,la2):
	response = requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?waypoint0="+l1+"%2C"+la1+"&waypoint1="+l2+"%2C"+la2+"&mode=fastest%3Bcar%3Btraffic%3Aenabled&app_id=VyImePHMbo4wPKeB27eU&app_code=rGRKtUwEInz4uIMNb04mHg&departure=now")
	json_data = json.loads(response.content.decode('utf8'))
	s=str(json_data)
	s=eval(s)

	return int(s['response']['route'][0]['summary']['distance'])

def location(loc):

	response=requests.get("https://geoipify.whoisxmlapi.com/api/v1?apiKey=at_G7xixY8c2KOjfJTFGtui0yXulCccb&ipAdress="+loc)
	json_data = json.loads(response.content.decode('utf8'))
	s = str(json_data)
	s = eval(s)
	return [str(s['location']['lat']),str(s['location']['lng'])]






app = Flask(__name__)



@app.route("/startj", methods=['GET','POST'])
def startj():
	if request.method == 'POST':
		notify.send("ambulance started")
		s = str(request.remote_addr)
		loc = location(s)
		count = 0
		while (distance(loc[0], loc[1], "13.0509767", "80.2126403") > 10) and count < 2:
			count += 1;
			s = str(request.remote_addr)
			loc = location(s)
			noti = signals(loc)
			if (noti != ""):
				notify.send(noti)

		fit = "https://image.maps.api.here.com/mia/1.6/mapview?app_id=VyImePHMbo4wPKeB27eU&app_code=rGRKtUwEInz4uIMNb04mHg&c=" + \
			  loc[0] + "," + loc[1] + "&z=16"
		return render_template("start.html", cor=fit)

	s = str(request.remote_addr)
	loc = location(s)
	fit = "https://image.maps.api.here.com/mia/1.6/mapview?app_id=VyImePHMbo4wPKeB27eU&app_code=rGRKtUwEInz4uIMNb04mHg&c=" + \
		  loc[0] + "," + loc[1] + "&z=16"
	return render_template("start.html", cor=fit)


if __name__=="__main__":
	app.run(host='0.0.0.0')