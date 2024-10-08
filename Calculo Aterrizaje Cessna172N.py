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
        "40": {
            "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
            "TOTAL_TO_CLEAR_50_FT_OBS": [1330, 1365, 1405, 1440, 1480, 1525, 1570, 1615, 1665]
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
        tabla_temperatura = "40C"

    tabla_seleccionada = tabla_combinada[tabla_temperatura]
    for i in range(len(tabla_seleccionada["PRESS_ALT_FT"])):
        if tabla_seleccionada["PRESS_ALT_FT"][i] == altitud:
            return {"PRESS ALT FT": altitud,
                    "TOTAL TO CLEAR 50 FT OBS": tabla_seleccionada["TOTAL_TO_CLEAR_50_FT_OBS"][i]}
    print("No se encontraron datos de altitud para la altitud y temperatura seleccionadas.")
    return None


def calcular_performance_distancia(temperatura, viento_contra, viento_cola, tipo_pista, aeropuerto,
                                   x_porcentaje_contra=None, x_porcentaje_cola=None):
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
    aeropuerto_lower = aeropuerto.lower()
    if aeropuerto_lower in elevaciones_preestablecidas:
        elevacion_pies = elevaciones_preestablecidas[aeropuerto_lower]

        x_porcentaje_contra = viento_contra / 9
        x_porcentaje_cola = viento_cola / 2

        datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)

        if datos_altitud:
            total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]

            if viento_contra > 0:
                reduccion_por_viento_contra = (x_porcentaje_contra // 10) * (total_to_clear * 0.10)
                total_to_clear -= reduccion_por_viento_contra

            if viento_cola > 0:
                aumento_por_viento_cola = (x_porcentaje_cola // 2) * (total_to_clear * 0.10)
                total_to_clear += aumento_por_viento_cola

            if tipo_pista.lower() == "dry" or tipo_pista.lower() == "grass":
                aumento_por_pista_pastoseco = total_to_clear * 0.45
                total_to_clear += aumento_por_pista_pastoseco

            print("Datos de Altitud:", datos_altitud)
            print("Distancia necesaria para el aterrizaje (pies):", total_to_clear)
        else:
            print("No se pudieron calcular los datos de altitud para la altitud y temperatura seleccionadas.")
    else:
        elevacion_pies = float(input("Ingresa la altura del aeropuerto (en pies): "))
        datos_altitud = obtener_datos_altitud(elevacion_pies, temperatura)

        if datos_altitud:
            total_to_clear = datos_altitud["TOTAL TO CLEAR 50 FT OBS"]

            if viento_contra > 0:
                reduccion_por_viento_contra = (x_porcentaje_contra // 10) * (total_to_clear * 0.10)
                total_to_clear -= reduccion_por_viento_contra

            if viento_cola > 0:
                aumento_por_viento_cola = (x_porcentaje_cola // 2) * (total_to_clear * 0.10)
                total_to_clear += aumento_por_viento_cola

            if tipo_pista.lower() == "dry" or tipo_pista.lower() == "grass":
                aumento_por_pista_pastoseco = total_to_clear * 0.45
                total_to_clear += aumento_por_pista_pastoseco

            print("Datos de Altitud:", datos_altitud)
            print("Distancia necesaria para el aterrizaje (pies):", total_to_clear)
        else:
            print("No se pudieron calcular los datos de altitud para la altitud y temperatura seleccionadas.")


def main():
    while True:
        print("\nBienvenido al Calculador de Distancia para el Aterrizaje de un Cessna 172N\n"
              "Este sistema te permite calcular la distancia necesaria para el aterrizaje de un Cessna 172N "
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

        aeropuerto_salida = input("Por favor, ingresa el indicador del aeropuerto/aeródromo de salida: ").lower()
        temperatura = float(input("Por favor, ingresa la temperatura del aeropuerto de salida (en grados Celsius): "))
        viento_contra = float(input("¿Tienes viento en contra? (nudos): "))

        if viento_contra == 0:
            viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))
        else:
            viento_cola = float(input("¿Cuántos nudos de viento en cola tienes? "))

        tipo_pista = input("Por favor, ingresa el tipo de pista (dry, grass, normal): ")

        calcular_performance_distancia(temperatura=temperatura, viento_contra=viento_contra, viento_cola=viento_cola,
                                       tipo_pista=tipo_pista, aeropuerto=aeropuerto_salida)

        continuar = input("¿Deseas realizar otro cálculo? (s/n): ")
        if continuar.lower() != "s":
            print("¡Gracias por usar el Calculador de Distancia para el Aterrizaje!")
            break

if __name__ == "__main__":
    main()
