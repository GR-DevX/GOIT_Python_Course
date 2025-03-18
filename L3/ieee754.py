import struct

def float_to_ieee754(num):
    print(f"Вхідне число: {num}")
    
    # Крок 1: Отримуємо двійкове представлення IEEE 754 через struct
    packed = struct.pack('>f', num)  # '>f' означає big-endian float
    bits = ''.join(f'{b:08b}' for b in packed)  # Отримуємо бітове представлення
    
    # Крок 2: Виділяємо частини
    sign = bits[0]  # Знак
    exponent = bits[1:9]  # Експонента
    mantissa = bits[9:]  # Мантиса
    
    # Крок 3: Розрахунок значень
    sign_value = (-1) ** int(sign)  # Обчислюємо знак
    exponent_value = int(exponent, 2) - 127  # Віднімаємо bias
    mantissa_value = 1 + sum(int(mantissa[i]) * 2**-(i + 1) for i in range(len(mantissa)))  # Мантиса з прихованою 1
    
    # Вивід проміжних результатів
    print(f"Бітовий код: {bits}")
    print(f"Знак: {sign} ({'-' if sign_value == -1 else '+'})")
    print(f"Експонента: {exponent} (десяткове значення {int(exponent, 2)}), справжня: 2^{exponent_value}")
    print(f"Мантиса: {mantissa} (десяткове значення {mantissa_value})")
    
    # Формула обчислення
    float_value = sign_value * mantissa_value * (2 ** exponent_value)
    print(f"Обчислене число: {float_value}")
    
    return bits

# Тестові значення
float_to_ieee754(3e5)
print("-" * 50)
float_to_ieee754(3e-5)
print("-" * 50)
float_to_ieee754(-3e5)
print("-" * 50)
float_to_ieee754(-3e-5)
print("-" * 50)
float_to_ieee754(-(128+8+4+2+1))
float_to_ieee754((128+8+4+2+1)*2)