class Carta {

    enum Color {
        ROJO, AMARILLO, VERDE, AZUL, NINGUNO
    }

    enum Tipo {
        NUMERO, SALTAR, REVERSO, ROBA_DOS, COMODIN, COMODIN_ROBA_CUATRO
    }

    private Color color;
    private Tipo tipo;
    private int numero;

    public Carta(Color color, Tipo tipo, int numero) {
        this.color = color;
        this.tipo = tipo;
        this.numero = numero;
    }

    public Color getColor() {
        return color;
    }

    public Tipo getTipo() {
        return tipo;
    }

    public int getNumero() {
        return numero;
    }

    public void setColor(Color color) {
        this.color = color;
    }

    public String toString() {
        if (tipo == Tipo.NUMERO) {
            return color + " " + numero;

        }

        else {
            return color + " " + tipo;
        }
    }
}