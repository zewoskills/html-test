# lamp = 'green'
# match lamp:
#     case 'green':
#         print('go')
#         case 'yellow':
#         print('остановитесь')
#         case 'red':
#         print('стоп')

# number = 1
# match number:
#     case 1:
#         print('one')
#     case 2:
#         print('two')
#     case 3:
#         print('three')
#     case _:
#         print('other')


# age = 20
# match age:
#     case age if age < 13:
#         print('child')
#     case age if age < 18:
#         print('teen')
#     case age if age >= 18:
#         print('adult')


# number = 5 
# match number:
#     case 1 | 2 | 3 | 4 | 5:
#         print('цифры до десяти')
#     case 10|20|30:
#         print('десятки')
#     case _:
#         print('другое')

# my_list = [1, 2, 3]
# match my_list:
#     case []:
#         print('this list is empty')
#     case [one_item]:
#         print(f'there is one item: {one_item}')
#     case [first_item, second_item]:
#         print(f'there are two items: {first_item} and {second_item}')
#     case [first_item, *other_item]:
#         print(f'the firts item is {first_item}; there are more items')

# alert = ('platform', 5)
# match alert:
#     case 'urgent':
#         print('this is a urgent alert')
#     case ('platform', 5):
#         print('this is a platform alert with level 5')
#     case ('platform', level) if level > 5:
#         print(f'this is a platform alert with level {level}, which is higher than 5')

# number = 100
# match number:
#     case number if number > 90:
#         print('отлично')
#     case number if number > 80:
#         print('хорошо')
#     case number if number > 70:
#         print('удовлетворительно')
#     case number if number < 70:
#         print('неудолетворительно')


# day = 7
# match day:
#     case 1:
#         print('понедельник, будни.')
#     case 2:
#         print('вторник, будни')
#     case 3:
#         print('среда,будни')
#     case 4:
#         print('четверг, будни')
#     case 5:
#         print('пятница,будни')
#     case 6:
#         print('суббота, выходные')
#     case 7:
#         print('воскресенье, выходные')
#     case _:
#         print('не существует')

# number = 5 
# match number:
#     case 1 | 2 | 3 | 4 | 5:
#         print('цифры до десяти')
#     case 10|20|30:
#         print('десятки')
#     case _:
#         print('другое')
# day = 7
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print('будни')
#     case 6 | 7:
#         print("выходные")
#     case _:
#         print('не правильно')


# def say_hello():
#     print('привет ерлик')
# say_hello()


# def say_hello():
#     return 'привет ерлик'
# print(say_hello())


# def say_hello(name):
#     return f'привет ерлик {name}!'
# name = input('введите имя: ')
# print(say_hello(name))

# def greet(name='гость'):
#     return f'привет {name}'

# print(greet(name ='Maxim'))

# def add(num1, num2):
#     total = num1 + num2
#     return f'{total}'

# total = add(1, 2)
# print(total * 2)

# def show_info(my_list):
#     for i in my_list:
#         return i

# print(show_info([1, 2, 3, 4, 5]))

# def calculate_tax(price: float,rate: float = 0.12) -> float:
#     """
#     лляляляя
#     """
#     return price * rate
# print(calculate_tax(100))

# def celsius_to_fahrenheit(celsius):
#     return celsius * 1.8 + 32

# print(celsius_to_fahrenheit(20))


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(11))


# try:
#     print(undefined_variable)
# except NameError:
#     print("Переменная не определена")

# try:
#     n = int(input("Введите число: "))
# except ValueError:
#     print("Ошибка: введено не число")
# else:
#     print(f"Вы ввели число: {n}")

# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(f"Ошибка: {str(e)}")

# try:
#     n = 2 / 0
# except TypeError:
#     print('Сообщение о TypeError')
# except ZeroDivisionError:
#     print("Сообщение о ZeroDivisionError: Деление на ноль")

# num2 = int(input())
# try:
#     n = num2 / 1
# except (TypeError, ZeroDivisionError):
#     print("Произошла ошибка: typeError или ZeroDivisionError")

# try:
#     n = '1' + 1
# except TypeError:
#     print("Произошла ошибка: TypeError")
# except Exception:
#     print('что то пошло не так')


# try:
#     n = '1' + 1
# except Exception:
#     print('что то пошло не так')
# except TypeError:
#     print("Произошла ошибка: TypeError")

# try:
#     age = int(input("Введите свой возраст: "))
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным")
#     print(f"Вам {age} лет")
# except ValueError as error_message:
#     print(f"Ошибка: {error_message}")


# try:
#     year = int(input("Введите год рождения: "))
#     age = 2026 - year
#     print('Ваш возраст:', age)
#     if age < 0:
#         raise ValueError("Возраст не может быть отрицательным")
# except ValueError:
#     print("Ошибка: введено не число или возраст отрицательный")

# try: 
#     peoples = int(input('Между сколькими людьми разделить яблоки?: ')) 
#     apples = int(input('Сколько яблок?: '))
#     n = apples / peoples
#     print(f'Каждому достанется по {n} яблок')
# except ZeroDivisionError:
#     print('Ошибка: на ноль делить нельзя')     

