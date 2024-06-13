class CartaMedicina extends Carta {
    public CartaMedicina(String nombre, String color) {
        super(nombre, "Medicina", color);
    }

    @Override
    public void jugar(Jugador jugador) {
        System.out.println("Carta Medicina jugada: " + getNombre() + " de color " + getColor());
        jugador.curarOrganos();
    }
}
