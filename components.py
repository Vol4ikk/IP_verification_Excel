import openpyxl as ox

book = ox.load_workbook('../Firewall.xlsx', data_only=True)

sheet_0 = book.worksheets[0]
policy = []

for row in range(15, sheet_0.max_row + 1):
    src_name = sheet_0[row][5].value
    ip = sheet_0[row][6].value
    port = sheet_0[row][7].value
    _l = [row, src_name, ip, port]
    _s = ''

    for i in _l:
        if i in ['#N/A', 'None', None] or str(i).find('N/A') != -1:
            _s = ''
            break
        _s += str(i) + ' || '
    if _s != '':
        print(_s)
