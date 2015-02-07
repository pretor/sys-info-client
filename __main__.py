import psutil
import requests
import platform
from cpuinfo import cpuinfo

info = cpuinfo.get_cpu_info()
coresLoadPercentage = psutil.cpu_percent(interval=1, percpu=True)
memoryInfo = psutil.virtual_memory()

payload = {}

for x in range(0,len(coresLoadPercentage)):	
	payload['core'+str(x)] = coresLoadPercentage[x]

tes = {'cpu[]'    : coresLoadPercentage,
       'cpubrand' : info['brand'],
       'memorypercent'   : memoryInfo.percent
}

r = requests.get("http://127.0.0.1:8000/get", params=tes)