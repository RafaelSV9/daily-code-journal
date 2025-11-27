import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.Scanner;

public class DailyCodeLogger {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Daily Code Journal ===");

        System.out.print("O que você estudou hoje? ");
        String studied = sc.nextLine();

        System.out.print("Quanto tempo estudou/codou (minutos)? ");
        String minutes = sc.nextLine();

        System.out.print("O que você quer fazer amanhã? ");
        String tomorrow = sc.nextLine();

        String date = LocalDate.now().toString();

        String entry = "\n" +
                "Data: " + date + "\n" +
                "Estudo: " + studied + "\n" +
                "Tempo: " + minutes + " min\n" +
                "Plano amanhã: " + tomorrow + "\n" +
                "-----------------------------\n";

        try (FileWriter fw = new FileWriter("journal.txt", true)) {
            fw.write(entry);
            System.out.println("✔ Log adicionado no journal.txt!");
        } catch (IOException e) {
            System.out.println("Erro ao salvar o log: " + e.getMessage());
        }

        sc.close();
    }
}
