import pandas as pd

xl = pd.ExcelFile("Firewall.xlsx")
df = pd.read_excel(xl, 0)

print(df)

