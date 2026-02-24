public class CelsiusToFahrenheit {
    public static void main(String[] args) {
    int celsius = 30;
    double fahrenheit = (celsius * 1.8) + 32;
    String mensagem = String.format("\nA temperatura de %d Celsius é equivalente a %.2f Fahrenheit\n", celsius, fahrenheit);
    System.out.println(mensagem);
    }
}