import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CalculodeDespegueyAterrizaje_Cessna172N {

    private static final Map<String, Integer> altitudesAeropuertos = new HashMap<>();

    static {
        altitudesAeropuertos.put("mgpb", 33);
        altitudesAeropuertos.put("mgsj", 29);
        altitudesAeropuertos.put("mgba", 1699);
        altitudesAeropuertos.put("mgcb", 4330);
        altitudesAeropuertos.put("mgcr", 627);
        altitudesAeropuertos.put("mgmm", 427);
        altitudesAeropuertos.put("mgpi", 427);
        altitudesAeropuertos.put("mgqz", 7710);
        altitudesAeropuertos.put("mgrt", 656);
        altitudesAeropuertos.put("mgza", 633);
        altitudesAeropuertos.put("mggt", 5000);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Bienvenido al sistema de cálculo de despegues y aterrizajes de un Cessna 172N para vuelos internos en Guatemala");
            System.out.println("¿Qué cálculo deseas realizar? \n1. Despegue \n2. Aterrizaje \n3. Ambos Cálculos \nElige una opción (1, 2, 3): ");
            String eleccion = scanner.nextLine();

            if (!eleccion.equals("1") && !eleccion.equals("2") && !eleccion.equals("3")) {
                System.out.println("Por favor, selecciona una opción válida.");
                continue;
            }

            if (eleccion.equals("1") || eleccion.equals("3")) {
                realizarCalculo(scanner, "Despegue");
            }

            if (eleccion.equals("2") || eleccion.equals("3")) {
                realizarCalculo(scanner, "Aterrizaje");
            }

            System.out.println("¿Deseas realizar otro cálculo? (s/n): ");
            String continuar = scanner.nextLine();
            if (!continuar.equalsIgnoreCase("s")) {
                System.out.println("¡Gracias por usar el sistema de cálculo de despegues y aterrizajes!");
                break;
            }
        }
        scanner.close();
    }

    private static void realizarCalculo(Scanner scanner, String tipoCalculo) {
        System.out.println("\nCálculo de " + tipoCalculo + ":");
        mostrarListaAeropuertos();
        System.out.println("Por favor, ingresa el indicador del aeropuerto/aeródromo de " + (tipoCalculo.equals("Despegue") ? "salida" : "llegada") + ": ");
        String aeropuerto = scanner.nextLine().toLowerCase();

        if (!altitudesAeropuertos.containsKey(aeropuerto)) {
            System.out.println("Aeropuerto no encontrado.");
            return;
        }

        System.out.println("Por favor, ingresa la temperatura del aeropuerto (en grados Celsius): ");
        double temperatura = scanner.nextDouble();
        System.out.println("¿Tienes viento en contra? (nudos): ");
        double vientoContra = scanner.nextDouble();
        System.out.println("¿Cuántos nudos de viento en cola tienes? ");
        double vientoCola = scanner.nextDouble();
        scanner.nextLine();
        System.out.println("Por favor, ingresa el tipo de pista (dry, grass, normal): ");
        String tipoPista = scanner.nextLine().toLowerCase();

        if (tipoCalculo.equals("Despegue")) {
            calcularPerformanceDespegue(temperatura, vientoContra, vientoCola, tipoPista, aeropuerto);
        } else {
            calcularPerformanceAterrizaje(temperatura, vientoContra, vientoCola, tipoPista, aeropuerto);
        }
    }

    private static void mostrarListaAeropuertos() {
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
    }

    private static Map<String, Double> obtenerDatosAltitud(int altitud, double temperatura) {
        Map<String, double[]> tablaCombinada = new HashMap<>();
        tablaCombinada.put("0C", new double[]{1205, 1235, 1265, 1300, 1335, 1370, 1415, 1455, 1500});
        tablaCombinada.put("10C", new double[]{1235, 1265, 1300, 1335, 1370, 1415, 1455, 1495, 1540});
        tablaCombinada.put("20C", new double[]{1265, 1300, 1335, 1370, 1410, 1450, 1490, 1535, 1580});
        tablaCombinada.put("30C", new double[]{1295, 1330, 1370, 1405, 1445, 1485, 1535, 1575, 1620});
        tablaCombinada.put("40C", new double[]{1330, 1365, 1405, 1440, 1480, 1525, 1570, 1615, 1665});

        String keyTemperatura;
        if (temperatura < 0 || temperatura > 40) {
            System.out.println("Temperatura fuera de rango (0°C - 40°C).");
            return null;
        } else if (temperatura < 10) {
            keyTemperatura = "0C";
        } else if (temperatura < 20) {
            keyTemperatura = "10C";
        } else if (temperatura < 30) {
            keyTemperatura = "20C";
        } else {
            keyTemperatura = "30C";
        }

        double[] tablaSeleccionada = tablaCombinada.get(keyTemperatura);
        int[] presAltFt = new int[]{0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000};
        
        for (int i = 0; i < presAltFt.length; i++) {
            if (presAltFt[i] == altitud) {
                Map<String, Double> resultado = new HashMap<>();
                resultado.put("distancia", tablaSeleccionada[i]);
                resultado.put("vref", 65.0 + 5.0 * (altitud / 10000.0));
                return resultado;
            }
        }

        System.out.println("Altitud fuera de rango (0 - 8000 pies).");
        return null;
    }

    private static void calcularPerformanceDespegue(double temperatura, double vientoContra, double vientoCola, String tipoPista, String aeropuerto) {
        int altitud = altitudesAeropuertos.get(aeropuerto);
        Map<String, Double> datos = obtenerDatosAltitud(altitud, temperatura);
        if (datos == null) {
            return;
        }

        double distancia = datos.get("distancia");
        double vref = datos.get("vref");

        if (tipoPista.equals("grass")) {
            distancia *= 1.2;
        }
        distancia -= vientoContra * 5;
        distancia += vientoCola * 5;

        System.out.println("Distancia de despegue requerida: " + distancia + " pies");
        System.out.println("Velocidad de referencia Vref: " + vref + " nudos");
    }

    private static void calcularPerformanceAterrizaje(double temperatura, double vientoContra, double vientoCola, String tipoPista, String aeropuerto) {
        int altitud = altitudesAeropuertos.get(aeropuerto);
        Map<String, Double> datos = obtenerDatosAltitud(altitud, temperatura);
        if (datos == null) {
            return;
        }

        double distancia = datos.get("distancia");
        double vref = datos.get("vref");

        if (tipoPista.equals("grass")) {
            distancia *= 1.2;
        }
        distancia -= vientoContra * 5;
        distancia += vientoCola * 5;

        System.out.println("Distancia de aterrizaje requerida: " + distancia + " pies");
        System.out.println("Velocidad de referencia Vref: " + vref + " nudos");
    }
}
