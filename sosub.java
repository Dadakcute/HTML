import java.util.Scanner;

public class sosub {
    public static void main(String[] args)
    {
        Scanner tc = new Scanner(System.in);

        System.out.print("Digite um número: ");
        double num1 = tc.nextDouble();

        System.out.print("Digite um segundo número: ");
        double num2 = tc.nextDouble();

        if (num1 > num2) {
            System.out.println("Como o primeiro número é maior que o segundo, foi realizada um soma entre os dois números. O resultado é: " + (num1 + num2));
        } else {
            System.out.println("Como o segundo número é maior que o segundo, foi realizada uma subtração entre esses dois números. O resultado é: " + (num2 - num1));
        }
        tc.close();
    }
    
}
