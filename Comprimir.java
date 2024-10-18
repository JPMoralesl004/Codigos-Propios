import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CompresorLZW {

    public static void main(String[] args) {
        String texto = "abababcbdc"; 
        LZWResultado resultado = comprime(texto);
        
        System.out.print("Salida comprimida: ");
        for (String code : resultado.codigos) {
            System.out.print(code);
        }
        System.out.println();

        System.out.println("Diccionario utilizado:");
        for (Map.Entry<Integer, String> entry : resultado.diccionario.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static LZWResultado comprime(String cadena) {
        Map<String, Integer> diccionario = new HashMap<>();
        List<String> salida = new ArrayList<>();
        
        int tamanioDiccionario = 1;
        diccionario.put("a", tamanioDiccionario++);
        diccionario.put("b", tamanioDiccionario++);
        diccionario.put("c", tamanioDiccionario++);

        String w = "";
        for (char c : cadena.toCharArray()) {
            String wc = w + c;
            if (diccionario.containsKey(wc)) {
                w = wc;
            } else {
                salida.add("(" + (diccionario.get(w) - 1) + "," + w.charAt(w.length() - 1) + ")");
                diccionario.put(wc, tamanioDiccionario++);
                w = "" + c;
            }
        }

        if (!w.isEmpty()) {
            salida.add("(" + (diccionario.get(w) - 1) + "," + w.charAt(w.length() - 1) + ")");
        }

        LZWResultado resultado = new LZWResultado();
        resultado.codigos = salida;
        resultado.diccionario = diccionario;

        return resultado;
    }

    static class LZWResultado {
        List<String> codigos;
        Map<Integer, String> diccionario;

        LZWResultado() {
            this.codigos = new ArrayList<>();
            this.diccionario = new HashMap<>();
        }
    }
}
