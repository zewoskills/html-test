"""Корзина покупок с базовыми операциями над товарами."""


class ShoppingCart:
    """Хранит товары, их цены и количество, а также умеет считать итоговую сумму."""

    def __init__(self):
        """Создаёт пустую корзину."""
        self.items = {}

    def addItem(self, name, price, qty):
        """Добавляет товар в корзину или увеличивает количество, если товар уже есть."""
        # Проверяем, что название товара передано корректно.
        if not name or not isinstance(name, str):
            raise ValueError("Название товара должно быть непустой строкой.")

        # Проверяем, что цена товара неотрицательная.
        if price < 0:
            raise ValueError("Цена товара не может быть отрицательной.")

        # Проверяем, что количество товара больше нуля.
        if qty <= 0:
            raise ValueError("Количество товара должно быть больше нуля.")

        # Если товар уже есть в корзине, просто увеличиваем количество.
        if name in self.items:
            self.items[name]["qty"] += qty
            return

        # Если товара ещё нет, добавляем новую запись в корзину.
        self.items[name] = {"price": price, "qty": qty}

    def removeItem(self, name):
        """Удаляет товар из корзины по названию."""
        # Проверяем наличие товара перед удалением.
        if name not in self.items:
            raise KeyError(f"Товар '{name}' отсутствует в корзине.")

        # Удаляем товар из словаря.
        del self.items[name]

    def updateQuantity(self, name, qty):
        """Изменяет количество товара в корзине."""
        # Проверяем, что товар существует в корзине.
        if name not in self.items:
            raise KeyError(f"Товар '{name}' отсутствует в корзине.")

        # Количество должно быть больше нуля, иначе товар лучше удалить.
        if qty <= 0:
            raise ValueError("Количество товара должно быть больше нуля.")

        # Обновляем количество товара.
        self.items[name]["qty"] = qty

    def getTotal(self):
        """Возвращает общую стоимость всех товаров в корзине."""
        # Проходим по всем товарам и суммируем цену умноженную на количество.
        total = 0
        for item in self.items.values():
            total += item["price"] * item["qty"]

        return total

    def clearCart(self):
        """Полностью очищает корзину."""
        # Очищаем словарь с товарами.
        self.items.clear()


if __name__ == "__main__":
    cart = ShoppingCart()

    # Добавляем товар в корзину.
    cart.addItem("Яблоки", 50, 3)
    cart.addItem("Хлеб", 30, 2)

    # Добавляем ещё один товар с тем же названием.
    cart.addItem("Яблоки", 50, 2)

    # Меняем количество товара.
    cart.updateQuantity("Хлеб", 5)

    # Получаем итоговую сумму.
    total = cart.getTotal()

    # Удаляем товар.
    cart.removeItem("Яблоки")

    # Очищаем корзину.
    cart.clearCart()


cart = ShoppingCart()
cart.addItem("Хлеб", 50, 2)
cart.addItem("Молоко", 80, 1)
print(cart.getTotal())
cart.updateQuantity("Хлеб", 5)
print(cart.getTotal())
cart.removeItem("Молоко")
print(cart.getTotal())
cart.clearCart()
print(cart.getTotal()) 