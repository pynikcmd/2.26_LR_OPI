#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Создать класс Fraction для работы с дробными числами.
    Число должно быть представлено двумя целочисленными полями:
    целая часть и дробная часть. Реализовать арифметические операции сложения,
    вычитания, умножения и операции сравнения.
"""


class Fraction:
    def __init__(self, whole_part, fractional_part):
        self.whole_part = int(whole_part)
        self.fractional_part = int(fractional_part)

    def read(self):
        self.whole_part = int(input("Введите целую часть: "))
        self.fractional_part = int(input("Введите дробную часть: "))

    def display(self):
        print(f"Fraction: {self.whole_part}.{self.fractional_part}")

    def add(self, other):
        if isinstance(other, Fraction):
            # Сложение дробных чисел
            new_whole_part = self.whole_part + other.whole_part
            new_fractional_part = self.fractional_part + other.fractional_part
            # Если дробная часть превышает 99, увеличиваем целую часть на 1 и вычитаем 100 из дробной части
            if new_fractional_part >= 100:
                new_whole_part += 1
                new_fractional_part -= 100
            return Fraction(new_whole_part, new_fractional_part)
        else:
            raise ValueError("Invalid argument type")

    def subtract(self, other):
        if isinstance(other, Fraction):
            # Вычитание дробных чисел
            new_whole_part = self.whole_part - other.whole_part
            new_fractional_part = self.fractional_part - other.fractional_part
            # Если дробная часть отрицательная, уменьшаем целую часть на 1 и добавляем 100 к дробной части
            if new_fractional_part < 0:
                new_whole_part -= 1
                new_fractional_part += 100
            return Fraction(new_whole_part, new_fractional_part)
        else:
            raise ValueError("Invalid argument type")

    def multiply(self, other):
        if isinstance(other, Fraction):
            # Умножение дробных чисел
            new_whole_part = (self.whole_part * other.whole_part) +\
                             (self.fractional_part * other.fractional_part) // 100
            new_fractional_part = (self.fractional_part * other.fractional_part) % 100
            return Fraction(new_whole_part, new_fractional_part)
        else:
            raise ValueError("Invalid argument type")

    def compare(self, other):
        if isinstance(other, Fraction):
            # Сравнение дробных чисел
            self_value = self.whole_part + (self.fractional_part / 100)
            other_value = other.whole_part + (other.fractional_part / 100)
            if self_value < other_value:
                return -1
            elif self_value > other_value:
                return 1
            else:
                return 0
        else:
            raise ValueError("Invalid argument type")


if __name__ == '__main__':
    # Пример использования класса Fraction
    fraction1 = Fraction(1, 50)
    fraction1.display()

    fraction2 = Fraction(0, 0)
    fraction2.read()
    fraction2.display()

    fraction3 = fraction1.add(fraction2)
    print("Сложение:")
    fraction3.display()

    fraction4 = fraction1.subtract(fraction2)
    print("Вычитание:")
    fraction4.display()

    fraction5 = fraction1.multiply(fraction2)
    print("Умножение:")
    fraction5.display()

    comparison = fraction1.compare(fraction2)
    if comparison < 0:
        print("Fraction 1 меньше, чем Fraction 2")
    elif comparison > 0:
        print("Fraction 1 больше, чем Fraction 2")
    else:
        print("Fraction 1 равен Fraction 2")
