# Task Manager Lite

Simple RESTful API for managing tasks, built with **Java 17 + Spring Boot 3 + H2**.

Ideal para portfólio: mostra domínio de API REST, camadas bem definidas (controller, service, repository) e uso de banco em memória.

---

## 🚀 Tecnologias

- Java 17
- Spring Boot 3 (Web, Data JPA, Validation)
- H2 Database (em memória)
- Maven

---

## 📂 Estrutura do Projeto

```text
task-manager-lite/
├── pom.xml
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── rafaelsv
│   │   │           └── taskmanager
│   │   │               ├── TaskManagerApplication.java
│   │   │               ├── controller
│   │   │               │   └── TaskController.java
│   │   │               ├── dto
│   │   │               │   ├── TaskRequest.java
│   │   │               │   └── TaskResponse.java
│   │   │               ├── model
│   │   │               │   └── Task.java
│   │   │               ├── repository
│   │   │               │   └── TaskRepository.java
│   │   │               └── service
│   │   │                   └── TaskService.java
│   │   └── resources
│   │       └── application.properties
```

---

## ⚙️ Como rodar

Pré-requisitos:

- Java 17 instalado
- Maven instalado

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/task-manager-lite.git
cd task-manager-lite
```

### 2️⃣ Rodar o projeto

```bash
mvn spring-boot:run
```

A API ficará disponível em:

```text
http://localhost:8080
```

---

## 📚 Endpoints principais

### 🔹 Listar todas as tarefas

`GET /api/tasks`

**Response 200 OK**

```json
[
  {
    "id": 1,
    "title": "Estudar Java",
    "description": "Praticar Spring Boot",
    "status": "PENDING",
    "createdAt": "2025-01-01T10:00:00",
    "updatedAt": "2025-01-01T10:00:00"
  }
]
```

---

### 🔹 Buscar tarefa por ID

`GET /api/tasks/{id}`

**Exemplo:**

```http
GET /api/tasks/1
```

---

### 🔹 Criar nova tarefa

`POST /api/tasks`

**Request body:**

```json
{
  "title": "Estudar Spring Boot",
  "description": "Criar uma API de tarefas",
  "status": "PENDING"
}
```

**Response 201 Created**

```json
{
  "id": 1,
  "title": "Estudar Spring Boot",
  "description": "Criar uma API de tarefas",
  "status": "PENDING",
  "createdAt": "2025-01-01T10:00:00",
  "updatedAt": "2025-01-01T10:00:00"
}
```

---

### 🔹 Atualizar uma tarefa (PUT)

`PUT /api/tasks/{id}`

**Request body:**

```json
{
  "title": "Estudar Spring Boot (atualizado)",
  "description": "Aprimorar API de tarefas",
  "status": "IN_PROGRESS"
}
```

---

### 🔹 Atualizar apenas o status (PATCH)

`PATCH /api/tasks/{id}/status`

**Request body:**

```json
{
  "status": "DONE"
}
```

---

### 🔹 Deletar tarefa

`DELETE /api/tasks/{id}`

**Response 204 No Content**

---

## 🧪 Validações

- `title` é obrigatório e tem limite de 100 caracteres.
- `description` tem limite de 1000 caracteres.
- `status` tem limite de 30 caracteres.
- Erros de validação retornam **400 Bad Request** com detalhes dos campos inválidos.

Exemplo:

```json
{
  "timestamp": "2025-01-01T10:00:00.000000",
  "status": 400,
  "errors": {
    "title": "Title is mandatory"
  }
}
```

---

## 🗄️ Banco de dados H2

Console do H2 disponível em:

```text
http://localhost:8080/h2-console
```

Config padrão:

- JDBC URL: `jdbc:h2:mem:tasksdb`
- User: `sa`
- Password: *(vazio)*

---

## 🌟 Ideias de evolução

- Paginação na listagem de tarefas
- Filtro por status (`/api/tasks?status=PENDING`)
- Autenticação JWT
- Documentação com OpenAPI/Swagger

---

## 📜 Licença

Projeto criado para estudo e portfólio. Fique à vontade para usar como base nos seus projetos.
