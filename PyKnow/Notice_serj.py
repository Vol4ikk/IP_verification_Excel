# обычный вывод
ip = '192.168.11.1'
mask = '/30'
print('У сети %s%s маска %s' % (ip, mask, mask))
# Вывод: У сети 192.168.11.1/30 маска /30

# Вывод через ",", вместо переноса слеш
q, w, e = map(int, input().split())  # map - запись введенных данных в переменные
a, b = int(input()), int(input())  # ввести числа через калытуру
print(q, w, e, sep=',', end='/')

# Вывод без пробела с точками через +
print(surname, name[0]+'.'+middlename[0]+'.')

# Разбивка адреса и имени
s = 'dns_Server 192.168.1.1/32'
s = s.replace(' ', '/')
s = s.split('/')
print(s)

# Вывод через словарь и f строку ff
#простой пример
text='''Число {0}; его квадрат = {1}; его куб = {2}'''.format(i,i**2,i**3)
print(text)

#Сложнее пример
a = [
    [14, '192.178.1.', '/30', 'neok'],
    [15, '192.168.11.1', '/24', 'ok'],
]
for raw, ip, mask, res in a:
    result = {
        "ok": f'Строка {raw} - верная',
        'neok': f'Внимание, строка {raw} - ошибочная'
    }
    text = f'Проверка {ip}{mask}. {result[res]}.'
    print(text)

# Проверка 192.178.1./30. Внимание, строка 14 - ошибочная.
# Проверка 192.168.11.1/24. Строка 15 - верная.

# СТРОКИ STRING изменяемый ()
a, b, c = int(input()), int(input()), int(input())  # набить строку через энтер
s = 'hawwo man'
s.find('w', 2)  # поиск w с 2 позции rfind (справа)
s.replace('w', 'l')  # замена w на l
s.isalpha()  # буквы ли?
s.isdigit()  # цифры ли?
s.count('o', 3)  # сколько о с 3 позиции

s.split()  # 'hawwo' 'man', по умолчанию пробел,
s.split('a')  # деление на строки по 'a'
len(s)  # 2 строки (подсчет строк)
','.join(s)  # нельзя соединить строку, если она одна
','.join(s.split())  # делим по пробелу и объединяем запятыми
"".join(reversed(s))  # развернуть строку
s[::-1]  # ТОже развернуть строку
r = '    \n    1413134       '
r.strip()  # удалить спецзнаки со всех стороны
r.lstrip(), r.rstrip()  # удалить спецсимволы слева/справа

# СПИСОК LIST Изменяемый []
A, B, C = sorted([int(input()) for _ in range(3)])  # Что бы набить список через перенос строки энтер
a = input().split()  # Просто набить список через пробел
s = list(map(int, input().split('.')))  # что бы набить список с клавиатуры, преобразовать в int (с помощью map) и разделить по точке
print(''.join(str(e) for e in b))  # b из списка  в строку
# генератор строки с клавиатуры в список int
a = input().split()
a = [int(i) for i in range(5)] # Генерируем i в список а
###
a = [True, 45, '/30', 5.4, [1, 2, 3, 4]]
# 45 in a
# True
b = [13, 15] + [12, '/28']
# [13, 15, 12, '/28']
print(b[2:])
# [12, '/28']
# ____________________
c = [1, 2, 3]
d = c
# b при изменении подятнет а.
#  Можно копировать d = c[:]. a[0:999] - срез с 0 до 999
# ИЛИ d = c.copy()
sum(c)
c.append(4)  # [1,2,3,4]. К с присоединить 4 справа
c.clear()
c.count('a')  # Считаем, сколько раз есть a
c.index(2, 3, 5)  # находим индекс 2 с индекса 3 до 5. Если его нет - ошибка
c.insert(2, 'hello')  # вставить на второй инжекс (сдвинуть вправо)
c.pop(4)  # Удалить справа 4 и показать его (если пусто - ошибка)
c.remove(4)  # удалить слева
i = iter([1,2,3])
next(i)

# ОПЕРАТОРЫ
# IF Если
a = int(input())
if 3 < a < 100:
    print('Больше 3')  # Это если да
    if 100 > a > 10:
        print('Двузначное')
elif a > 100:
    print('Трехзначное')
else:
    print('Не больше 3')  # Это если нет
print('Bye')  # Это в любом случае

# While ЦИКЛ

while True:
    i = (input())
    if i == 'exit':  # Если введется exit цикл закончится
        break
    if len(i) < 5:  # Если длинна а меньше 5, вывести malo и повторить цикл
        print('malo', i)
        continue
#   else:     # Если цикл с условием - можно выводить, что делать при не
#     print('bb')
    print(len(i))


# Удалить все переменные в списке. Без ошибок
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
while 5 in a:  # Выполнять пока выполняется условие, после чего переходить к следующей задаче
    a.remove(5)
    continue  # Повторять пока повторяется
print(a)

# Добавлять пока не встретится 0
a = []
while 0 not in a:
    a.append(int(input()))
print(a)
# Отрицательные в положительные
import random

a = [random.randint(-10,10) for i in range(10)]
b =[abs(elem) for elem in a]
print(b)
# Проверка записи
a = input()
i = 0
while i != len(a):
    if a[i] == "e" or a[i] == "a":
        print("Ага! Нашлась")
        break
    else:
        print('Текущая буква:', a[i])
        i += 1
while i == len(a):
    print("Распечатали все буквы")
    break

# range - арифметическая прогрессия
list(range(3)) # [0 1 2]
print(list(range(-11,-36,-1))) # отрицательные
range(10, 21, 2) # с 10 до 21 с шагом 2. range(10, 21, 2)
range(3, 0, -1) # В обратном порядке, range(2, 1, 0)
i = iter(range(3))
next(i)
a,b,c = range(5,8)


# Цикл for
# обход по индексам
a = [13, 0, 14, 555, 643, 12, 33, 523, '/30', 22]
n = len(a)
for i in range(n):
    print(i, a[i])
print(a)

# удаление копий дублей
a = [13, 0, 14, 555, 643, 12, 12, 0, 33, 0, 523, '/30', 22]
b = []
for i in a:
    if not i in b:
        b.append(i)
print(b)

# сложение списка
numbers = [1, 2, 3, 4, 5]
total = 0
for i in numbers:
    total += number
print(total)
input('Нажмите энтер') # Цикл продолжится после нажатия энтер

    # Вложенный цикл
a = int(input())
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

# (!)Вложенные списки
a = [
    [0, 4, 11],
    [1, [12, 13, 14, 15], 2, 3],
    [5, 7, 9]
]
print(len(a))  # Длинна всего списка а
print(a[1][1][2])  # Элемент 2 из списка 0 (14)

    # По элементам в списке

for i in a:  # Перебирает строки по одной, без элементов. [0, 4, 11]...
    print(i)
    for j in i:  # Перебирает элементы в строке, которая сейчас в i 0, 4, 11 и возвращается к i
        print(j, end='')
    print()

    # По индексам

for i in range(3):  # Сначала берем первый из трех столбцов
    for j in range(4):  # проходимся по четырем элементам внутри столбца
        print(a[i][j], end=' ')  # Выводим значение i столбца и j строки)
    # Для строк аналогично
b = ['hello', 'hi', 'teryU']
print(b[2][-1])  # Строка тоже список, обращаемся к 2 объекту, последней букве

#Заполнение вложенного списка из фиксированных значений
a = []
n = int(input())  # Строки
m = int(input())  # Столбцы
for i in range(n):  # обходим список n раз (столько строк)
    a.append([0] * m)  # Добавляем значение '0' m раз
for i in a:  # заполняем список a значениями
    print(i)  # в i будут храниться построчно символы '0' m раз

#Заполнение вложенного списка c клавиатуры
a = []
n = int(input())  # Строки
m = int(input())  # Столбцы
for i in range(n):  # обходим список n раз (столько строк)
    b = []  # промежуточный список
    for i in range(m):  # обходим список m раз (столько столбцов)
        b.append(int(input()))  # Добавляем в b то, что ввели с клавиатуры (значения строки)
    a.append(b)  # Наполняем список [a] тем, что набили в строку m
for i in a: # пробегаемся по всем элементам a и выводим
    print(i)

    # ЛУЧШЕ ИСПОЛЬЗОВАТЬ map

# генератор строки
a = [0 for i in range(10) if c>0]

# генератор строки с клавиатуры в список int
a = input().split()
a = [int(i) for i in a]


# SET!!!МНОЖЕСТВО set - выводит только неповторяющиеся объекты
# создание
z = set(map(int, input().split())) # Ввести с калытуры, запилить в множество через пробел
a = {1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4}  # {1,2,3,4}
b = {'he', 'hi', 'ha', 'hi', 'he'}  # {'he', 'hi', 'ha'}
c = set('rhgabcaaabbbccc')  # {'c', 'a', 'h', 'g', 'b', 'r'}
f = set()

# удалить дубли
a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
a = list(set(a))  # сначала делаем множеством, потом обратно списком, но уже без дублей {1,2,3,4}

c = {1, 3, 7, 8, 9}
d = {1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4}
d.add(9)  # Добавление элементов {1,2,3,4,9}
d.update([5, 6, 7])  # добавляем поочередно 5, 6, 7. Если есть дубли - не добавятся

d.discard(4)  # Удалить 4. Если нет - ничего не происходит
d.remove(4)  # Удалить 4, но если нет - ошибка
len(d)  # Длинна множества

# Пересечения
print(4 in d, 7 not in d)  # Есть ли 4 или 7 в множестве
print(d & c)  # Проверка пересечений множеств C и D
c &= d  # В с сохранить пересечения между c и d
print(c.intersection(d))  # Возвращает пересечение, но не изменяет список c
c.intersection_update(d)  # изменяем список с аналогично c &= d. Оставляем только пересечения

# Объединения
print(c | d)
print(c.union(d))  # Возвращает объединенный
с |= d  # объединяет так же как снизу
c = c.union(d)  # объединяет c и d без дублей

# Вычитание
print(c - d)
c -= d

print(c ^ d)  # Симметричная разность. Только различающиеся
c == b  # Сравнение всех элементов

text = input()
a = set()
while text != '':  # Пока не введется пустая строка записывать строки
    slova = text.split()  # делим строки по пробелам
    a.update(slova) # добавляем во множество a все поделенные строки, без повторений
    text = input()
print(len(a))

#!!!!Словари DICT
# Команда items() возвращает объект представления, который отображает список пар кортежей словаря (ключ, значение).

d = {
    # key:value,
    'msk': 495,
    'spb': 812,
    'smr': 63
}

c = dict(msk=495, spb=812, smr=63)  # Только строки

a = [['msk', 495], ['spb', 812], ['smr', 63]]
ad = dict(a)

q = dict.fromkeys(['a', 'b', 'c'], 100)  # Присвоить каждому ключу a,b,c значение 100 в словаре q
print(d['msk'])  # Обращение к ключу msk и вывод 495
print(d.get('msk', 'no sey')) # Тоже обращение к ключу, но без ошибки. Если нет - вернет no sey
d.setdefault('suz', 456) # Обращается к значению, если его енет - создает и ключ, и значение. Если есть - без ошибки

d['arh'] = 4354  # Добавление нового 'arh' ключа в словарь d со значением 4354. Можно изменять так же
del d['arh']  # Удаляем значение ключи и значение arh
d.pop('suz') # удаляет значение и выводит его нам
print('msk' in d, 'ssl' not in d)  # есть ли 'msk' В словаре d

# Вывод всех пар ключ - значение как строка одна
for key in d:
    print(key, d[key])
# Вывод пар как отдельные значения строки
for key, value in d.items():
    print(key, value)

# Генератор словарей
a = {i for i in range(1,11))}

w = {word: len(word) for word in ['hello', 'hi', 'www']} # набиваем словарь словами и считаем длинну слов

# пример
fw = {}  # Пустой словарь
s = 'dns_Server 192.168.1.1/32 192.168.2.1/32 192.168.3.1/32'
s = s.split()  # Разбиваем по пробелу
fw['name'] = s[0]  # первое значение в словать как name
fw['ip'] = []  # Пустой ключ для значения адресов
for i in s[1:]:  # начиная с адресов проходим цикл
    fw['ip'].append(i)  # Добавляем адреса к ключу 'ip' в словаре fw
print(fw)
### {'name': 'dns_Server', 'ip': ['192.168.1.1/32', '192.168.2.1/32', '192.168.3.1/32']}

# Обращаемся к ключу как key, к значению value формируя словарь со значениями Int.
users = {
    'Bob': '43',
    'Ivan': '555',
    'Oleh': '123',
}
# new_data = {key.title(): int(value) for key, value in users.items()}
new_data={} # новый словарь
for key, value in users.items(): # В две переменные берем ключ и значение items()
    new_data[key] = int(value) # по ключу берем значение и делаем его Int
print(users)
print(new_data)
# {'Bob': '43', 'Ivan': '555', 'Oleh': '123'}
# {'Bob': 43, 'Ivan': 555, 'Oleh': 123}


#обращаемся по значению в словаре
users = [
    [0, 'Bob', 'passwd'],
    [12, 'Ivan', 'qwe'],
    [66, 'Oleh', '1234'],
]
new_users = {i[1]: i for i in users} # по значению 1 находим информацию. Можем по 0 или 1, используется как ключ
print(new_users) # Словарь, где [1] - ключ {'Bob': [0, 'Bob', 'passwd'],...
print(new_users['Oleh']) # Ищем по 'Oleh' и выдаем строку [66, 'Oleh', '1234']



    #!!! Функции
def keanu_reeves():
    print("YOU'RE BREATHTAKING")

    #Фильтр по не пустым значениям
g = [1, 3, 4, [], '', 'hi', [1,2],0, 578]
print(list(filter(None, g))) # [1, 3, 4, 'hi', [1, 2], 578]


# Таблицы excel

