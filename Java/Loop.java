import java.util.Scanner;

public class Loop {
    public static void main(String[] args) {
        Scanner le = new Scanner(System.in);
        double mediaAvaliacao = 0;
        double nota;

        for (int i = 0; i < 3; i++) {
            System.out.print("Diga sua avaliação para o filme:  ");
            nota = le.nextDouble();
            mediaAvaliacao += nota;
        }

        System.out.println("Média de avaliações: " + mediaAvaliacao/3);

    }
}