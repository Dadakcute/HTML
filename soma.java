import java.util.Scanner;

public class soma {
    public static void main(String[] args)
    {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um número: ");
        double num1 = teclado.nextDouble();
        System.out.print("Digite um segundo número: ");
        double num2 = teclado.nextDouble();
        System.out.println("A soma dos 2 números é: "+ (num1 + num2));
        teclado.close();

    }
}
