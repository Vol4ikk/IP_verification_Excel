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