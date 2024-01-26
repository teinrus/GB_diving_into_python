
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.

# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.

# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.

# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# backpack={}
# temp_item=0
# for key, value in items.items():
#     if value+temp_item <max_weight:
#         backpack[key]=value
#         temp_item+=value
# print(backpack)
        


# # {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}



# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
import re
from collections import Counter

def get_top_words(text):
    # Заменяем апостроф на пробел, чтобы слова, разделенные апострофами, были обработаны отдельно
    text = text.replace("'", " ")
    # Убираем знаки препинания и приводим к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text.lower())
    # Разделяем текст на слова
    words = text.split()
    # Исключаем слова, содержащие цифры
    words = [word for word in words if not any(char.isdigit() for char in word)]

    # Подсчитываем количество встречаемых слов
    word_counts = Counter(words)
    # Получаем топ-10 самых частых слов
    top_words = word_counts.most_common(10)

    # Сортируем сначала по количеству, затем по алфавиту в обратном порядке
    sorted_top_words = sorted(top_words, key=lambda x: (x[1], x[0]), reverse=True)

    return sorted_top_words

# Пример использования
text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"

top_words = get_top_words(text)
print(top_words)









# [('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]
# # [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
# lst = [1, 2, 3, 4, 5]
# lst = [1, 1, 2, 2, 3, 3]
# lst = [1, 1, 1, 1, 1]
# temp_lst1=[]
# temp_lst2=[]
# for el in lst:
#     if el in temp_lst1:
#         temp_lst2.append(el)
#     else:
#         temp_lst1.append(el)

# print(list(set(temp_lst2)))
