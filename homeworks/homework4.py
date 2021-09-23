"""
Здесь вам нужно реализовать несколько фукнкций.
Для каждой функции есть другая тестовая функция, которая ее проверяет.
Чтобы убедиться, что ваше решение работает запустите ее.
Если функция нвзывется some_function, то тестирующия функция называется test_some_function.
Для проверки просто запустите тестирующую функцию, если после запуска увидели сообщение
Great your solution works! значит все ок!
Если возникла ошибка AssertionError значит решение не работает.
Если вдруг вы нашли ошибку в тестах, пишите в чат мы обсудим.


Краткая заметка. Прочитайте про оператор включения in в коллекциях.
https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
"""


def count_greater_or_equal(numbers, x):
    """
    Функия принимает на вход список чисел numbers и число x.
    Возращает количество элементов списка numbers больше либо равных x.
    """
    pass


def test_count_greater_or_equal():
    assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
    assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
    assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
    assert count_greater_or_equal([0, 1], 2) == 0
    assert count_greater_or_equal([], 2) == 0
    print("Great your solution works!")


def rotate(numbers, n):
    """
    Функия принимает на вход список чисел numbers и число n.
    Применяет к этому списку операцию вращения направо n раз и возвращает его.
    Функция возращает ссылку на исходный список(повернутый нужное кол-во раз), а не создает новый.
    Операция вращения работает так: 0-ой элемент становится 1-м, 1-ый становится вторым, 2-ой третьим и т д.
    Последний становится первый. Примеры смотреть в тестовой функции.
    """
    pass


def test_rotate():
    assert rotate([1, 2, 3], 1) == [3, 1, 2]
    assert rotate([1, 2, 3], 2) == [2, 3, 1]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1], 1) == [1]
    assert rotate([1], 0) == [1]
    assert rotate([], 2) == []
    print("Great your solution works!")


def extend(a, b):
    """
    Даны два списка, надо их обеъединить и получить один список.
    Надо расширить список a элементами из списка b.
    """
    pass


def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")


def is_prime(n):
    """
    Дано число n.
    Если n простое число верните True, иначе False.
    Определние простого числа https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
    """


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(24) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(107) is True
    assert is_prime(19) is True
    print("Great your solution works!")


def merge(a, b):
    """
    Сложная задача. Если самостоятельно решите без Гугла, вы большой молодец.
    Даны два отсортированных по возрастанию списка чисел a, b.
    Надо объединить их в один список, так чтобы результирующий список тоже был отсортирован.
    Нельзя пользоваться  методом sort у списка. Нельзя пользоваться стандартной функцией sorted.
    """
    pass


def test_merge():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], []) == [4, 5, 6]
    assert merge([], [1, 3, 5]) == [1, 3, 5]
    assert merge([], []) == []
    print("Great your solution works!")


def has_substring(s, t):
    """
    Даны две строки s и t.
    Верните True если строка s содержит строку t в качестве подстроки, иначе верните False
    Нельзя пользоваться оператором in или любой другой встроенной опрецией проверки на подстроку.
    Делаем все руками :)
    """


def test_has_substring():
    assert has_substring("some text", "text") is True
    assert has_substring("some text", "some") is True
    assert has_substring("", "text") is False
    assert has_substring("text", "") is True  # любая строка содержит в себе пустую подстроку
    assert has_substring("", "") is True  # даже пустая строка содержит в себе пустую подстроку :)
    print("Great your solution works!")

