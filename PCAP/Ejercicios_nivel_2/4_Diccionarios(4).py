
fecha = input("Introduce la fecha dd/mm/aaaa: ")

dia, mes, año = fecha.split("/")

meses = {
    "01": "enero", "02": "febrero", "03": "marzo", "04": "abril",
    "05": "mayo", "06": "junio", "07": "julio", "08": "agosto",
    "09": "septiembre", "10": "octubre", "11": "noviembre", "12": "diciembre"
}

nombre_mes = meses[mes]

print(f"{dia} de {nombre_mes} de {año}")