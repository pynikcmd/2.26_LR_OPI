#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Поле first — дробное число, левая граница диапазона;
    поле second — дробное число, правая граница диапазона.
    Реализовать метод rangecheck() — проверку заданного числа
    на принадлежность диапазону.
"""


class Numb:
    def __init__(self, first, second):
        self.first = float(first)  # Преобразование значения аргумента first в тип float и присвоение его полю first
        self.second = float(second)  # Преобразование значения аргумента second в тип float и присвоение его полю second

    def read(self):
        # Ввод значений для полей first и second с клавиатуры
        self.first = float(input("Введите первое значение: "))
        self.second = float(input("Введите второе значение: "))

    def display(self):
        print(f"Pair: {self.first}, {self.second}")  # Вывод пары значений

    def rangecheck(self, number):
        # Проверка принадлежности числа к диапазону
        if self.first <= number <= self.second:
            print(f"{number} находится в диапазоне.")
        else:
            print(f"{number} вне диапазона.")


def make_pair(first, second):
    # Создание объекта Pair и возврат его экземпляра
    return Numb(first, second)


if __name__ == '__main__':
    pair1 = Numb(1.5, 3.7)
    pair1.display()

    pair2 = make_pair(2.0, 4.5)
    pair2.display()

    number = float(input("Введите число для проверки диапазона: "))
    pair2.rangecheck(number)
