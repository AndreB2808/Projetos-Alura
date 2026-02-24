import  java.util.Scanner;

public class Leitura {
    public static void main(String[] args) {
        Scanner le = new Scanner(System.in);
        System.out.print("Insira um filme: ");
        String filme = le.nextLine();
        System.out.print("Insira um ano: ");
        int ano = le.nextInt();
        System.out.print("Insira sua nota para o filme: ");
        double nota = le.nextDouble();
        
        System.out.println("Filme inserido: " + filme);
        System.out.println("Ano inserido: " + ano);
        System.out.println("Nota inserida: " + nota);
        le.close();
    }
}
