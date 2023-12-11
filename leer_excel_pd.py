import pandas as pd 


file = pd.ExcelFile("ejemplo2.xlsx")
print(file.sheet_names)
df=file.parse("Hoja de datos")
print(df)

usuario="diego"
id=1
df = pd.read_excel("ejemplo2.xlsx")
column = df.columns[2]
print(column)
print("-" * len(column))

for index, row in df.iterrows():
   if(row[column]==usuario):
        return (print("correcto"))
