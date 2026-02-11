import java.util.Scanner;

public class comparacao2 {
    public static void main(String[] args)
{
    Scanner teclado = new Scanner(System.in);
    System.out.print("Digite um número: ");
    double num1 = teclado.nextDouble();
    System.out.print("Digite um segundo número: ");
    double num2 = teclado.nextDouble();
    if (num1 > num2) {
        System.out.println("O número maior é: " + (num1));
    } else {
        System.out.println("O número maior é: " + (num2));
    }
    teclado.close();
}
}
