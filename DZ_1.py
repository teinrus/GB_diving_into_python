# #При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# #При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

a = 1
b = 1
c = 3

# Введите ваше решение ниже
if a < b+c or b < a+c or c < a+b:
    print("Треугольник существует")
    if a == b and b == c:
        print("Треугольник равносторонний")
    elif a == b:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".

# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.   
num = 4

# from math import sqrt

if 1 >= num or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    i = 2
    prime = True
    while i <= sqrt(num):
        if num % i == 0:
            prime = False
            break
        i += 1
    
    if prime:
        print("Простое")
    else:
        print("Не является простым")

# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Числа в каждом списке не повторяются.

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# Введите ваше решение ниже
my_sum=0
for el in list2:
    if el in list1:
        my_sum+=1

print(f"Количество совпадающих чисел: {my_sum}")