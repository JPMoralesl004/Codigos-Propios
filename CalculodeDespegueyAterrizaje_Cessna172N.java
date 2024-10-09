import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CalculoDespegue_aterrizaje {

    static Map<String, Map<String, int[]>> tablaDespegue = new HashMap<>();
    static Map<String, Map<String, int[]>> tablaAterrizaje = new HashMap<>();

    static {
        tablaDespegue.put("0C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1250, 1370, 1510, 1670, 1860, 2060, 2310, 2610, 2975}
        ));
        tablaDespegue.put("10C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1340, 1475, 1625, 1800, 2000, 2235, 2515, 2850, 3245}
        ));
        tablaDespegue.put("20C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1440, 1585, 1750, 1940, 2165, 2425, 2740, 3125, 3610}
        ));
        tablaDespegue.put("30C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1545, 1705, 1885, 2095, 2340, 2635, 2985, 3430, 4000}
        ));
        tablaDespegue.put("40C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1655, 1830, 2030, 2260, 2535, 2860, 3265, 3775, 4465}
        ));

        tablaAterrizaje.put("0C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1400, 1550, 1750, 1950, 2150, 2500, 2900, 3400, 4000}
        ));
        tablaAterrizaje.put("10C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1500, 1650, 1850, 2050, 2250, 2600, 3000, 3500, 4100}
        ));
        tablaAterrizaje.put("20C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1600, 1750, 1950, 2150, 2350, 2700, 3100, 3600, 4200}
        ));
        tablaAterrizaje.put("30C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1700, 1850, 2050, 2250, 2450, 2800, 3200, 3700, 4300}
        ));
        tablaAterrizaje.put("40C", Map.of(
                "PRESS_ALT_FT", new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000},
                "TOTAL_TO_CLEAR_50FT_OBS", new int[]{1800, 1950, 2150, 2350, 2550, 2900, 3300, 3800, 4400}
        ));
    }

    public static void mostrarListaAeropuertos() {
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
        System.out.println("| ZACAPA            | MGZA      |");
    }

    public static int calcularDespegue(double peso, int altitud, double temp, String tipoCampo) {
        Map<String, int[]> tabla = tipoCampo.equals("standard") ? tablaDespegue : tablaDespegue; // No hay tabla para "short_field" en el ejemplo original

        if (altitud < 0 || altitud > 8000) {
            throw new IllegalArgumentException("Altitud fuera del rango permitido");
        }

        String tempKey = temp < 0 ? "0C" : temp < 10 ? "10C" : temp < 20 ? "20C" : temp < 30 ? "30C" : "40C";
        int altitudIndex = altitud / 1000;

        return tabla.get(tempKey)["TOTAL_TO_CLEAR_50FT_OBS"][altitudIndex] + (int) (peso / 1000) * 10; // Este es un cálculo de ejemplo, ajusta según tu lógica.
    }

    public static int calcularAterrizaje(double peso, int altitud, double temp) {
        Map<String, int[]> tabla = tablaAterrizaje;

        if (altitud < 0 || altitud > 8000) {
            throw new IllegalArgumentException("Altitud fuera del rango permitido");
        }

        String tempKey = temp < 0 ? "0C" : temp < 10 ? "10C" : temp < 20 ? "20C" : temp < 30 ? "30C" : "40C";
        int altitudIndex = altitud / 1000;

        return tabla.get(tempKey)["TOTAL_TO_CLEAR_50FT_OBS"][altitudIndex] + (int) (peso / 1000) * 10; // Este es un cálculo de ejemplo, ajusta según tu lógica.
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nBienvenido al calculador de despegue y aterrizaje.");
            System.out.println("1. Calcular despegue");
            System.out.println("2. Calcular aterrizaje");
            System.out.println("3. Salir");
            System.out.print("Selecciona una opción: ");
            String opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                mostrarListaAeropuertos();
                System.out.print("Selecciona un aeródromo de salida (por ejemplo, MGPB): ");
                String aerodromo = scanner.nextLine();
                System.out.print("Ingrese el peso de la aeronave en libras: ");
                double peso = scanner.nextDouble();
                System.out.print("Ingrese la altitud en pies (0 a 8000): ");
                int altitud = scanner.nextInt();
                System.out.print("Ingrese la temperatura en grados Celsius: ");
                double temp = scanner.nextDouble();
                System.out.print("Ingrese el tipo de campo (standard o short_field): ");
                String tipoCampo = scanner.next();
                int resultado = calcularDespegue(peso, altitud, temp, tipoCampo);
                System.out.printf("Total para despegar: %d pies.\n", resultado);
                scanner.nextLine(); // Limpiar el buffer

            } else if (opcion.equals("2")) {
                mostrarListaAeropuertos();
                System.out.print("Selecciona un aeródromo de salida (por ejemplo, MGPB): ");
                String aerodromo = scanner.nextLine();
                System.out.print("Ingrese el peso de la aeronave en libras: ");
                double peso = scanner.nextDouble();
                System.out.print("Ingrese la altitud en pies (0 a 8000): ");
                int altitud = scanner.nextInt();
                System.out.print("Ingrese la temperatura en grados Celsius: ");
                double temp = scanner.nextDouble();
                int resultado = calcularAterrizaje(peso, altitud, temp);
                System.out.printf("Total para aterrizar: %d pies.\n", resultado);
                scanner.nextLine(); // Limpiar el buffer

            } else if (opcion.equals("3")) {
                System.out.println("Saliendo...");
                break;

            } else {
                System.out.println("Opción no válida. Intenta de nuevo.");
            }
        }
        scanner.close();
    }
}
