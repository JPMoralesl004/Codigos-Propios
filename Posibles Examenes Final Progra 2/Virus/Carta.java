class Carta {
    private String nombre;
    private String tipo;

    public Carta(String nombre, String tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public void jugar(Jugador jugador) {
    }
}