import java.time.LocalTime;
import java.util.Scanner;

public class tempolocal6 {
    public static void main(String[] args)
    {
        Scanner teclado = new Scanner (System.in);

        int hora = LocalTime.now().getHour();
        System.out.print("Digite seu nome: ");
        String nome = teclado.nextLine();
        System.out.print("Digite sua idade: ");
        int idade = teclado.nextInt();

        String cumprimento;
        if (hora >= 5 && hora <12) {
            cumprimento = "Bom dia, ";
        } else if (hora >= 12 && hora < 18){
            cumprimento = "Boa tarde, ";
        } else if (hora >= 18 && hora <22){
            cumprimento = "Boa noite, ";
        } else {
            cumprimento = "Vai dormir, ";
        }
        
        System.out.println(cumprimento + nome + "!");

        if (idade < 18) {
            System.out.println("Entrada não permitida!");
        } else {
            System.out.println("Entrada liberada!");
        }
        teclado.close();
    }
    
}
