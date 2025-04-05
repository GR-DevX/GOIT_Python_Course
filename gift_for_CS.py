# Бувають часи, коли кількість з’єднань обмежена, а хоч якийсь аналіз потрібен. 
# Головне - забезпечити достатньою кількістю вхідних даних. 
# nmap -p 1-1024 -oX scan_results.xml 192.168.1.0/24 (а краще - більше, в рази більше серверів для навчання)


import xml.etree.ElementTree as ET
import random
import numpy as np
import tensorflow as tf

# Функція парсингу XML-скану від nmap
def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    labels = []
    
    for host in root.findall("host"):
        open_ports = set()
        for port in host.findall(".//port"):
            if port.find("state").get("state") == "open":
                open_ports.add(int(port.get("portid")))
        
        # Вибираємо до 10 портів випадково
        input_ports = random.sample(sorted(open_ports), min(len(open_ports), 10))
        output_ports = [1 if p in open_ports else 0 for p in range(1, 1025)]
        
        # Оновлений вхідний вектор (заповнений до 1024 фіч)
        input_vector = [1 if p in input_ports else 0 for p in range(1, 1025)]
        
        data.append(input_vector)
        labels.append(output_ports)
    
    return np.array(data, dtype=np.float32), np.array(labels, dtype=np.float32)

# Завантажуємо навчальні дані з nmap
X_train, y_train = parse_nmap_xml("scan_results.xml")

# Перевіряємо розмірність
print(f"X_train shape: {X_train.shape}")  # Має бути (N, 1024)
print(f"y_train shape: {y_train.shape}")  # Має бути (N, 1024)

# Побудова нейронної мережі
model = tf.keras.Sequential([
    tf.keras.layers.Dense(512, activation="relu", input_shape=(1024,)),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(1024, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Тренуємо модель
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Функція передбачення портів
def predict_ports(scanned_ports):
    input_data = np.array([[1 if p in scanned_ports else 0 for p in range(1, 1025)]], dtype=np.float32)
    
    # Гарантуємо правильну форму перед передбаченням
    if len(input_data.shape) == 1:
        input_data = input_data.reshape(1, 1024)
    
    predicted_ports = model.predict(input_data)[0]
    return [p+1 for p in range(1024) if predicted_ports[p] > 0.5]

# l33tsp34k
leet_map = {
    "http": "h7tp",
    "ssh": "5sH",
    "ftp": "f7p",
    "telnet": "73lN37",
    "smtp": "5mT9",
    "dns": "dn5",
    "pop3": "p0P3",
    "imap": "1m4P",
    "https": "h77p5",
}

# Функція перетворення назв сервісів в l33tsp34k
def leetspeak(service):
    return leet_map.get(service, service)

# Приклад розбору відкритих портів
def parse_ports_with_leet(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    ports = {}

    for host in root.findall("host"):
        ip = host.find("address").get("addr")
        ports[ip] = []
        
        for port in host.findall(".//port"):
            if port.find("state").get("state") == "open":
                port_id = port.get("portid")
                service = port.find("service")
                service_name = service.get("name") if service is not None else "unknown"
                
                ports[ip].append(f"{port_id} ({leetspeak(service_name)})")
    
    return ports

# Використання
leet_ports = parse_ports_with_leet("scan_results.xml")
for ip, ports in leet_ports.items():
    print(f"{ip}: {', '.join(ports)}")

target_ip = "192.168.0.1"

# Проскановані 10 портів
scanned = {22, 80, 443, 3306, 53, 25, 8080, 110, 995, 993}

# AI прогнозує відкриті порти
predicted = predict_ports(scanned)

print(f"Проскановані порти: {scanned}")
print(f"AI передбачив відкриті порти: {predicted}")
