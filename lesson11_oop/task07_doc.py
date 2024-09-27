# 2. Строка документации
# Как и при создании функции, при создании классов принято оставлять
# документацию к нему. Для этого достаточно использовать многострочный
# комментарий сразу после определения класса — строки class ClassName:
# Посмотрите на пример
class User:
    """A User training class for demonstrating class
    documentation.
    Shows the operation of the help(cls) and the dander method
    __doc__"""
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print('Справка класса User ниже', '*' * 50)
help(User)
print('Справка экземпляра u_1 ниже', '*' * 50)
help(u_1)
# После заголовка класса оставили пару строк описания. Также добавлена строка
# документации для метода __init__. Далее вызываем справку для класс User и для
# его экземпляра. С первого взгляда они похожи и выводят куда больше информации.
# Помимо оставленной документации help собирает информацию о методах класса.
# Выводит первую строку метода и строку документации метода, если она задана
# многострочным комментарием.
# Отличие справки для класса и экземпляра лишь в первой строке. Сравните:
# Help on class User in module __main__:
# 10
# Help on User in module __main__ object:



# Хранение документации в __doc__
# Любая многострочная строка после заголовка класса и метода автоматичские
# сохраняется в дандер переменную __doc__. Помимо вызова справки через
# функцию help можно прочитать отдельный мнострочник напрямую обратившись к
# переменной.
class User2:
    """A User2 training class for demonstrating class
    documentation.
    Shows the operation of the help(cls) and the dander method
    __doc__"""
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
        print(f'Создал {self.name = }')
    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_11 = User2('Спенглер')
print(f'Документация класса: {User2.__doc__ = }')
print(f'Документация экземпляра: {u_11.__doc__ = }')
print(f'Документация метода: {u_11.simple_method.__doc__}')
# Как и в случае с help обращение через класс или через экземпляр не даёт разницы