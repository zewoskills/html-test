CHILD_AGE_LIMIT = 12
SENIOR_AGE_LIMIT = 60
WEEKEND_DAYS = (6, 7)
GLASSES_3D_SURCHARGE = 150

WEEKDAY_PRICES = {"child": 150, "senior": 200, "adult": 300}
WEEKEND_PRICES = {"child": 250, "senior": 300, "adult": 400}


class InvalidTicketDataError(ValueError):
    pass


def _get_age_category(age: int) -> str:
    if age < CHILD_AGE_LIMIT:
        return "child"
    if age >= SENIOR_AGE_LIMIT:
        return "senior"
    return "adult"


def calculate_ticket_price(age: int, day_of_week: int, has_3d_glasses: bool) -> float:
    if age < 0 or not (1 <= day_of_week <= 7):
        raise InvalidTicketDataError(
            f"age должен быть >= 0, day_of_week в диапазоне 1..7 "
            f"(получено age={age}, day_of_week={day_of_week})"
        )

    prices = WEEKEND_PRICES if day_of_week in WEEKEND_DAYS else WEEKDAY_PRICES
    price = prices[_get_age_category(age)]

    if has_3d_glasses:
        price += GLASSES_3D_SURCHARGE

    return price


def demo_ticket_prices() -> None:
    print(calculate_ticket_price(10, 6, True))   # 250+150=400
    print(calculate_ticket_price(10, 2, False))  # 150
    print(calculate_ticket_price(65, 7, True))   # 300+150=450
    print(calculate_ticket_price(65, 3, False))  # 200
    print(calculate_ticket_price(30, 6, False))  # 400
    print(calculate_ticket_price(30, 2, True))   # 300+150=450

    try:
        calculate_ticket_price(-1, 9, False)
    except InvalidTicketDataError as e:
        print('OK:', e)


if __name__ == "__main__":
    demo_ticket_prices()