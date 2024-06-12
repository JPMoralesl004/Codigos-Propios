import java.util.ArrayList;
import java.util.Collections;

class Baraja {
    private ArrayList<Carta> cartas;

    public Baraja() {
        cartas = new ArrayList<>();
        inicializarBaraja();
        barajar();
    }

    private void inicializarBaraja() {
        cartas.add(new CartaVirus("Virus 1"));
        cartas.add(new CartaVirus("Virus 2"));
        cartas.add(new CartaMedicina("Medicina 1"));
        cartas.add(new CartaMedicina("Medicina 2"));
        cartas.add(new CartaOrgano("Corazón"));
        cartas.add(new CartaOrgano("Riñón"));
        cartas.add(new CartaTratamiento("Antivirales"));
        cartas.add(new CartaTratamiento("Antibióticos"));
    }

    public void barajar() {
        Collections.shuffle(cartas);
    }

    public Carta robarCarta() {
        return cartas.size() > 0 ? cartas.remove(cartas.size() - 1) : null;
    }
}