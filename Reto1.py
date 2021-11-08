
# Importar libreria Pandas
import pandas as pd

# Leer fichero excel, filtrando que lea la Hoja 1 y la columna email
df = pd.read_excel(io="Documento.xls", sheet_name="Hoja1",usecols=["email"])

# Imprime los emails unicos de la columna emails
print(df["email"].unique())


