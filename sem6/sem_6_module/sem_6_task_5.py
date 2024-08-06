"""
Задание №5
📌 Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
📌 Ключ словаря - загадка, значение - список с отгадками.
📌 Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""

__all__ = ['riddles']

def guess_what(riddle: str, guesses: list, attempts: int = 3) -> int:
    print(f'Отгадайте загадку {riddle}. {'\n'}'
          f'Число попыток: {attempts}.')

    count = 1
    guess = input('Введите отгадку: ').lower()

    while count < attempts:
        if guess in guesses:
            print(f'Угадали! Это {guess}.')
            return count
        print(f'Неверно. Число попыток {attempts - count}.')
        guess = input('Введите отгадку: ').lower()
        count += 1
        if guess in guesses:
            print(f'Угадали! Это {guess}.')
            return count

    print(f'Не угадали!')
    return 0


def riddles():
    riddles_dict = {
        "Что такое всегда перед вами, но вы не можете видеть?": ["будущее", "грядущее"],
        "Что имеет шею, но не имеет головы?": ["Бутылка", "бутылка"],
        "Что можно найти в Москве, но никогда в Париже?": ["Буква \"О\" (в слове Москва)", "О", "о"],
        "Что имеет ноги, но не может ходить?": ["стол", "стул"],
        "Что может лететь, но не имеет крыльев?": ["время"],
    }
    return [guess_what(k, v) for k, v in riddles_dict.items()]


if __name__ == '__main__':
    res = riddles()
    print(res)
