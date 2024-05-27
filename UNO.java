import java.util.ArrayList;
import java.util.Scanner;

public class UNO {

    private static Mazo mazo;
    private static ArrayList<Carta> pilaDescarte;
    private static Jugador[] jugadores;
    private static int jugadorActual;
    private static boolean direccionJuego;
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Menu.mostrarMenu();

        int numeroJugadores = Menu.seleccionarNumeroJugadores();
        
        inicializarJuego(numeroJugadores);

        while (true) {
            
            Jugador jugador = jugadores[jugadorActual];
            System.out.println("Turno del Jugador " + (jugadorActual + 1));
            System.out.println("Tus cartas:");

            for (int i = 0; i < jugador.getMano().size(); i++) {
                System.out.println((i + 1) + ": " + jugador.getMano().get(i));
            }

            System.out.println("Carta en la pila: " + pilaDescarte.get(pilaDescarte.size() - 1));
            System.out.println("Elige una carta para jugar o 0 para robar una carta:");

            int eleccion = scanner.nextInt();

            if (eleccion == 0) {
                jugador.robarCarta(mazo);

            } else {
                Carta cartaElegida = jugador.getMano().get(eleccion - 1);
                Carta cartaSuperior = pilaDescarte.get(pilaDescarte.size() - 1);

                if (puedeJugarCarta(cartaElegida, cartaSuperior)) {
                    jugador.jugarCarta(eleccion - 1, pilaDescarte);
                    ejecutarEfectoCarta(cartaElegida);

                    if (jugador.haGanado()) {
                        System.out.println("¡El Jugador " + (jugadorActual + 1) + " ha ganado!");
                        break;
                    }

                } else {
                    System.out.println("No puedes jugar esa carta.");
                }
            }

            siguienteJugador();
        }

        scanner.close();
    }

    private static void inicializarJuego(int numeroJugadores) {
        mazo = new Mazo();
        pilaDescarte = new ArrayList<>();
        jugadores = new Jugador[numeroJugadores];
        for (int i = 0; i < jugadores.length; i++) {
            jugadores[i] = new Jugador(i + 1);

            for (int j = 0; j < 7; j++) {
                jugadores[i].robarCarta(mazo);
            }
        }

        pilaDescarte.add(mazo.robarCarta());
        jugadorActual = 0;
        direccionJuego = true;
    }

    private static boolean puedeJugarCarta(Carta cartaElegida, Carta cartaSuperior) {

        return cartaElegida.getColor() == cartaSuperior.getColor() ||
            cartaElegida.getTipo() == cartaSuperior.getTipo() ||
            cartaElegida.getColor() == Carta.Color.NINGUNO;
    }

    private static void ejecutarEfectoCarta(Carta carta) {

        switch (carta.getTipo()) {

            case SALTAR:
                siguienteJugador();
                break;

            case REVERSO:
                direccionJuego = !direccionJuego;
                break;

            case ROBA_DOS:
                siguienteJugador();
                jugadores[jugadorActual].robarCarta(mazo);
                jugadores[jugadorActual].robarCarta(mazo);
                break;

            case COMODIN:
                elegirColor(carta);
                break;

            case COMODIN_ROBA_CUATRO:
                elegirColor(carta);
                siguienteJugador();
                jugadores[jugadorActual].robarCarta(mazo);
                jugadores[jugadorActual].robarCarta(mazo);
                jugadores[jugadorActual].robarCarta(mazo);
                jugadores[jugadorActual].robarCarta(mazo);

                break;
        }
    }

    private static void elegirColor(Carta carta) {

        System.out.println("Elige un color: 1. ROJO 2. AMARILLO 3. VERDE 4. AZUL");
        int eleccionColor = scanner.nextInt();
        carta.setColor(Carta.Color.values()[eleccionColor - 1]);
    }

    private static void siguienteJugador() {
        if (direccionJuego) {
            jugadorActual = (jugadorActual + 1) % jugadores.length;

        }

        else {
            jugadorActual = (jugadorActual - 1 + jugadores.length) % jugadores.length;
        }
    }
}