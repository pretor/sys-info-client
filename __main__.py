import psutil
import requests
import platform
from cpuinfo import cpuinfo
import sensors
import subprocess

def find_vga():
   vga = subprocess.check_output("lspci | grep VGA", shell=True, executable='/bin/bash')
   return vga.split(":")[2]

info = cpuinfo.get_cpu_info()
coresLoadPercentage = psutil.cpu_percent(interval=1, percpu=True)
memoryInfo = psutil.virtual_memory()
cpuTempCores = []
sensors.init()
try:
    for chip in sensors.iter_detected_chips():       
        for feature in chip:
        	if not "Core" in feature.label: continue
            	cpuTempCores.append(feature.get_value()) 
finally:
    sensors.cleanup()

payload = {'cpu[]'      : coresLoadPercentage,
       'cpubrand'       : info['brand'],
       'memorypercent'  : memoryInfo.percent,
       'memorytotal'    : memoryInfo.total / (1024 * 1024),
       'gpuname'        : find_vga(),
       'cputempcores[]' : cpuTempCores,
       'platform'       : platform.system(),
       'platformrelease': platform.release(),
       'platformname'   : platform.node()
}

r = requests.get("http://127.0.0.1:8000/get", params=payload)
