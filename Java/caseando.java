public class caseando {
    public static void main(String[] args) {
        int dia = 6;
        String nomeDia;

        nomeDia = switch (dia) {
            case 1 -> "domingo";
            case 2 -> "segunda-feira";
            case 3 -> "terça-feira";
            case 4 -> "quarta-feira";
            case 5 -> "quinta-feira";
            case 6 -> "sexta-feira";
            case 7 -> "sábado";
            default -> "Dia inválido";
        };

        System.out.println("O dia " + dia + " é " + nomeDia);
    }
}
