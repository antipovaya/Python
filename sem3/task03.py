"""
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""
from pprint import pprint

my_tuple = (1, 10,
            7.86, 3.14,
            'potato', 'tomato',
            (1, 4, 5), (2,),
            [1, 2, 3], [5],
            {7, 0}, {'hg', 'co'})

my_dict = {}

for item in my_tuple:
    key = type(item)  # .strip('<>').split()[1].strip("'")
    my_dict.setdefault(key, []).append(item)  # dict.setdefault(key[, default]) -> Значение по ключу, либо default
#  key : Ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать.
#  default=None : Значение, которое будет использовано при добавлении нового элемента в словарь.
# Позволяет получить значение из словаря по ключу. Автоматически добавляет элемент словаря, если он отсутствует.

# if key not in my_dict:
# my_dict[key] = []
# elif type(my_dict[key]) == key:
# my_dict[key].append(item)

pprint(my_dict)
