import openpyxl

book = openpyxl.open('Firewall.xlsx', read_only=True)

sheet = book.active
cells = sheet
print(sheet [16][6].value)

for row in range (1,sheet.max_row+1):
    src = sheet[row][3]
    src_name = sheet[row][4]
    src_ip = sheet[row][5]
    print (row, src.value,src_ip.value,src_name.value)