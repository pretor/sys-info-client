import psutil
import requests

coresLoadPercentage = psutil.cpu_percent(interval=1, percpu=True)

payload = {}

for x in range(0,len(coresLoadPercentage)):	
	payload['core'+str(x)] = coresLoadPercentage[x]

r = requests.get("http://pretor.pythonanywhere.com/get", params=payload)


