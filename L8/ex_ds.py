from statistics import mean
from typing import List

# Декоратор для логування
def log_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} -> {result}")
        return result
    return wrapper

# Фільтруємо некоректні показники (None або < 0)
@log_function
def filter_valid(data: List[float]):
    return list(filter(lambda x: x is not None and x >= 0, data))

# Застосовуємо зсув значень (замикання)
def shift_values(shift: float):
    return lambda values: list(map(lambda x: x + shift, values))

# Каррування для перевірки меж значень
def in_range(min_val):
    return lambda max_val: lambda x: min_val <= x <= max_val

# Головна функція
def process_sensor_data(sensor1: List[float], sensor2: List[float]):
    # Фільтруємо дані
    sensor1, sensor2 = map(filter_valid, [sensor1, sensor2])

    # Усереднюємо значення
    avg_values = list(map(mean, zip(sensor1, sensor2)))

    # Додаємо зсув для калібрування
    calibrate = shift_values(-0.5)
    calibrated = calibrate(avg_values)

    # Перевіряємо, чи всі значення в допустимому діапазоні
    is_valid = all(map(in_range(0)(50), calibrated))

    print(f"Final data: {calibrated}")
    print(f"All values in range: {is_valid}")

if __name__=='__main__':
    # Дані з сенсорів
    sensor1_data = [10, 20, None, 35, -5, 50]
    sensor2_data = [15, 25, 30, None, 45, 55]

    process_sensor_data(sensor1_data, sensor2_data)
