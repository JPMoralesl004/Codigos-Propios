import java.util.ArrayList;
import java.util.Collections;

class Mazo {
    
    private ArrayList<Carta> cartas;

    public Mazo() {
        cartas = new ArrayList<>();

        for (Carta.Color color : Carta.Color.values()) {

            if (color == Carta.Color.NINGUNO) continue;

            for (int i = 0; i < 10; i++) {
                cartas.add(new Carta(color, Carta.Tipo.NUMERO, i));

                if (i != 0) cartas.add(new Carta(color, Carta.Tipo.NUMERO, i));
            }
            for (int i = 0; i < 2; i++) {
                cartas.add(new Carta(color, Carta.Tipo.SALTAR, -1));
                cartas.add(new Carta(color, Carta.Tipo.REVERSO, -1));
                cartas.add(new Carta(color, Carta.Tipo.ROBA_DOS, -1));
            }
        }
        for (int i = 0; i < 4; i++) {
            cartas.add(new Carta(Carta.Color.NINGUNO, Carta.Tipo.COMODIN, -1));
            cartas.add(new Carta(Carta.Color.NINGUNO, Carta.Tipo.COMODIN_ROBA_CUATRO, -1));
        }
        
        Collections.shuffle(cartas);
    }

    public Carta robarCarta() {
        return cartas.remove(cartas.size() - 1);
    }

    public int size() {
        return cartas.size();
    }
}