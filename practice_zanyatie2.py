"""
Модуль интернет-магазина: расчёт доставки, скидок и оформление заказа.

Задание: найдите не менее 5 code smells из шести (Long Method, Duplicate
Code, Magic Number, Long Parameter List, Dead Code, God Object).
Для каждого укажите номер строки, название смэлла и обоснование в 1 предложение.
"""

import logging


def get_shipping_cost_eu(weight):
    return weight * 2.5 + 5


def get_shipping_cost_us(weight):
    return weight * 2.5 + 5


def apply_discount(price):
    return price * 0.9
    print("discount applied")  # эта строка никогда не выполнится


# def old_calculate_total(items):
#     total = 0
#     for i in items:
#         total += i["price"]
#     return total * 0.8


def register_customer(name, email, age, city, street, house, phone, is_admin, is_active):
    customer = {
        "name": name,
        "email": email,
        "age": age,
        "city": city,
        "street": street,
        "house": house,
        "phone": phone,
        "is_admin": is_admin,
        "is_active": is_active,
    }
    return customer


def checkout(cart, customer_email, customer_name, is_vip, weight):
    # валидация
    if not cart:
        raise ValueError("empty cart")
    if customer_email is None:
        raise ValueError("no email")

    # расчёт суммы товаров
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]

    # применяем порог бесплатной доставки
    if total > 1000:
        shipping = 0
    else:
        shipping = get_shipping_cost_eu(weight)

    total += shipping

    # скидка для VIP
    if is_vip:
        total = total * 0.9

    # налог
    total = total * 1.2

    # "сохранение" в базу
    print(f"Saving order for {customer_name}, total={total}")

    # уведомление
    print(f"Отправка письма на {customer_email}: ваш заказ на сумму {total}")

    return total


class ShopManager:
    """Отвечает за всё сразу: базу, логи, расчёты и рассылку писем."""

    def __init__(self):
        self.logger = logging.getLogger("shop")

    def connect_to_db(self):
        print("connecting to db...")

    def calculate_tax(self, price):
        return price * 1.2

    def send_email(self, to, text):
        print(f"email to {to}: {text}")

    def log_error(self, message):
        self.logger.error(message)

    def render_receipt_html(self, order):
        return f"<html><body>Order total: {order['total']}</body></html>"

    def parse_config_file(self, path):
        with open(path) as f:
            return f.read()


if __name__ == "__main__":
    cart = [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]
    checkout(cart, "test@example.com", "Иван", True, 3)
