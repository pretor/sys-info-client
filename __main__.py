import psutil
import requests
from time import sleep

cpu = psutil.cpu_percent(interval=1, percpu=True)

payload = {
	'core0': cpu[0],
	'core1': cpu[1],
	'core2': cpu[2],
	'core3': cpu[3],
	'core4': cpu[4],
	'core5': cpu[5],
	'core6': cpu[6],
	'core7': cpu[7]
	}

r = requests.get("http://pretor.pythonanywhere.com/get", params=payload)


