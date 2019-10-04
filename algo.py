from notify_run import Notify
notify=Notify()


signals={ 'vadapalani':[], 'kodambakkam':[], }
sigtemp=[]
visited={'vadapalani':0,'kodambakkam':0}

def distance(l1,la1,l2,la2):
	response = requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?waypoint0="+l1+"%2C"+la1+"&waypoint1="+l2+"%2C"+la2+"&mode=fastest%3Bcar%3Btraffic%3Aenabled&app_id=VyImePHMbo4wPKeB27eU&app_code=rGRKtUwEInz4uIMNb04mHg&departure=now")
	json_data = json.loads(response.content.decode('utf8'))
	s=str(json_data)
	s=eval(s)

	return int(s['response']['route'][0]['summary']['distance'])

def area(l1,la1):
	response = requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?waypoint0="+l1+"%2C"+la1+"&waypoint1="+l2+"%2C"+la2+"&mode=fastest%3Bcar%3Btraffic%3Aenabled&app_id=VyImePHMbo4wPKeB27eU&app_code=rGRKtUwEInz4uIMNb04mHg&departure=now")
	json_data = json.loads(response.content.decode('utf8'))
	s=str(json_data)
	s=eval(s)

	return (s['response']['route'][0]['summary']['area'])


def calc(loc,dest):
	global signals,sigtemp

	areap = area(loc[0],loc[1])
    if(sigtemp.empty() and visited['areap']==0):
    	sigtemp=signals[areap]
    	visited['areap']=1



	min1=9999999999
	for i in sigtemp:
		if distance(i[0],i[1],dest[0],dest[1])+distance(loc[0],loc[1],i[0],i[1])<min1:
			min1=distance(i[0],i[1],dest[0],dest[1])+distance(loc[0],loc[1],i[0],i[1])
			closesl=i[0]
			closesla=i[1]

	reald=distance(loc[0],loc[1],dest[0],dest[1])
	if(reald<min1):


	else:
		signaldist=distance(loc[0],closel,closela)
		notify.send()


	signals.remove([closel.closela])






    








