# Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше 
# заданного минимума и не больше заданного максимума)

from random import randint

print('введите длинну массива:')
n =int(input())
list_1 = list()
for i in range(n):
    list_1.append(randint(-10, 10))
print(list_1)

print('введите нижнюю отметку диапазона:')
min = int(input())
print('введите верхнюю отметку диапазона:')
max = int(input())

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i)