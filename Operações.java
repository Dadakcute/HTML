import java.util.Scanner;

public class Operações {
    public static void main(String[] args)
    {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int num1 = teclado.nextInt();

        System.out.print("Digite um número: ");
        int num2 = teclado.nextInt();

        System.out.print("Digite um número: ");
        int num3 = teclado.nextInt();

        System.out.print("Digite um número: ");
        int num4 = teclado.nextInt();

        System.out.println("soma =" + (num1+num2));
        System.out.println("subtração =" + (num3-num4));
        System.out.println("divisão ="+ (num2/num3));
        System.out.println("multiplicação =" + (num4*num1));
        teclado.close();
    }
}