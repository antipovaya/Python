# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
from functools import wraps

logging.basicConfig(filename='log_2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке '
                           '{lineno} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def decor(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Аргументы функции: {args} результат: {result}, имя функции {func.__name__}')

        return result

    return wrapper


@decor
def power(x, y):
    return x ** y


print(power(0, 3))
