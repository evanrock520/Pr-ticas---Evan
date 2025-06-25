def extraer(nombre_archivo, len_header):
    temperatura = []
    humedad = []
    presion = []
    hora = []
    fecha = []

    with open(nombre_archivo, "r") as pfile:
        lineas = pfile.readlines()

    if len(lineas) <= len_header:
        return {}

    for linea in lineas[len_header:]:
        valores = linea.strip().split(',')
        if len(valores) < 4:
            continue

        fecha_hora = valores[0].strip().split(' ')

        fecha.append(fecha_hora[0])
        hora.append(fecha_hora[1])
        temperatura.append(float(valores[1]))
        humedad.append(float(valores[2]))
        presion.append(float(valores[3]))

    datos = {
        'T': temperatura,
        'H': humedad,
        'P': presion,
        'hora': hora,
        'fecha': fecha
    }

    return datos
