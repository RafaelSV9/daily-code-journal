# TechConsult - Gestão de Equipes de Consultores (POO em Java)

Este projeto implementa, em Java, um sistema simples de **gestão de equipes de consultores** utilizando os pilares de **Programação Orientada a Objetos**: classes, encapsulamento, herança, polimorfismo e uso de coleções.

O domínio é baseado no enunciado de um desafio educacional: a empresa fictícia **TechConsult** organiza suas equipes de consultores (Backend, Frontend e Dados), e o sistema deve listar os consultores de uma equipe em ordem alfabética.

---

## ✅ Objetivo do sistema

- Modelar **consultores** com:
  - `nome`
  - `especialidade` (Backend, Frontend, Dados)
  - `nivel` de experiência (Junior, Pleno, Senior)
- Modelar **equipes**, cada uma contendo vários consultores de diferentes especialidades.
- Ao receber **o nome de uma equipe via entrada padrão (STDIN)**:
  - Se a equipe existir, listar os consultores **em ordem alfabética pelo nome**, um por linha, no formato:

    ```txt
    nome especialidade nivel
    ```

  - Se a equipe não existir, imprimir:

    ```txt
    Equipe nao encontrada
    ```

---

## 🧱 Estrutura de classes

Pacote `techconsult.model`:

- `Consultor` (abstrata)
  - Atributos:
    - `nome`
    - `nivel`
    - `especialidade`
  - Implementa `Comparable<Consultor>` para permitir ordenação por nome.
- `ConsultorBackend` (extends `Consultor`)
- `ConsultorFrontend` (extends `Consultor`)
- `ConsultorDados` (extends `Consultor`)
- `Equipe`
  - Atributos:
    - `nome`
    - `List<Consultor> consultores`
  - Métodos:
    - `adicionar(Consultor c)`
    - `ordenados()` → retorna lista de consultores ordenada por nome.

Pacote `techconsult`:

- `Main`
  - Cria equipes fixas (`Alpha` e `Beta`) com consultores pré-cadastrados.
  - Lê o nome da equipe via `Scanner`.
  - Busca a equipe em um `Map<String, Equipe>`.
  - Imprime os consultores da equipe em ordem, ou `"Equipe nao encontrada"`.

---

## 📂 Estrutura de pastas

```txt
techconsult-equipes-poo/
└── src/
    └── main/
        └── java/
            └── techconsult/
                ├── Main.java
                └── model/
                    ├── Consultor.java
                    ├── ConsultorBackend.java
                    ├── ConsultorFrontend.java
                    ├── ConsultorDados.java
                    └── Equipe.java
```

---

## ▶️ Como compilar e executar

Na raiz do projeto (`techconsult-equipes-poo`), execute:

### 1. Compilar

```bash
javac -d out $(find src -name "*.java")
```

Isso gera os `.class` dentro da pasta `out`.

### 2. Executar

```bash
cd out
java techconsult.Main
```

---

## 💻 Exemplos de uso

### Exemplo 1

**Entrada:**

```txt
Alpha
```

**Saída:**

```txt
Bruno Backend Senior
Lucas Dados Pleno
Maria Frontend Junior
```

### Exemplo 2

**Entrada:**

```txt
Beta
```

**Saída:**

```txt
Ana Dados Senior
Joao Backend Junior
```

### Exemplo 3

**Entrada:**

```txt
Gamma
```

**Saída:**

```txt
Equipe nao encontrada
```

---

## 🌱 Conceitos de POO aplicados

- **Encapsulamento**: atributos privados com acesso controlado via getters.
- **Herança**: `ConsultorBackend`, `ConsultorFrontend` e `ConsultorDados` herdam de `Consultor`.
- **Polimorfismo**: a lista de consultores (`List<Consultor>`) armazena objetos de diferentes subclasses.
- **Coleções**:
  - `List<Consultor>` para consultores de uma equipe.
  - `Map<String, Equipe>` para indexar equipes pelo nome.

Você pode usar este projeto como base para estudos, para desafios educacionais ou como exemplo de POO em Java no seu portfólio. 🚀
