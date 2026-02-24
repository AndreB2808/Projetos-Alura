import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {
        Scanner le = new Scanner(System.in);
        String nome, tipoC, option;
        double cash;

        System.out.printf("\nIniciando o sistema de cadastro de clientes...\n");
        System.out.printf("Insira o nome do usuário: ");
        nome = le.nextLine();
        System.out.printf("Insira o tipo de conta: ");
        tipoC = le.nextLine();
        System.out.printf("Insira o saldo inicial: ");
        cash = le.nextDouble();
        System.out.printf("\n-----------------------------------------------------\n");
        System.out.printf("Nome do usuário: %s\n", nome);
        System.out.printf("Tipo de conta: %s\n", tipoC);
        System.out.printf("Saldo disponível: R$%.2f\n", cash);
        System.out.printf("-----------------------------------------------------\n");

        do {
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        System.out.printf("\n| Opções |\n");
        System.out.printf("\n[1] - Sacar dinheiro\n");
        System.out.printf("[2] - Depositar dinheiro\n");
        System.out.printf("[3] - Consultar saldo\n");
        System.out.printf("[4] - Sair\n");
        System.out.printf("\nSelecione a opção desejada: ");
        option = le.next();

        switch (option) {
            case "1":
                System.out.printf("\nDigite o valor que deseja sacar: ");
                double saque = le.nextDouble();
                if (saque > cash) {
                    System.out.printf("\nSaldo insuficiente para saque! Tente novamente!\n");
                } else {
                    cash -= saque;
                    System.out.printf("\nSaque de R$%.2f realizado com sucesso!\n", saque);
                    System.out.printf("Novo saldo: R$%.2f\n", cash);
                }
                break;
            case "2":
                System.out.printf("\nDigite o valor que deseja depositar: ");
                double deposito = le.nextDouble();
                cash += deposito;
                System.out.printf("\nDepósito de R$%.2f realizado com sucesso!\n", deposito);
                System.out.printf("Novo saldo: R$%.2f\n", cash);
                break;
            case "3":
                System.out.printf("\nSeu saldo atual é: R$%.2f\n", cash);
                break;
            case "4":
                System.out.printf("\nSaindo do sistema. Até logo!\n\n");
                break;
            default:
                System.out.printf("\nOpção inválida! Tente novamente.\n");
        }
    }    while (!option.equals("4"));
        le.close();
    }
}
