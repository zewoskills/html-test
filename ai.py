def count_grades(grades):
    """
    Принимает список оценок и возвращает словарь с их количеством.
    """
    result = {}
    for grade in grades:
        if grade in result:
            result[grade] += 1
        else:
            result[grade] = 1
    return result

if __name__ == "__main__":
    example = [5, 4, 5, 3]
    print(f"Вход: {example}")
    print(f"Выход: {count_grades(example)}")
