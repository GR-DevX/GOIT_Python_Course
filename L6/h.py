import os, time, subprocess
from logger_module import *

def check_port_scans():
    result = subprocess.run(['netstat',"-ant"],capture_output=True,text=True)
    suspicious_ips=[]
    for line in result.stdout.split("\n"):
        if "SYN_RECV" in line:
            ip=line.split()[4].split[':'][0]
            if ip not in suspicious_ips:
                suspicious_ips.append(ip)
                print(warn(f'Suspicious connection found from ip: {ip}'))

def monitor_failed_logins():
    if os.path.exists("/var/log/auth.log"):
        with open("/var/log/auth.log",'r' )  as f:
            for line in f.readlines()[-10:]:
                if "Failed" in line:
                    print(error(f"Failed logging attempt: {line.strip()}"))

if __name__=="__main__":
    print(info("Running our mimimal IDS..."))
    while True:
        check_port_scans()
        # monitor_failed_logins()
        #time.sleep(1)

