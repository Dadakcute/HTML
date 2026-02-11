import java.util.Scanner;

public class comparacao3 {
    public static void main(String[] args)
{
    Scanner teclado = new Scanner(System.in);
    System.out.print("Digite um número: ");
    double num1 = teclado.nextDouble();
    System.out.print("Digite um segundo número: ");
    double num2 = teclado.nextDouble();
    System.out.print("digite um terceiro número: ");
    double num3 = teclado.nextDouble();

    if (num1 > num2 && num1 > num3) {
        System.out.println("O primeiro é o maior: "+ (num1));
    } else if (num2 > num1 && num2 > num3){
        System.out.println("O segundo é o maior: "+ (num2));
    } else{
        System.out.println("O terceiro é o maior: "+ (num3));
    } 
    teclado.close();
}
}
