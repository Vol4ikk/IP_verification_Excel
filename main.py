import openpyxl as ox

book = ox.load_workbook('Firewall.xlsx', data_only=True)

sheet_1 = book.worksheets[1]
_policy=[]

for row in range(13, sheet_1.max_row + 1):
    # src = sheet_1[row][2].value
    src_name = sheet_1[row][3].value
    src_ip = sheet_1[row][4].value
    # dst = sheet_1[row][6].value
    dst_name = sheet_1[row][7].value
    dst_ip = sheet_1[row][8].value
    port = sheet_1[row][9].value
    # print(row, src_name, src_ip, dst_name, dst_ip, port)
    _l = [row, src_name, src_ip, dst_name, dst_ip, port]
    _s = ''

    for i in _l:
        if i in ['#N/A', 'None', None] or str(i).find('N/A') != -1:
            _s = ''
            break
        _s += str(i) + ' || '
    if _s != '':
        print(_s)
        _policy.append(_l)



