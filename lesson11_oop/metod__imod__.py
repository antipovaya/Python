# In place методы
# In place методы используются при короткой записи математического символа
# слитно со знаком равенства: a += b. Такая запись подразумевает внесение
# изменений в исходный объект, а не возврат нового экземпляра. Возвращать надо
# самого себя — self.
# Вычисление процентов вместо нахождения
# остатка от деления, __imod__
# Создадим простой класс Money, который будет увеличивать значение на указанный
# процент при записи Money %= float | int

from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)
# Для точности вычислений используется класс Decimal. Поэтому при увеличении на
# указанный процент используем дополнительное обёртывание правого значение в
# Decimal.
# 🔥 Важно! Не забывайте return self при работе с in place дандер методами.


# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
class MyClass:

    def __init__(self, data):
        self.data = data

    def __and__(self, other):
        return MyClass(self.data + other.data)

    def __str__(self):
        return str(self.data)


a = MyClass([1, 2, 3, 4, 5])
b = MyClass([2, 4, 6, 8, 10])
print(a & b)
