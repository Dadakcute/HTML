import java.util.Scanner;
import java.util.Arrays;

public class ordemcrescente {
    public static void main(String[] args)
    {
        Scanner teclado = new Scanner(System.in);
        
        int numeros[] = new int[5];

        for (int i = 0; i <5; i++) {
            System.out.print("Digite um número: ");
            numeros[i] = teclado.nextInt();
            }
        Arrays.sort(numeros);
        System.out.println("Os números digitados, na ordem decrescente, são: ");

        for (int i = 0; i <5 ; i++) {
            System.out.print(numeros[i]);
            if (i <4){
                System.out.print(", ");
                }
            }
    teclado.close();   }
    }

