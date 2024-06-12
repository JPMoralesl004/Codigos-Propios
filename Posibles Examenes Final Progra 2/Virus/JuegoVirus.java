import java.util.Scanner;

public class JuegoVirus {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Juego juego = new Juego();

        System.out.print("Ingrese el nombre del Jugador 1: ");
        String nombreJugador1 = scanner.nextLine();
        Jugador jugador1 = new Jugador(nombreJugador1);

        System.out.print("Ingrese el nombre del Jugador 2: ");
        String nombreJugador2 = scanner.nextLine();
        Jugador jugador2 = new Jugador(nombreJugador2);

        juego.agregarJugador(jugador1);
        juego.agregarJugador(jugador2);
        juego.iniciarJuego();

        for (int turno = 0; turno < 5; turno++) {
            for (Jugador jugador : juego.getJugadores()) {
                System.out.println("\nTurno de " + jugador.getNombre());
                System.out.println("Mano: ");
                for (int i = 0; i < jugador.getMano().size(); i++) {
                    System.out.println(i + ". " + jugador.getMano().get(i).getNombre() + " (" + jugador.getMano().get(i).getTipo() + ")");
                }

                System.out.print("Elija una carta para jugar (ingrese el índice): ");
                int indiceCarta = scanner.nextInt();
                scanner.nextLine();  // Consumir la nueva línea
                jugador.jugarCarta(indiceCarta);
            }
        }

        Jugador ganador = juego.determinarGanador();
        if (ganador != null) {
            System.out.println("El ganador es: " + ganador.getNombre());
        } else {
            System.out.println("El juego ha terminado en empate.");
        }
        
        scanner.close();
    }
}
