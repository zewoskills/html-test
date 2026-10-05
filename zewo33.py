from typing import Any


def calculate_discount(
    user_type: str,
    total_amount: float,
    is_first_order: bool,
) -> float:
    if user_type not in {"premium", "standard"}:
        return total_amount

    if user_type == "premium" and total_amount > 100:
        discount = 0.25 if is_first_order else 0.20
    elif user_type == "premium":
        discount = 0.10
    elif total_amount > 100:
        discount = 0.10
    else:
        discount = 0.05

    return total_amount * (1 - discount)




def get_active_user_emails(
    users_list: list[dict[str, Any]],
) -> list[str]:
    return [
        email.lower()
        for user in users_list
        if user.get("is_active") is True
        if (email := user.get("email"))
    ]










 