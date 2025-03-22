from typing import List
import re

# Декоратор для логування
def log_attempts(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} detected {len(result)} suspicious entries")
        return result
    return wrapper

# Фільтр підозрілих IP-адрес
@log_attempts
def filter_suspicious(ips: List[str]):
    return list(filter(lambda ip: any(part == "666" for part in ip.split(".")), ips))

# Каррування для перевірки портів
def check_ports(allowed_ports):
    return lambda attempts: list(filter(lambda x: int(x.split(":")[1]) not in allowed_ports, attempts))

# Замикання для приховування реальних IP перед логуванням
def anonymize_logs(mask: str):
    def anonymizer(logs: List[str]):
        return list(map(lambda log: re.sub(r"\d+\.\d+\.\d+\.\d+", mask, log), logs))
    return anonymizer

# Головна функція
def analyze_logs(ip_logs: List[str], port_attempts: List[str]):
    # Фільтруємо підозрілі IP
    bad_ips = filter_suspicious(ip_logs)

    # Фільтруємо спроби доступу до закритих портів
    check_blocked_ports = check_ports([80, 443, 22])
    blocked_attempts = check_blocked_ports(port_attempts)

    # Анонімізуємо логи перед виведенням
    anonymize = anonymize_logs("XXX.XXX.XXX.XXX")
    safe_logs = anonymize(ip_logs)

    print(f"Safe logs: {safe_logs}")
    print(f"Blocked port attempts: {blocked_attempts}")

# Вхідні дані
ip_entries = ["192.168.1.1", "10.0.0.1", "123.666.45.32", "172.16.0.5", "8.8.8.8"]
port_scans = ["192.168.1.1:22", "10.0.0.1:3389", "123.666.45.32:8080", "172.16.0.5:53"]

analyze_logs(ip_entries, port_scans)
