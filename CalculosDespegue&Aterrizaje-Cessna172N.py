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

tabla_despegue = {
    "0C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1250, 1370, 1510, 1670, 1860, 2060, 2310, 2610, 2975]
    },
    "10C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1340, 1475, 1625, 1800, 2000, 2235, 2515, 2850, 3245]
    },
    "20C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1440, 1585, 1750, 1940, 2165, 2425, 2740, 3125, 3610]
    },
    "30C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1545, 1705, 1885, 2095, 2340, 2635, 2985, 3430, 4000]
    },
    "40C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1655, 1830, 2030, 2260, 2535, 2860, 3265, 3775, 4465]
    }
}

tabla_aterrizaje = {
    "0C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1400, 1550, 1750, 1950, 2150, 2500, 2900, 3400, 4000]
    },
    "10C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1500, 1650, 1850, 2050, 2250, 2600, 3000, 3500, 4100]
    },
    "20C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1600, 1750, 1950, 2150, 2350, 2700, 3100, 3600, 4200]
    },
    "30C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1700, 1850, 2050, 2250, 2450, 2800, 3200, 3700, 4300]
    },
    "40C": {
        "PRESS_ALT_FT": [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
        "TOTAL_TO_CLEAR_50FT_OBS": [1800, 1950, 2150, 2350, 2550, 2900, 3300, 3800, 4400]
    }
}

def calcular_despegue(peso, altitud, temp, tipo_campo):
    if tipo_campo == "standard":
        tabla = tabla_despegue
    elif tipo_campo == "short_field":
        tabla = tabla_despegue_short_field
    else:
        raise ValueError("Tipo de campo no válido")

    if altitud < 0 or altitud > 8000:
        raise ValueError("Altitud fuera del rango permitido")

    presion = (peso / 1000) + (temp * 2)
    if temp < 0:
        temp_key = "0C"
    elif temp < 10:
        temp_key = "10C"
    elif temp < 20:
        temp_key = "20C"
    elif temp < 30:
        temp_key = "30C"
    else:
        temp_key = "40C"

    pres_alt_ft = tabla[temp_key]["PRESS_ALT_FT"]
    total_clear_obs = tabla[temp_key]["TOTAL_TO_CLEAR_50FT_OBS"]

    return total_clear_obs[altitud // 1000]

def calcular_aterrizaje(peso, altitud, temp):
    if altitud < 0 or altitud > 8000:
        raise ValueError("Altitud fuera del rango permitido")

    if temp < 0:
        temp_key = "0C"
    elif temp < 10:
        temp_key = "10C"
    elif temp < 20:
        temp_key = "20C"
    elif temp < 30:
        temp_key = "30C"
    else:
        temp_key = "40C"

    pres_alt_ft = tabla_aterrizaje[temp_key]["PRESS_ALT_FT"]
    total_clear_obs = tabla_aterrizaje[temp_key]["TOTAL_TO_CLEAR_50FT_OBS"]

    return total_clear_obs[altitud // 1000]

def main():
    while True:
        print("\nBienvenido al calculador de despegue y aterrizaje.")
        print("1. Calcular despegue")
        print("2. Calcular aterrizaje")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_lista_aeropuertos()
            aerodromo = input("Selecciona un aeródromo de salida (por ejemplo, MGPB): ")
            peso = float(input("Ingrese el peso de la aeronave en libras: "))
            altitud = int(input("Ingrese la altitud en pies (0 a 8000): "))
            temp = float(input("Ingrese la temperatura en grados Celsius: "))
            tipo_campo = input("Ingrese el tipo de campo (standard o short_field): ")
            resultado = calcular_despegue(peso, altitud, temp, tipo_campo)
            print(f"Total para despegar: {resultado} pies.")

        elif opcion == "2":
            mostrar_lista_aeropuertos()
            aerodromo = input("Selecciona un aeródromo de salida (por ejemplo, MGPB): ")
            peso = float(input("Ingrese el peso de la aeronave en libras: "))
            altitud = int(input("Ingrese la altitud en pies (0 a 8000): "))
            temp = float(input("Ingrese la temperatura en grados Celsius: "))
            resultado = calcular_aterrizaje(peso, altitud, temp)
            print(f"Total para aterrizar: {resultado} pies.")

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
