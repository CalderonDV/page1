import pandas as pd 


df = pd.DataFrame(
    {
        "Nombre": ["diego", "lizet", "María", "Pablo"],
        "Apellido": ["calderon", "ochoa", "Tito", "Hernández"],
        "clave": ["123456a","123456b","asd","asdfg"],
    }
)

df.to_excel("ejemplo2.xlsx", sheet_name="Hoja de datos", index=True)


