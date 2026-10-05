"""
Модуль обработки заказов интернет-магазина (учебный "легаси"-фрагмент).

Задание: составьте письменный отчёт — список из не менее 8 проблем,
для каждой укажите приоритет (критично / важно / незначительно)
и обоснование в 1-2 предложения. В конце дайте общую оценку:
на сколько часов рефакторинга тянет этот модуль.
"""

import datetime

warehouse_stock = {
    "sku-1": 5,
    "sku-2": 0,
    "sku-3": 12,
}

customer_data = {}


def get_item_price(sku):
    prices = {
        "sku-1": 1200,
        "sku-2": 350,
        "sku-3": 899,
    }
    return prices.get(sku, 0)


def check_stock(sku, qty):
    try:
        available = warehouse_stock[sku]
        return available >= qty
    except:
        pass


def reserve_stock(sku, qty):
    try:
        warehouse_stock[sku] -= qty
    except:
        pass


def process_order(order_id, items, customer_email, customer_name, discount, is_vip, region, promo_code, notes):
    itog = 0
    total_summa = 0
    problems_log = []

    for it in items:
        sku = it["sku"]
        qty = it["qty"]

        if check_stock(sku, qty):
            reserve_stock(sku, qty)
        else:
            problems_log.append(f"{sku} not available")
            # заказ продолжает оформляться, даже если товара нет на складе

        price = get_item_price(sku)

        if region == "EU":
            if price > 500:
                if qty > 1:
                    if is_vip:
                        line_total = price * qty * 0.95
                    else:
                        line_total = price * qty * 0.97
                else:
                    line_total = price * qty
            else:
                line_total = price * qty
        elif region == "US":
            if price > 500:
                if qty > 1:
                    if is_vip:
                        line_total = price * qty * 0.93
                    else:
                        line_total = price * qty * 0.96
                else:
                    line_total = price * qty
            else:
                line_total = price * qty
        else:
            line_total = price * qty

        itog += line_total

    total_summa = itog

    # начисление скидки
    if discount > 0.1 or is_vip:
        total_summa = total_summa * (1 - discount)

    # налог
    if region == "EU":
        total_summa = total_summa * 1.2
    elif region == "US":
        total_summa = total_summa * 1.08

    # доставка
    if total_summa > 1000:
        shipping_cost = 0
    else:
        shipping_cost = 15

    total_summa += shipping_cost

    order_record = {
        "id": order_id,
        "customer": customer_name,
        "email": customer_email,
        "total": total_summa,
        "date": datetime.datetime.now(),
        "notes": notes,
        "promo": promo_code,
    }

    customer_data[customer_email] = order_record

    print(f"Order {order_id} saved, total={total_summa}")

    if problems_log:
        print("Проблемы при оформлении:", problems_log)

    print(f"Sending confirmation email to {customer_email}")

    return total_summa


def recalculate_total(items, region, is_vip):
    # дублирует часть логики расчёта суммы из process_order
    total = 0
    for it in items:
        price = get_item_price(it["sku"])
        qty = it["qty"]
        if region == "EU" and is_vip and price > 500 and qty > 1:
            total += price * qty * 0.95
        else:
            total += price * qty
    return total


def cancel_order(customer_email):
    if customer_email in customer_data:
        del customer_data[customer_email]
        print("Order cancelled")


if __name__ == "__main__":
    order_items = [{"sku": "sku-1", "qty": 2}, {"sku": "sku-2", "qty": 1}]
    process_order(
        "ORD-001",
        order_items,
        "client@example.com",
        "Пётр",
        0.05,
        False,
        "EU",
        None,
        "",
    )
