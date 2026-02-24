public class Condicional {
    public static void main(String[] args) {
     int ano = 1981;
     boolean incluido = true;
     //double nota = 4.6;
     String plano = "PlusPlus";
     if (ano >= 2022) {
        System.out.println("Lançamentos recentes populares!");
     } else {
        System.out.println("Relíquias do passado!");
     }
     if (incluido == true && plano.equals("PlusPlus")) {
        System.out.println("Filme disponível para assistir!");
     } else {
        System.out.println("Filme indisponível para assistir!");
     }
    }
}
