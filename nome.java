import java.util.Scanner;

public class nome {
    public static void main(String[] args)
    {
        Scanner teclado= new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = teclado.nextLine();
        System.out.println("Bom dia, " + (nome));
        teclado.close();
    }
}
