"""
Здесь вам нужно реализовать несколько фукнкций.
Для каждой функции есть другая тестовая функция, которая ее проверяет.
Чтобы убедиться, что ваше решение работает запустите ее.
Если функция нвзывется some_function, то тестирующия функция называется test_some_function.
Для проверки просто запустите тестирующую функцию, если после запуска увидели сообщение
Great your solution works! значит все ок!
Если возникла ошибка AssertionError значит решение не работает.
Если вдруг вы нашли ошибку в тестах, пишите в чат мы обсудим.
"""


def unique(numbers):
    """
    Дна список чисел. Некоторые числа в нем могут повторяться.
    Верните новый список чисел, который состоит из чисел numbers, но уже без повторений.
    """
    pass


def test_unique():
    assert unique([1, 1, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert unique([1, 1, 1, 1]) == [1]
    assert unique([]) == []


def count_words(string):
    """
    Дан список строк strings.
    Нужно для каждой строки посчитать сколько раз она встретилось в списке.
    """
    pass


def test_count_words():
    assert count_words(["text", "text", "apple", "orange", "yellow", "orange"]) == {
        "text": 2,
        "orange": 2,
        "yellow": 1,
        "apple": 1
    }
    assert count_words(["text", "text", "text", "text", "text", "orange"]) == {
        "text": 5,
        "orange": 1,
    }
    assert count_words([]) == {}


def consistent_string(strings, allowed):
    """
    Дан список строк strings, и строка allowed, которая состоит из уникальных символов.
    Реализуйте функцию, которая из списка строк strings отфильтрует только те, которые состоят из символов
    содержащихся в allowed и не содержат других символов. Нужное вернуть множество(set) из нужных строк.
    """
    pass


def test_consistent_string():
    assert consistent_string(allowed="ab", strings=["ad", "bd", "aaab", "baa", "badab"]) == {"aaab", "baa"}
    assert consistent_string(allowed="abc", strings=["a", "b", "c", "ab", "ac", "bc", "abc"]) == {"a", "b", "c", "ab",
                                                                                                  "ac", "bc", "abc"}
    assert consistent_string(allowed="cad", strings=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == {"cc", "acd",
                                                                                                           "ac", "d"}


def sort_desc(strings):
    """
    Дан список строк. Отсортируйте его в порядке обратном алфавитному.
    """
    pass


def test_sort_desc():
    assert sort_desc(["ad", "bd", "aaab", "baa", "badab"]) == ['bd', 'badab', 'baa', 'ad', 'aaab']
    assert sort_desc(["a", "b", "c", "ab", "ac", "bc", "abc"]) == ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a']


def filter_even(numbers):
    """
    При помощи встроенный функции фильтр, отфильтруйте только четные числа из списка numbers
    в отсортированном по возрастанию порядке
    """


def test_filter_even():
    assert filter_even([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12]) == [2, 4, 6, 8, 10, 12]
    assert filter_even([2, 2, 4, 6, 6, 8, 10, 12]) == [2, 2, 4, 6, 6, 8, 10, 12]
    assert filter_even([1, 1, 2, 3]) == [2]
    assert filter_even([1, 3, 5]) == []





