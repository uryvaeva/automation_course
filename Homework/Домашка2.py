# Задача № 1
print("Задача № 1")
figure_1 = 3
perimeter = figure_1 * 4
square = figure_1 ** 2
diagonal = round(figure_1 * (2 ** 0.5), 2)
result = f""" Сторона квадрата = {figure_1}. Его периметр = {perimeter}, площадь = {square}, даигональ = {diagonal}.
"""
print(result)

# Задача № 2
print("Задача № 2")
a = 2
b = 6.3
c = 4
discr = round(b ** 2 - 4 * a * c, 2)
result = f""" Для чисел {a}, {b}, {c} дискриминант равен {discr}.
"""
print(result)

# Задача № 3
print("Задача № 3")
str1 = "Первая"
str2 = "Вторая"
symbols1 = str1[:2]
symbols2 = str2[:2]
shifted_1 = symbols2 + str1[2:]
shifted_2 = symbols1 + str2[2:]
result = f""" В словах "{str1}" и "{str2}" меняем местами 2 первые буквы. Получится: "{shifted_1}" и "{shifted_2}".
"""
print(result)

# Задача № 4
print("Задача № 4")
path = r"D:\Download\flash\Vivaldi\concert.mp3"
end_folder = path.find("\\", 3)
extension_dot = path.rfind(".")
last_slash = path.rfind("\\")
print(
    "Полный путь до файла: ", path, "\n",
    "Название файла без расширения:", path[last_slash + 1:extension_dot], "\n",
    "Название диска:", path[0], "\n",
    "Название корневой папки:", path[3:end_folder])

print()

# Задача № 5
print("Задача № 5")
a = 10
b = 30
result1 = """ %d + %d = %d """ % (a, b, a + b)
print(result1)
result2 = """ %d * %d = %d """ % (a, b, a * b)
print(result2)

print()

# Задача № 6
print("Задача № 6")
str3 = "КаРаМеЛьКа"
print("Целое слово:", str3)
print("Без символов, имеющих нечётный индекс:", str3[0:-1:2])

print()

# Задача № 7
print("Задача № 7")
str4 = "btw"
str5 = "I, quartz pyx, who fling muck beds"
first_1 = str5.find(str4[0])
first_2 = str5.find(str4[1])
first_3 = str5.find(str4[2])
print(
    "Первая строка:", str4, "\n",
    "Вторая строка:", str5, "\n",
    "Срез:", str5[min(first_1, first_2, first_3):max(first_1, first_2, first_3) + 1])
