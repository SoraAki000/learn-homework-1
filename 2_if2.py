"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры
  и выводя на экран результаты

"""


def main():
    def comparing(stroka_1, stroka_2):
        if (type(stroka_1) != str) or (type(stroka_2) != str):
            return 0
        elif stroka_1 == stroka_2:
            return 1
        elif stroka_2 == "learn":
            return 3
        elif len(stroka_1) > len(stroka_2):
            return 2

    print(comparing("test", 0))
    print(comparing("same string", "same string"))
    print(comparing("first long string", "second string"))
    print(comparing("wha we doing here?", "learn"))


if __name__ == "__main__":
    main()
