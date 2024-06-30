def obtener_datos_altitud(altitud, temperatura):
    tabla_combinada = {
        "0C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1250, 1370, 1510, 1675, 1859, 2061, 2314, 2611, 2975]
        },
        "10C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1340, 1475, 1625, 1800, 2000, 2235, 2510, 2850, 3270]
        },
        "20C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1440, 1585, 1750, 1940, 2165, 2425, 2740, 3125, 3610]
        },
        "30C": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1545, 1705, 1885, 2095, 2340, 2635, 2985, 3430, 4000]
        },
        "40C": {  # Corregido "40" a "40C"
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1655, 1830, 2030, 2260, 2535, 2860, 3265, 3775, 4465]
        }
    }
    if temperatura < 0 or temperatura > 40:
        print("Temperatura fuera de rango (0°C - 40°C).")
        return None
    elif temperatura < 10:
        tabla_temperatura = "0C"
    elif temperatura < 20:
        tabla_temperatura = "10C"
    elif temperatura < 30:
        tabla_temperatura = "20C"
    elif temperatura < 40:
        tabla_temperatura = "30C"
    else:
        tabla_temperatura = "40C"  # Corregido para manejar temperatura igual a 40°C

    tabla_seleccionada = tabla_combinada[tabla_temperatura]
    for i in range(len(tabla_seleccionada["PRESS_ALT_FT"])):
        if tabla_seleccionada["PRESS_ALT_FT"][i] == altitud:
            return {"PRESS ALT FT": altitud,
                    "TOTAL TO CLEAR 50 FT OBS": tabla_seleccionada["TOTAL_TO_CLEAR_50_FT_OBS"][i]}
    print("No se encontraron datos de altitud para la altitud y temperatura seleccionadas.")
    return None


def calcular_performance_distancia(temperatura, viento_contra, viento_cola, tipo_pista, aeropuerto):
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
    aeropuerto_upper = aeropuerto.upper()  # Convertido a mayúsculas para manejar correctamente los códigos de aeropuerto
    if aeropuerto_upper in elevaciones_preestablecidas:
        elevacion_pies = elevaciones_preestablecidas[aeropuerto_upper]
        x_porcentaje = viento_contra / 9
        datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)
        if datos_altitud:
            total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]

            distancia_necesaria_pies = total_to_clear - (total_to_clear * (x_porcentaje / 100))

            if viento_cola <= 10:
                distancia_necesaria_pies *= 1.10
            if tipo_pista.lower() in ["dry", "grass runway"]:  # Simplificado el chequeo del tipo de pista
                distancia_necesaria_pies *= 1.15

            print("Datos de Altitud:", datos_altitud)
            print("Distancia necesaria para el despegue (pies):", distancia_necesaria_pies)
        else:
            print("No se pudieron calcular los datos de altitud para la altitud y temperatura seleccionadas.")
    else:
        elevacion_pies = float(input("Ingresa la altura del aeropuerto (en pies): "))
        x_porcentaje = viento_contra / 9
        datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)
        if datos_altitud:
            total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]

            distancia_necesaria_pies = total_to_clear - (total_to_clear * (x_porcentaje / 100))

            if viento_cola <= 10:
                distancia_necesaria_pies *= 1.10
            if tipo_pista.lower() in ["dry", "grass runway"]:  # Simplificado el chequeo del tipo de pista
                distancia_necesaria_pies *= 1.15

            print("Datos de Altitud:", datos_altitud)
            print("Distancia necesaria para el despegue (pies):", distancia_necesaria_pies)
        else:
            print("No se pudieron calcular los datos de altitud para la altitud y temperatura seleccionadas.")


def main():
    while True:
        print("\nBienvenido al Calculador de Distancia para el Despegue de un Cessna 172N\n"
              "Este sistema te permite calcular la distancia necesaria para el despegue de un Cessna 172N "
              "considerando varias condiciones, como longitud de la pista, temperatura del aeropuerto de salida, "
              "viento y tipo de pista. Este programa está diseñado para vuelos internos en Guatemala, o para"
              "salida de vuelos internacionales partiendo de aeropuertos guatemaltecos.\n")

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

        aeropuerto_salida = input("Por favor, ingresa el indicador del aeropuerto/aeródromo de salida: ").upper()  # Convertido a mayúsculas
        temperatura = float(input("Por favor, ingresa la temperatura del aeropuerto de salida (en grados Celsius): "))
        viento_contra = float(input("¿Tienes viento en contra? (nudos): "))

        if viento_contra == 0:
            viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))
        else:
            viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))

        tipo_pista = input("Por favor, ingresa el tipo de pista (dry, grass, normal): ")

        calcular_performance_distancia(
            temperatura=temperatura,
            viento_contra=viento_contra,
            viento_cola=viento_cola,
            tipo_pista=tipo_pista,
            aeropuerto=aeropuerto_salida
        )

        continuar = input("¿Deseas realizar otro cálculo? (s/n): ")
        if continuar.lower() != "s":
            print("¡Gracias por usar el Calculador de Distancia para el Despegue!")
            break


if __name__ == "__main__":
    main()
