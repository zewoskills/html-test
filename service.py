from typing import TypedDict


class User(TypedDict):
	"""Данные пользователя, необходимые для расчёта."""

	age: int
	city: str


def add_user(users: list[User], user: User) -> list[User]:
	"""Добавляет пользователя в список и возвращает обновлённый список."""
	age = user.get("age")
	if isinstance(age, bool) or not isinstance(age, int) or not 0 <= age <= 120:
		raise ValueError("age должен быть целым числом от 0 до 120")

	users.append(user)
	return users


def averageAge(users: list[User], city: str) -> float | None:
	"""Возвращает средний возраст пользователей в указанном городе."""
	ages = [
		user["age"]
		for user in users
		if user.get("city") == city
	]

	if not ages:
		return None

	return sum(ages) / len(ages)


if __name__ == "__main__":
	users: list[User] = []

	add_user(users, {"age": 20, "city": "Moscow"})
	add_user(users, {"age": 30, "city": "Moscow"})
	add_user(users, {"age": 40, "city": "Kazan"})

	print(f"Пользователи: {users}")
	print(f"Средний возраст в Москве: {averageAge(users, 'Moscow')}")
