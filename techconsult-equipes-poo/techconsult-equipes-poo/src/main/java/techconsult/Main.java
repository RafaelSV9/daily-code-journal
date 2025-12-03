package techconsult;

import techconsult.model.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Map<String, Equipe> equipes = new HashMap<>();

        Equipe alpha = new Equipe("Alpha");
        alpha.adicionar(new ConsultorDados("Lucas", "Pleno"));
        alpha.adicionar(new ConsultorBackend("Bruno", "Senior"));
        alpha.adicionar(new ConsultorFrontend("Maria", "Junior"));
        equipes.put("Alpha", alpha);

        Equipe beta = new Equipe("Beta");
        beta.adicionar(new ConsultorBackend("Joao", "Junior"));
        beta.adicionar(new ConsultorDados("Ana", "Senior"));
        equipes.put("Beta", beta);

        String nomeEquipe = sc.nextLine();
        Equipe equipe = equipes.get(nomeEquipe);

        if (equipe == null) {
            System.out.println("Equipe nao encontrada");
        } else {
            List<Consultor> lista = equipe.ordenados();
            for (Consultor c : lista) {
                System.out.println(c.getNome() + " " + c.getEspecialidade() + " " + c.getNivel());
            }
        }

        sc.close();
    }
}
