# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open("test_file/task_3.txt", "r") as file:
    purchases_data = file.read().strip().split("\n\n")

purchases = []
for purchase in purchases_data:
    purchase_list = []
    for price in purchase.split("\n"):
        purchase_list.append(int(price))
    purchases.append(purchase_list)

three_most_expensive_purchases = sum(sorted([sum(sublist) for sublist in purchases], reverse=True) [:3])

assert three_most_expensive_purchases == 202346
