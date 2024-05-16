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
