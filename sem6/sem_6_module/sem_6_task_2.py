"""
Задание №2
📌 Создайте модуль с функцией внутри.
📌 Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
📌 Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
📌 Функция выводит подсказки “больше” и “меньше”.
📌 Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""

from random import randint

__all__ = ['guess_number']

def guess_number(low_limit, upper_limit, attempts):
    print(f'Угадайте число в диапазоне между {low_limit} и {upper_limit}. '
          f'У вас {attempts} попыток.')

    number_to_guess = randint(low_limit, upper_limit)
    print(number_to_guess) # закомментировать
    count = 0
    number = int(input('Введите целое число: '))

    while count < attempts - 1:
        if number == number_to_guess:
            print(f'Угадали! Это {number_to_guess}.')
            return True
        else:
            count += 1
            print(f'Неверно. У вас осталось {attempts - count} попыток')
            if number < number_to_guess:
                print('больше')
            else:
                print('меньше')
            number = int(input('Введите целое число: '))
    else:
        return False


low_limit, upper_limit = 2, 15
attempts = (low_limit + upper_limit) // 4

if __name__ == '__main__':
    res = guess_number(low_limit, upper_limit, attempts)
    print(res)
