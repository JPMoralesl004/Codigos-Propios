import java.util.Scanner;

public class Menu {
    private static Scanner scanner = new Scanner(System.in);

    public static void mostrarMenu() {

        System.out.println("Bienvenido a UNO");
        System.out.println("Reglas Básicas del Juego:");
        System.out.println("1. Las cartas deben coincidir en color o número/tipo con la carta superior de la pila de descarte.");
        System.out.println("2. Las cartas especiales pueden cambiar el flujo del juego (Salto, Reverso, Roba Dos, Comodín, Comodín Roba Cuatro).");
        System.out.println("3. El primer jugador en quedarse sin cartas gana el juego.");
        System.out.println("4. Si no puedes jugar una carta, debes robar una carta del mazo.");
        System.out.println();
    }

    public static int seleccionarNumeroJugadores() {
        int numeroJugadores = 0;
        while (numeroJugadores < 2 || numeroJugadores > 10) {
            System.out.println("Selecciona el número de jugadores (2-10):");
            numeroJugadores = scanner.nextInt();

            if (numeroJugadores < 2 || numeroJugadores > 10) {
                System.out.println("Número de jugadores no válido. Por favor, elige entre 2 y 10 jugadores.");
            }
        }

        return numeroJugadores;
    }
}