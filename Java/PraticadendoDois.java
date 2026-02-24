import java.util.Scanner;

public class PraticadendoDois {
    public static void main(String[] args) {
        Scanner le = new Scanner(System.in);
        double nota1 = 8.1;
        double nota2 = 7.3;
        double media = (nota1 + nota2) / 2;
        System.out.println(String.format("Média das notas: %.2f", media));
        double vaiVirarInt = 1.55;
        int convertido = (int) vaiVirarInt;
        System.out.println(convertido);
        String palavra = "Palavra que começa com a letra ";
        char letra = 'C';
        String frase = palavra + letra;
        System.out.println(frase);
        double precoProduto = 23.99;
        int quantidade = 3;
        double valorTotal = precoProduto * quantidade;
        System.out.println(String.format("Preço do produto: %.2f || Quantidade: %d || Valor total: %.2f", precoProduto, quantidade, valorTotal));
        double valorEmDolar = 7.55;
        double conversaoReal = valorEmDolar * 4.94;
        System.out.println(String.format("Valor em dolar: %.2f ||Valor em reais: %.2f", valorEmDolar, conversaoReal));
        double precoOriginal = 87.99;
        double percentualDesconto = 35;
        double valorDesconto = ((100 - percentualDesconto) * 0.01) * precoOriginal;
        System.out.println(String.format("Preço original: %.2f || Desconto: %.0f%% || Valor do produto com desconto: %.2f", precoOriginal, percentualDesconto, valorDesconto));
        System.out.print("Digite um número inteiro: ");
        int numero = le.nextInt();

        if (numero % 2 == 0) {
            System.out.println("O número é par.");
        } else {
            System.out.println("O número é ímpar.");
        }

        System.out.println("Tabuada do " + numero + ":");
        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));
        }
    }
}
