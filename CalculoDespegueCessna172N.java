import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CalculoDespegueCessna172N {

    private static final Map<String, Map<String, int[]>> tablaCombinada = new HashMap<>();

    static {
        Map<String, int[]> tabla0C = new HashMap<>();
        tabla0C.put("PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000});
        tabla0C.put("TOTAL_TO_CLEAR_50_FT_OBS", new int[]{1250, 1370, 1510, 1675, 1859, 2061, 2314, 2611, 2975});
        tablaCombinada.put("0C", tabla0C);

        Map<String, int[]> tabla10C = new HashMap<>();
        tabla10C.put("PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000});
        tabla10C.put("TOTAL_TO_CLEAR_50_FT_OBS", new int[]{1340, 1475, 1625, 1800, 2000, 2235, 2510, 2850, 3270});
        tablaCombinada.put("10C", tabla10C);

        Map<String, int[]> tabla20C = new HashMap<>();
        tabla20C.put("PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000});
        tabla20C.put("TOTAL_TO_CLEAR_50_FT_OBS", new int[]{1440, 1585, 1750, 1940, 2165, 2425, 2740, 3125, 3610});
        tablaCombinada.put("20C", tabla20C);

        Map<String, int[]> tabla30C = new HashMap<>();
        tabla30C.put("PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000});
        tabla30C.put("TOTAL_TO_CLEAR_50_FT_OBS", new int[]{1545, 1705, 1885, 2095, 2340, 2635, 2985, 3430, 4000});
        tablaCombinada.put("30C", tabla30C);

        Map<String, int[]> tabla40C = new HashMap<>();
        tabla40C.put("PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000});
        tabla40C.put("TOTAL_TO_CLEAR_50_FT_OBS", new int[]{1655, 1830, 2030, 2260, 2535, 2860, 3265, 3775, 4465});
        tablaCombinada.put("40C", tabla40C);
    }

    public static Map<String, Integer> obtenerDatosAltitud(int altitud, int temperatura) {
        String tablaTemperatura;
        if (temperatura < 0 || temperatura > 40) {
            System.out.println("Temperatura fuera de rango (0°C - 40°C).");
            return null;
        } else if (temperatura < 10) {
            tablaTemperatura = "0C";
        } else if (temperatura < 20) {
            tablaTemperatura = "10C";
        } else if (temperatura < 30) {
            tablaTemperatura = "20C";
        } else if (temperatura < 40) {
            tablaTemperatura = "30C";
        } else {
            tablaTemperatura = "40C";
        }

        Map<String, int[]> tablaSeleccionada = tablaCombinada.get(tablaTemperatura);
        for (int i = 0; i < tablaSeleccionada.get("PRESS_ALT_FT").length; i++) {
            if (tablaSeleccionada.get("PRESS_ALT_FT")[i] == altitud) {
                return Map.of("PRESS ALT FT", altitud, "TOTAL TO CLEAR 50 FT OBS", tablaSeleccionada.get("TOTAL_TO_CLEAR_50_FT_OBS")[i]);
            }
        }
        System.out.println("No se encontraron datos de altitud para la altitud y temperatura seleccionadas.");
        return null;
    }

    public static void calcularPerformanceDistancia(int temperatura, int vientoContra, int vientoCola, String tipoPista, String aeropuerto) {
        Map<String, Double> elevacionesPreestablecidas = Map.of(
                "mgpb", 32.80,
                "mgsj", 45.93,
                "mgrd", 65.61,
                "mgrb", 465.88,
                "mgza", 633.20,
                "mgrt", 656.16,
                "mgpp", 1692.91,
                "mggt", 5000.0,
                "mgqz", 7808.40,
                "mgsm", 7939.63,
                "mgqc", 6614.17
        );
        String aeropuertoLower = aeropuerto.toLowerCase();
        double elevacionPies;
        if (elevacionesPreestablecidas.containsKey(aeropuertoLower)) {
            elevacionPies = elevacionesPreestablecidas.get(aeropuertoLower);
        } else {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Ingresa la altura del aeropuerto (en pies): ");
            elevacionPies = scanner.nextDouble();
        }

        double xPorcentaje = vientoContra / 9.0;
        Map<String, Integer> datosAltitud = obtenerDatosAltitud((int) elevacionPies, temperatura);
        if (datosAltitud != null) {
            int totalToClear = datosAltitud.get("TOTAL TO CLEAR 50 FT OBS");

            double distanciaNecesariaPies = totalToClear - (totalToClear * (xPorcentaje / 100.0));

            if (vientoCola <= 10) {
                distanciaNecesariaPies *= 1.10;
            }
            if (tipoPista.equalsIgnoreCase("dry") || tipoPista.equalsIgnoreCase("grass runway")) {
                distanciaNecesariaPies *= 1.15;
            }

            System.out.println("Datos de Altitud: " + datosAltitud);
            System.out.println("Distancia necesaria para despegue (pies): " + distanciaNecesariaPies);
        } else {
            System.out.println("No se pudieron calcular los datos de altitud para la altitud y temperatura seleccionadas.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("\nBienvenido al Calculador de Distancia para el Despegue de un Cessna 172N\n"
                    + "Este sistema te permite calcular la distancia necesaria para el despegue de un Cessna 172N "
                    + "considerando varias condiciones, como longitud de la pista, temperatura del aeropuerto de salida, "
                    + "viento y tipo de pista. Este programa está diseñado para vuelos internos en Guatemala, o para"
                    + "salida de vuelos internacionales partiendo de aeropuertos guatemaltecos.\n");

            System.out.println("\nLista de aeropuertos/aeródromos de salida:");
            System.out.println("| LUGAR             | INDICADOR |");
            System.out.println("|-------------------|-----------|");
            System.out.println("| PUERTO BARRIOS    | MGPB      |");
            System.out.println("| PUERTO DE SAN JOSÉ| MGSJ      |");
            System.out.println("| BARILLAS          | MGBA      |");
            System.out.println("| BANANERA          | MGBN      |");
            System.out.println("| COBÁN             | MGCB      |");
            System.out.println("| CHAHAL            | MGCH      |");
            System.out.println("| CHINAJÁ           | MGCJ      |");
            System.out.println("| CHAMÁ             | MGCM      |");
            System.out.println("| CHAMPERICO        | MGCP      |");
            System.out.println("| CHIQUIMULA        | MGCQ      |");
            System.out.println("| CARMELITA         | MGCR      |");
            System.out.println("| CHISEC            | MGCS      |");
            System.out.println("| COATEPEQUE        | MGCT      |");
            System.out.println("| DOS LAGUNAS       | MGDL      |");
            System.out.println("| ESQUIPULAS        | MGES      |");
            System.out.println("| FRAY BARTOLOMÉ    |           |");
            System.out.println("| DE LAS CASAS      | MGFB      |");
            System.out.println("| LA AURORA         | MGGT      |");
            System.out.println("| HUEHUETENANGO     | MGHT      |");
            System.out.println("| SAN JERÓNIMO      | MGJE      |");
            System.out.println("| JUTIAPA           | MGJU      |");
            System.out.println("| LA LIBERTAD       | MGLL      |");
            System.out.println("| MUNDO MAYA        | MGMM      |");
            System.out.println("| PLAYA GRANDE      | MGPG      |");
            System.out.println("| PETÉN ITZÁ        | MGPI      |");
            System.out.println("| POPTÚN            | MGPP      |");
            System.out.println("| QUICHÉ            | MGQC      |");
            System.out.println("| QUETZALTENANGO    | MGQZ      |");
            System.out.println("| RABINAL           | MGRA      |");
            System.out.println("| RUBELSANTO        | MGRB      |");
            System.out.println("| RÍO DULCE         | MGRD      |");
            System.out.println("| RESURRECCIÓN      | MGRE      |");
            System.out.println("| RETALHULEU        | MGRT      |");
            System.out.println("| SAN ANDRÉS        |           |");
            System.out.println("| SAJCABAJÁ         | MGSA      |");
            System.out.println("| SAN MARCOS        | MGSM      |");
            System.out.println("| SAYAXCHÉ          | MGSX      |");
            System.out.println("| TILAPA            | MGTI      |");
            System.out.println("| USPANTÁN          | MGUS      |");
            System.out.println("| XALBAL            | MGXB      |");
            System.out.println("| ZACAPA            | MGZA      |\n");

            System.out.print("Por favor, ingresa el indicador del aeropuerto/aeródromo de salida: ");
            String aeropuertoSalida = scanner.nextLine();
            System.out.print("Por favor, ingresa la temperatura del aeropuerto de salida (en grados Celsius): ");
            int temperatura = scanner.nextInt();
            System.out.print("¿Tienes viento en contra? (nudos): ");
            int vientoContra = scanner.nextInt();
            double vientoCola;
            if (vientoContra == 0) {
                System.out.print("¿Cuántos nudos de viento en cola tienes? ");
                vientoCola = scanner.nextDouble();
            } else {
                System.out.print("¿Cuántos nudos de viento en cola tienes? ");
                vientoCola = scanner.nextDouble();
            }
            scanner.nextLine(); // Limpiar buffer
            System.out.print("Por favor, ingresa el tipo de pista (dry, grass, normal): ");
            String tipoPista = scanner.nextLine();

            calcularPerformanceDistancia(temperatura, vientoContra, (int) vientoCola, tipoPista, aeropuertoSalida);

            System.out.print("¿Deseas realizar otro cálculo? (s/n): ");
            String continuar = scanner.nextLine();
            if (!continuar.equalsIgnoreCase("s")) {
                System.out.println("¡Gracias por usar el Calculador de Distancia para el Despegue!");
                break;
            }
        }
    }
}
