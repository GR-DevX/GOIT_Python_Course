# продажі потоком:
# Категорія
# Сума
# Кількість

# 1. Обробка даних на льоту
# 2. Визначити найпопулярніші категорії
# 3. Агрегувати продажі по категоріях
# 4. Зберігаємо останні 5 операцій
# 5. Точні фін підрахунки

from collections import defaultdict, Counter, deque
from decimal import Decimal
import random

def sales_stream():
    categories=['Electronics','Clothing','Books','Toys','Home']
    while True:
        yield{
            'category':random.choice(categories),
            'amount':Decimal(random.uniform(5,500)).quantize(Decimal('0.01')),
            'quantity':random.randint(1,10),
        }

if __name__=='__main__':
    stream=sales_stream()
    
    total_sales=defaultdict(Decimal)  # Загальна сума коштів по категоріях
    quantity_sold=Counter() # кількість проданих одиниць по категоріях
    recent_sales=deque(maxlen=5) # останні 5 транзакцій

    # Обробляємо  по 30
    for _ in range(30):
        sale=next(stream)
        print(sale) # DEBUG
        category, amount, quantity = sale['category'], sale['amount'], sale['quantity']
        total_sales[category]+=amount #DECIMAL - precision
        quantity_sold[category]+=quantity # int
        recent_sales.append(sale) # заносимо операцію в історію
    print()
    print()
    #Виводимо:
    print(f"Три найпопулярніші категорії: {quantity_sold.most_common(3)}")
    print()
    print("Загальний прибуток по категоріях:")
    for cat,total in total_sales.items():
        print(f"{cat:10}: ${total}")
    print()
    print("5 останніх транзакцій:")
    for sale in recent_sales:
        print(f"{sale['category']:15}|{sale['quantity']:13}шт|${sale['amount']}")
