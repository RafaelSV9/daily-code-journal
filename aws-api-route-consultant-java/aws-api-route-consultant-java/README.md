# AWS API Route Consultant (Java CLI)

Pequeno projeto em Java inspirado na jornada de estudos de **Backend com Java & AWS**.

A ideia é simular o dia a dia de um consultor que ajuda a padronizar rotas de APIs REST e a escolher serviços AWS adequados para diferentes demandas.

## 🎯 Objetivos do projeto

- Converter nomes de endpoints em **CamelCase** (ex.: `GetUserProfile`) para rotas RESTful padronizadas:
  - Padrão: `/api/v1/get-user-profile`
- Validar se uma rota segue regras básicas de padronização:
  - Começa com `/api/v1/`
  - Não termina com `/`
  - Usa apenas **letras minúsculas** e **hífens**
- Sugerir um serviço AWS com base em uma descrição simples de demanda:
  - EC2, S3, RDS, Lambda ou API Gateway

> Projeto pensado para ser simples, didático e ideal para portfólio de quem está estudando Java + AWS.

---

## 🧱 Estrutura

Pacote `awsconsult`:

- `Main`  
  - CLI que oferece um pequeno menu:
    - (1) Converter endpoint CamelCase em rota RESTful
    - (2) Validar rota RESTful
    - (3) Sugerir serviço AWS para uma demanda

- `EndpointConverter`  
  - Responsável por transformar `GetUserProfile` em `/api/v1/get-user-profile`.

- `RoutePatternValidator`  
  - Garante que a rota siga o padrão RESTful definido.

- `AwsService`  
  - Enum com alguns serviços básicos da AWS:
    - `EC2`, `LAMBDA`, `API_GATEWAY`, `S3`, `RDS`, `SERVICO_DESCONHECIDO`.

- `AwsRouteAdvisor`  
  - Implementa uma lógica simples de sugestão de serviço AWS com base em um texto:
    - "armazenar arquivos" → S3  
    - "subir servidor" → EC2  
    - "função sob demanda" → LAMBDA  
    - "banco de dados relacional" → RDS  
    - "rota http, eventos" → API_GATEWAY  

---

## ▶️ Como compilar e executar

Na raiz do projeto:

### 1. Compilar

```bash
javac -d out $(find src -name "*.java")
```

### 2. Executar

```bash
cd out
java awsconsult.Main
```

---

## 🧪 Exemplos rápidos

### 1) Converter endpoint CamelCase

Entrada (opção 1):

```text
GetUserProfile
```

Saída:

```text
Rota gerada: /api/v1/get-user-profile
```

---

### 2) Validar rota

Entrada (opção 2):

```text
/api/v1/create-invoice
```

Saída:

```text
Rota válida
```

---

### 3) Sugerir serviço AWS

Entrada (opção 3):

```text
preciso armazenar imagens e arquivos na nuvem
```

Saída:

```text
Serviço sugerido: S3
```

---

## 💡 Possíveis melhorias

- Transformar em API REST com Spring Boot.
- Persistir histórico de consultas em um banco.
- Expor essa lógica atrás de um API Gateway real na AWS.
- Dockerizar a aplicação.

---

Projeto ideal para treinar:

- Lógica com **Strings**
- Enum e regras de negócio simples
- Organização de código em pacotes
- Pensamento orientado a serviços na nuvem (AWS)

