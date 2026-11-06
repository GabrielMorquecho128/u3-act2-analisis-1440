# importar librerias
import pandas as pd
import numpy as np
print("Analisis de datos Alumnos Marco morquecho NC=1440")
transacciones = {
    "Id_Transaccion": ["T001", "T002", "T003", "T001", "T002", "T006"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df = pd.DataFrame(transacciones)
print(df)
print("-+-+-+-+ Agrupar por una sola columna Transaccion-+-+-+-+")
agrupado = df.groupby('Id_Transaccion')
print(agrupado)
print("-+-+-+-+ por Monto -+-+-+-+")
# monto promedio por Transaccion
print(agrupado['Monto'].mean())
print("-+-+-+-+ ubicacion inusual -+-+-+-+")
# ubicacion máxima en cada Transaccion
print(agrupado['Ubicacion_Inusual'].max())
print("-+-+-+-+ Agrupar por fraude -+-+-+-+")
# fraude máximo en cada Transaccion
print(agrupado['Es_Fraude'].max())




