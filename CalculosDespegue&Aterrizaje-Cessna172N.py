def main():
    while True:
        print("Bienvenido al sistema de cálculo de despegues y aterrizajes de un Cessna 172N para vuelos internos en Guatemala")
        eleccion = input("¿Qué cálculo deseas realizar? \n1. Despegue \n2. Aterrizaje \n3. Ambos Cálculos \nElige una opción (1, 2, 3): ")

        if eleccion not in ["1", "2", "3"]:
            print("Por favor, selecciona una opción válida.")
            continue

        if eleccion in ["1", "3"]:
            print("\nCálculo de Despegue:")
            mostrar_lista_aeropuertos()
            aeropuerto_salida = input("Por favor, ingresa el indicador del aeropuerto/aeródromo de salida: ").upper()
            try:
                temperatura = float(input("Por favor, ingresa la temperatura del aeropuerto de salida (en grados Celsius): "))
                viento_contra = float(input("¿Tienes viento en contra? (nudos): "))
                viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))
            except ValueError:
                print("Por favor, ingresa valores válidos para la temperatura y el viento.")
                continue
            tipo_pista = input("Por favor, ingresa el tipo de pista (dry, grass, normal): ")
            calcular_performance_despegue(
                temperatura=temperatura,
                viento_contra=viento_contra,
                viento_cola=viento_cola,
                tipo_pista=tipo_pista,
                aeropuerto=aeropuerto_salida
            )

        if eleccion in ["2", "3"]:
            print("\nCálculo de Aterrizaje:")
            mostrar_lista_aeropuertos()
            aeropuerto_llegada = input("Por favor, ingresa el indicador del aeropuerto/aeródromo de llegada: ").upper()
            try:
                temperatura = float(input("Por favor, ingresa la temperatura del aeropuerto de llegada (en grados Celsius): "))
                viento_contra = float(input("¿Tienes viento en contra? (nudos): "))
                viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))
            except ValueError:
                print("Por favor, ingresa valores válidos para la temperatura y el viento.")
                continue
            tipo_pista = input("Por favor, ingresa el tipo de pista (dry, grass, normal): ")
            calcular_performance_aterrizaje(
                temperatura=temperatura,
                viento_contra=viento_contra,
                viento_cola=viento_cola,
                tipo_pista=tipo_pista,
                aeropuerto=aeropuerto_llegada
            )

        continuar = input("¿Deseas realizar otro cálculo? (s/n): ")
        if continuar.lower() != "s":
            print("¡Gracias por usar el sistema de cálculo de despegues y aterrizajes!")
            break

def mostrar_lista_aeropuertos():
    print("\nLista de aeropuertos/aeródromos de salida:")
    print("| LUGAR             | INDICADOR |")
    print("|-------------------|-----------|")
    print("| PUERTO BARRIOS    | MGPB      |")
    print("| PUERTO DE SAN JOSÉ| MGSJ      |")
    print("| BARILLAS          | MGBA      |")
    print("| BANANERA          | MGBN      |")
    print("| COBÁN             | MGCB      |")
    print("| CHAHAL            | MGCH      |")
    print("| CHINAJÁ           | MGCJ      |")
    print("| CHAMÁ             | MGCM      |")
    print("| CHAMPERICO        | MGCP      |")
    print("| CHIQUIMULA        | MGCQ      |")
    print("| CARMELITA         | MGCR      |")
    print("| CHISEC            | MGCS      |")
    print("| COATEPEQUE        | MGCT      |")
    print("| DOS LAGUNAS       | MGDL      |")
    print("| ESQUIPULAS        | MGES      |")
    print("| FRAY BARTOLOMÉ    |           |")
    print("| DE LAS CASAS      | MGFB      |")
    print("| LA AURORA         | MGGT      |")
    print("| HUEHUETENANGO     | MGHT      |")
    print("| SAN JERÓNIMO      | MGJE      |")
    print("| JUTIAPA           | MGJU      |")
    print("| LA LIBERTAD       | MGLL      |")
    print("| MUNDO MAYA        | MGMM      |")
    print("| PLAYA GRANDE      | MGPG      |")
    print("| PETÉN ITZÁ        | MGPI      |")
    print("| POPTÚN            | MGPP      |")
    print("| QUICHÉ            | MGQC      |")
    print("| QUETZALTENANGO    | MGQZ      |")
    print("| RABINAL           | MGRA      |")
    print("| RUBELSANTO        | MGRB      |")
    print("| RÍO DULCE         | MGRD      |")
    print("| RESURRECCIÓN      | MGRE      |")
    print("| RETALHULEU        | MGRT      |")
    print("| SAN ANDRÉS        |           |")
    print("| SAJCABAJÁ         | MGSA      |")
    print("| SAN MARCOS        | MGSM      |")
    print("| SAYAXCHÉ          | MGSX      |")
    print("| TILAPA            | MGTI      |")
    print("| USPANTÁN          | MGUS      |")
    print("| XALBAL            | MGXB      |")
    print("| ZACAPA            | MGZA      |\n")

def obtener_datos_altitud(altitud, temperatura):
    tabla_combinada = {
        "0C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1205, 1235, 1265, 1300, 1335, 1370, 1415, 1455, 1500]
        },
        "10C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1235, 1265, 1300, 1335, 1370, 1415, 1455, 1495, 1540]
        },
        "20C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1265, 1300, 1335, 1370, 1410, 1450, 1490, 1535, 1580]
        },
        "30C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1295, 1330, 1370, 1405, 1445, 1485, 1535, 1575, 1620]
        },
        "40C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1330, 1365, 1405, 1440, 1480, 1525, 1570, 1615, 1665]
        }
    }
    
    if not (0 <= temperatura <= 40):
        print("Temperatura fuera de rango (0°C - 40°C).")
        return None

    if temperatura < 10:
        tabla_temperatura = "0C"
    elif temperatura < 20:
        tabla_temperatura = "10C"
    elif temperatura < 30:
        tabla_temperatura = "20C"
    elif temperatura < 40:
        tabla_temperatura = "30C"
    else:
        tabla_temperatura = "40C"

    tabla_seleccionada = tabla_combinada[tabla_temperatura]
    for i, alt in enumerate(tabla_seleccionada["PRESS_ALT_FT"]):
        if alt == altitud:
            return {"PRESS ALT FT": altitud, "TOTAL TO CLEAR 50 FT OBS": tabla_seleccionada["TOTAL_TO_CLEAR_50_FT_OBS"][i]}
    
    print("No se encontraron datos para la altitud y temperatura seleccionadas.")
    return None

def obtener_elevacion_aeropuerto(aeropuerto):
    elevaciones_preestablecidas = {
        "MGPB": 32.80,
        "MGSJ": 45.93,
        "MGRD": 65.61,
        "MGRB": 465.88,
        "MGZA": 633.20,
        "MGRT": 656.16,
        "MGPP": 1692.91,
        "MGGT": 5000,
        "MGQZ": 7808.40,
        "MGSM": 7939.63,
        "MGQC": 6614.17
    }
    aeropuerto_upper = aeropuerto.upper()
    return elevaciones_preestablecidas.get(aeropuerto_upper, float(input("Ingresa la altura del aeropuerto (en pies): ")))

def calcular_performance_despegue(temperatura, viento_contra, viento_cola, tipo_pista, aeropuerto):
    elevacion_pies = obtener_elevacion_aeropuerto(aeropuerto)
    
    x_porcentaje_contra = viento_contra / 9
    x_porcentaje_cola = viento_cola / 2
    datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)
    if not datos_altitud:
        print("No se pudieron calcular los datos para la altitud y temperatura seleccionadas.")
        return
    
    total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]
    
    if viento_contra > 0:
        reduccion_por_viento_contra = (x_porcentaje_contra // 10) * (total_to_clear * 0.10)
        total_to_clear -= reduccion_por_viento_contra
    if viento_cola > 0:
        aumento_por_viento_cola = (x_porcentaje_cola // 2) * (total_to_clear * 0.10)
        total_to_clear += aumento_por_viento_cola
    if tipo_pista.lower() in ["dry", "grass"]:
        aumento_por_pista_pastoseco = total_to_clear * 0.45
        total_to_clear += aumento_por_pista_pastoseco
    
    print("Datos de Altitud para el Despegue:", datos_altitud)
    print(f"Distancia necesaria para el despegue (pies):", total_to_clear)

def calcular_performance_aterrizaje(temperatura, viento_contra, viento_cola, tipo_pista, aeropuerto):
    elevacion_pies = obtener_elevacion_aeropuerto(aeropuerto)
    
    x_porcentaje_contra = viento_contra / 9
    x_porcentaje_cola = viento_cola / 2
    datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)
    if not datos_altitud:
        print("No se pudieron calcular los datos para la altitud y temperatura seleccionadas.")
        return
    
    total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]
    
    if viento_contra > 0:
        reduccion_por_viento_contra = (x_porcentaje_contra // 10) * (total_to_clear * 0.10)
        total_to_clear -= reduccion_por_viento_contra
    if viento_cola > 0:
        aumento_por_viento_cola = (x_porcentaje_cola // 2) * (total_to_clear * 0.10)
        total_to_clear += aumento_por_viento_cola
    if tipo_pista.lower() in ["dry", "grass"]:
        aumento_por_pista_pastoseco = total_to_clear * 0.45
        total_to_clear += aumento_por_pista_pastoseco
    
    print("Datos de Altitud para el Aterrizaje:", datos_altitud)
    print(f"Distancia necesaria para el aterrizaje (pies):", total_to_clear)

if __name__ == "__main__":
    main()
