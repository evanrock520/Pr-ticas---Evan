from matplotlib import pyplot as plt
import datetime
from procesa_csv import extraer

# Define el nombre del archivo y número de líneas de encabezado
nombre_archivo = "datos.csv"   
len_header = 1                

# Extrae los datos
datos = extraer(nombre_archivo, len_header)

# Convierte las fechas y horas a objetos datetime
fechas_horas = []
for f, h in zip(datos['fecha'], datos['hora']):  
    dt = datetime.datetime.strptime(f + ' ' + h, '%Y/%m/%d %H:%M:%S')
    fechas_horas.append(dt)

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(fechas_horas, datos['T'], label='Temperatura')
plt.xlabel("Tiempo")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura a lo largo del tiempo")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
