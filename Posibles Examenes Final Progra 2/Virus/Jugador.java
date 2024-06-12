import java.util.ArrayList;

class Jugador {
    private String nombre;
    private ArrayList<Carta> mano;
    private ArrayList<String> organosInfectados;

    public Jugador(String nombre) {
        this.nombre = nombre;
        this.mano = new ArrayList<>();
        this.organosInfectados = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void agregarCartaAMano(Carta carta) {
        mano.add(carta);
    }

    public void jugarCarta(int indice) {
        if (indice >= 0 && indice < mano.size()) {
            Carta carta = mano.remove(indice);
            carta.jugar(this);
        } else {
            System.out.println("Índice de carta no válido");
        }
    }

    public void infectarOrganos() {
        organosInfectados.add("Órgano " + (organosInfectados.size() + 1));
        System.out.println(nombre + " ha infectado un órgano.");
    }

    public void curarOrganos() {
        if (!organosInfectados.isEmpty()) {
            organosInfectados.remove(organosInfectados.size() - 1);
            System.out.println(nombre + " ha curado un órgano.");
        } else {
            System.out.println(nombre + " no tiene órganos infectados para curar.");
        }
    }

    public void agregarOrgano(String nombreOrgano) {
        System.out.println(nombre + " ha añadido un órgano: " + nombreOrgano);
    }

    public void aplicarTratamiento(String nombreTratamiento) {
        System.out.println(nombre + " ha aplicado el tratamiento: " + nombreTratamiento);
    }

    public ArrayList<String> getOrganosInfectados() {
        return organosInfectados;
    }

    public ArrayList<Carta> getMano() {
        return mano;
    }
}
