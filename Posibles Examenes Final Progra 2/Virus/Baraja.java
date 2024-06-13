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
        cartas.add(new CartaVirus("Virus 1", "Rojo"));
        cartas.add(new CartaVirus("Virus 2", "Verde"));
        cartas.add(new CartaMedicina("Medicina 1", "Azul"));
        cartas.add(new CartaMedicina("Medicina 2", "Amarillo"));
        cartas.add(new CartaOrgano("Corazón", "Rojo"));
        cartas.add(new CartaOrgano("Riñón", "Azul"));
        cartas.add(new CartaTratamiento("Antivirales", "Verde"));
        cartas.add(new CartaTratamiento("Antibióticos", "Amarillo"));
        cartas.add(new CartaVirus("Virus 3", "Azul"));
        cartas.add(new CartaMedicina("Medicina 3", "Rojo"));
        cartas.add(new CartaOrgano("Hígado", "Verde"));
        cartas.add(new CartaTratamiento("Vacuna", "Rojo"));
    }

    public void barajar() {
        Collections.shuffle(cartas);
    }

    public Carta robarCarta() {
        return cartas.size() > 0 ? cartas.remove(cartas.size() - 1) : null;
    }
}
