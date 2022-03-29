import openpyxl as ox  # работа с Excel
import ipaddress as ipa  # Работа с адресами
import warnings  # Обработчик ошибок без доп.функций
import re


def check_ip(ip):
    try:  # Если
        ipa.ip_interface(ip)  # Этот адрес ip верный
        return True  # Вернуть True
    except ValueError:  # Если вылетает ошибка (ipaddress.ip_interface выдает ValueError)
        return False  # Вернуть False


print('Для работы костыля положите Firewall.xlsx в ту же папку и нажмите Enter')
input()

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')  # Обрабатываем ошибку расширенных проверок

book = ox.load_workbook('Firewall.xlsx', data_only=True)  # Объявляем чтение книги

for row in range(15, book.worksheets[0].max_row + 1):  # Вывод с 15 строки на первой стр. до последнего значения
    sheet = book.worksheets[0]  # Присваиваем первой странице
    name = sheet[row][4].value  # Значения из D столбца
    src_name = sheet[row][5].value  # Значения из F столбца
    src_ip = sheet[row][6].value  # Значения из G столбца
    port = sheet[row][7].value  # Значения из H столбца
    main_str = [row, src_name, src_ip, name, port]  # собираем в список
    proc_str = ''

    for i in main_str[1:3]:
        if i in ['#N/A', 'None', None] or str(i).find('N/A') != -1:  # Удаляем строки без значений
            proc_str = ''
            break
        proc_str += str(i) + ' '  # Если в строке есть значения - сохраняем в proc_str

    if proc_str != '':
        proc_dic = {'name': main_str[3], 'row': main_str[0], 'src_name': main_str[1], 'src_ip': main_str[2],
                    'port': []}  # Генерируем словарь из всех вводных данных
        for prt in main_str[4:]:  # начиная с портов разделяем по \n и загоняем в словарь
            prt = str(prt).split('\n')
            proc_dic['port'] = prt

        for pt in proc_dic['port']:  # Из словаря дёргаем поры
            gno = re.search(r"TCP/|UDP/|ICMP|GRE|None", pt)  # Регулярным выражением проверяем правильность значения
            if gno is None:  # Если поиск не дал результатов - записывается None
                print(f'В строке №{row} порт/протокол {pt} указан некорректно, проверьте')

        if '\n' in main_str[1]:
            print(f'В строке №{row} ошибка, указано несколько имен объектов. Одно имя == один адрес.')
        if '\n' in main_str[2]:
            print(f'В строке №{row} ошибка, указано несколько ip адресов. Один адрес == одно имя.')
        if '\n' not in main_str[2]:
            if check_ip(main_str[2]) is False:
                print(
                    f'Адрес "{main_str[2]}" в строке №{row} не является хостом или сетью. Укажите в формате *.*.*.*/*')

input()
