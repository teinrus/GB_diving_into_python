# ; Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# ; Функцию hex используйте для проверки своего результата.

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

num = 255

# # Введите ваше решение ниже
for_un_16=str(format(num, "x")).upper()
print(f"Шестнадцатеричное представление числа: {for_un_16}")
print(f"Проверка результата: {hex(num)}")

# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.

# Для проверки своего кода используйте модуль fractions.

#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# frac1 = "1/2"
# frac2 = "1/3"

# # Введите ваше решение ниже
# import fractions

# print(f"Сумма дробей: {fractions.Fraction(frac1)+fractions.Fraction(frac2)}")
# print(f"Произведение дробей: {fractions.Fraction(frac1)*fractions.Fraction(frac2)}")

