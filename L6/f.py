import logger_module as log
#print(log.error('Some warning text'))
import time,psutil

def monitor_resources(interval=1):
    print()
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        if cpu>70 or ram>70:
            print(log.warn(f'HIGH LOAD! CPU:{cpu}%, RAM:{ram}%'),end='')
        else:
            print(log.info(f'CPU:{cpu}%, RAM:{ram}%'),' '*15,end='')
        print('\r',end='')
        time.sleep(interval)


if __name__=='__main__':
    try:
        monitor_resources()
    except KeyboardInterrupt:
        print()
        print('Bye...')