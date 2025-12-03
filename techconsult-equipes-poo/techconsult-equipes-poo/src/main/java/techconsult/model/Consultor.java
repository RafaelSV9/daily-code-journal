package techconsult.model;

public abstract class Consultor implements Comparable<Consultor> {
    protected String nome;
    protected String nivel;
    protected String especialidade;

    public Consultor(String nome, String nivel, String especialidade) {
        this.nome = nome;
        this.nivel = nivel;
        this.especialidade = especialidade;
    }

    public String getNome() {
        return nome;
    }

    public String getNivel() {
        return nivel;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    @Override
    public int compareTo(Consultor outro) {
        return this.nome.compareTo(outro.nome);
    }
}
