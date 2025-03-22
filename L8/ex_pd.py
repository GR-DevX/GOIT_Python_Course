from typing import List, Dict

# Декоратор для логування запитів
def log_request(func):
    def wrapper(user, *args, **kwargs):
        print(f"User {user['name']} ({user['role']}) is accessing data")
        return func(user, *args, **kwargs)
    return wrapper

# Фільтр дозволених ендпоінтів
def filter_allowed_endpoints(role: str, endpoints: List[str]):
    return list(filter(lambda ep: ep.startswith(f"/{role}"), endpoints))

# Каррування для перевірки дозволу на дію
def has_permission(required_role):
    return lambda user: user["role"] == required_role

# Замикання для форматування JSON-відповідей
def json_response_formatter(fields: List[str]):
    return lambda data: [{key: item[key] for key in fields if key in item} for item in data]

# Головна функція
@log_request
def handle_request(user: Dict, endpoints: List[str], data: List[Dict]):
    # Вибираємо дозволені ендпоінти
    allowed_endpoints = filter_allowed_endpoints(user["role"], endpoints)

    # Перевіряємо, чи має користувач доступ
    is_admin = has_permission("admin")
    access_granted = any(map(is_admin, [user]))

    # Форматуємо відповідь
    format_json = json_response_formatter(["id", "name"])
    formatted_data = format_json(data)

    print(f"Allowed endpoints: {allowed_endpoints}")
    print(f"Access granted: {access_granted}")
    print(f"Formatted data: {formatted_data}")

# Дані для запиту
user_info = {"name": "Alice", "role": "user"}
available_endpoints = ["/admin/settings", "/user/profile", "/user/orders", "/public/info"]
database_records = [{"id": 1, "name": "Item A", "price": 100}, {"id": 2, "name": "Item B", "price": 200}]

handle_request(user_info, available_endpoints, database_records)
