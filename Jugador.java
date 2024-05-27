import java.util.ArrayList;

class Jugador {

    private ArrayList<Carta> mano;
    private int id;

    public Jugador(int id) {

        this.id = id;
        mano = new ArrayList<>();
    }

    public void robarCarta(Mazo mazo) {
        mano.add(mazo.robarCarta());

    }

    public void jugarCarta(int indice, ArrayList<Carta> pilaDescarte) {
        pilaDescarte.add(mano.remove(indice));

    }

    public ArrayList<Carta> getMano() {
        return mano;

    }

    public boolean haGanado() {
        return mano.isEmpty();

    }

    public int getId() {
        return id;
        
    }
}