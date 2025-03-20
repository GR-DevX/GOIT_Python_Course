from collections import defaultdict, Counter, deque
from decimal import Decimal
import random

#Генератор трафіку
def traffic_streams():
    ips=["192.168.0.1","10.0.0.2","8.8.8.8","192.168.1.100","172.16.0.5"]
    while True:
        yield (random.choice(ips),Decimal(random.uniform(0.1,5)).quantize(Decimal("0.01")))

if __name__=="__main__":
    #контейнери
    traffic_data = defaultdict(Decimal) # Обсяг трафіку по кодному IP
    request_count = Counter() # кількість запитів від кожного IP
    recent_requests = deque(maxlen=10) # Останні 10 запитів

    #Симуляція моніторингу:
    stream=traffic_streams()
    for _ in range(500):
        ip,data=next(stream)
        print(f"ip:{ip:15}, data:{data} MB") ## DEBUG
        traffic_data[ip]+=data
        request_count[ip]+=1
        recent_requests.append((ip,data))
    print()
    print()
    #вивід
    print(f"Топ IP за кількістю запитів: {request_count.most_common(3)}")
    print()
    print("Обсяг трафіку за IP:")
    for ip,data in traffic_data.items():
        print(f"{ip:15}:{data} MB")

    print()
    print("Останні 10 запитів:")
    for ip,data in recent_requests:
        print(f"{ip:15}:{data}MB")