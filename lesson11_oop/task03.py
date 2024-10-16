# Шаблон Одиночка, Singleton
# Ещё один вариант использования дандре __new__ — паттерн Singleton. Он
# позволяет создавать лишь один экземпляр класса. Вторая и последующие попытки
# будут возвращать ранее созданый экземпляр.
# 🔥 Внимание! Это не единственный вариант создания паттерна Одиночка в
# Python, а версия через __new__
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')
c = Singleton('Третий')
print(a is c)
print(f'{a.name = }\n{b.name = }\n{c.name = }')
# Защищенная переменная _instance хранит None и при создании первого
# экземпляра получает на него ссылку. Благодаря *args, **kwargs в методе __new__
# аргумент “Первый” проваливается в метод __init__ и попадает в параметр name.
# При создании экземпляра второй раз возвращается его первая версия и у неё
# заменяется свойство name. Переменные a и b ссылаются на один и тот же класс, а
# следовательно их свойство name общее.
