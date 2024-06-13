class CartaVirus extends Carta {
    public CartaVirus(String nombre, String color) {
        super(nombre, "Virus", color);
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Virus jugada: " + getNombre() + " de color " + getColor());
        jugador.infectarOrganos();
    }
}
