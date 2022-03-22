import openpyxl as ox  # работа с Excel
from tabulate import tabulate  # Вывод табличкой, а не кортежами
import ipaddress as ipa  # Работа с адресами
import warnings  # Обработчик ошибок без доп.функций


def check_ip(ip):
    try:  # Если
        ipa.ip_interface(ip)  # Этот адрес ip верный
        return True  # Вернуть True
    except ValueError:  # Если вылетает ошибка (ipaddress.ip_interface выдает ValueError)
        return False  # Вернуть False


warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')  # Обрабатываем ошибку расширенных проверок

book = ox.load_workbook('Firewall.xlsx', data_only=True)  # Объявляем чтение книги

for row in range(15, book.worksheets[0].max_row + 1):  # Вывод с 15 строки на первой стр. до последнего значения
    sheet = book.worksheets[0]  # Присваиваем первой странице
    src_name = sheet[row][5].value  # Значения из F столбца
    port = sheet[row][6].value  # Значения из G столбца
    main_str = [row, src_name, port]  # собираем в список
    proc_str = ''

    for i in main_str:
        if i in ['#N/A', 'None', None] or str(i).find('N/A') != -1:  # Удаляем строки без значений
            proc_str = ''
            break
        proc_str += str(i) + ' '  # Если в строке есть значения - сохраняем в proc_str

    if proc_str != '':
        if '\n' in main_str[1]:
            print(f'В строке {row} ошибка, указано несколько имен объектов')
        if '\n' in main_str[2]:
            print(f'В строке {row} ошибка, указано несколько ip адресов')
        if '\n' not in main_str[2]:
            if check_ip(main_str[2]) is False:
                print(f'Адрес "{main_str[2]}" в строке не является хостом или сетью')
    print(main_str)