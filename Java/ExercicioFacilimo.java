public class ExercicioFacilimo {
    public static void main(String[] args) {
        System.out.println("\nOlá Alura!");
        System.out.println("\nTudo bom?\n");
        System.out.println(10 + 5);
        System.out.println(10 - 5);     
        String tentativa = "1324";
        String senha = "1234";
        if (tentativa.equals(senha)) {
            System.out.println("Acesso concedido");
        } else {
            System.out.println("Acesso negado");
        }
        String nome = "Alura";
        int idade = 30;
        double valor = 55.9999;
        System.out.println(String.format("""
        Meu nome é %s, eu tenho %d anos e hoje gastei %.2f reais
                """, nome, idade, valor));
        double media = (1.5 + 8.3 + 9.7) / 3;
        // Casting \/ 
        int classificar = (int) media / 2;
        System.out.println(classificar);
    }
}
