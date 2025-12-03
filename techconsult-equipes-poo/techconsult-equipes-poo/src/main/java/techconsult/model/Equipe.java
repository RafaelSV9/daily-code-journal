package techconsult.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Equipe {
    private String nome;
    private List<Consultor> consultores = new ArrayList<>();

    public Equipe(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return nome;
    }

    public void adicionar(Consultor c) {
        consultores.add(c);
    }

    public List<Consultor> ordenados() {
        List<Consultor> lista = new ArrayList<>(consultores);
        Collections.sort(lista);
        return lista;
    }
}
