import java.util.Random;
import java.util.Scanner;

public class Adivinha {
    public static void main(String[] args) {
        Scanner le = new Scanner(System.in);
        System.out.println("\nBem-vindo ao jogo de adivinhação!\n");
        int secret = new Random().nextInt(100);
        for (int tentativa = 1; tentativa <= 5; tentativa++) {
            System.out.println(String.format("Tentativa %d/5", tentativa));
            System.out.print("Insira o seu chute: ");
            int chute = le.nextInt();
            if (chute == secret) {
                System.out.println("Parabéns! Você acertou!");
                break;
            } else if (chute < secret) {
                System.out.println("Tente um número maior.");
            } else {
                System.out.println("Tente um número menor.");
            }
        }
        System.out.println("Fim do jogo!");
    }
}