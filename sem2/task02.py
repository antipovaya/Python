"""
Задание №2
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.

"""

data = [1, 4.2, 'str', False, (1, 2), None, 1, 1]

for i, el in enumerate(data, 1): #  Возвращает объект-перечисление, отдающий пары счётчик-элемент для элементов указанной последовательности.
    print(f"Порядковый номер: {i}, значение: {el}, адрес в памяти: {id(el)}, размер в памяти: {el.__sizeof__()}, "
          f"хеш объекта: {hash(el)}, "
          f"{'целое число' if type(el) == int else 'не целое число'}, "
          f"{'строка' if isinstance(el, str) else 'не строка'}")

