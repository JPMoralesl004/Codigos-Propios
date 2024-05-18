public class Main {
    public static void main(String[] args) {
        ArbolDecision arbol = new ArbolDecision();
        arbol.iniciarArbol();
        arbol.casoAsintomaticoPositivo();
        arbol.expandirArbolConNuevoFlujo();
        arbol.agregarNotasCuarentenaAislamiento();
        arbol.agregarRecomendacionesPruebasCuarentena();
        arbol.tomarDecision(arbol.raiz);
    }
}