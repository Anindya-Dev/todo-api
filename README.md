# 📝 FastAPI Todo API

A simple **Todo REST API** built using **FastAPI, SQLAlchemy, and SQLite**.
This project demonstrates how to build a backend API with **CRUD operations** using modern Python frameworks.

The API allows users to:

* Create a todo
* View all todos
* View a specific todo
* Update completion status
* Delete a todo

---

# 🚀 Tech Stack

* Python
* FastAPI
* SQLAlchemy (ORM)
* SQLite
* Pydantic

---

# 📂 Project Structure

```
todo-api
│
├── main.py
├── todo.db
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Anindya-Dev/todo-api.git
cd todo-api
```

---

### 2️⃣ Create a virtual environment (optional but recommended)

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn sqlalchemy pydantic
```

---

# ▶️ Running the Server

Start the FastAPI server:

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📘 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

## Root Endpoint

**GET /**

Response

```
{
  "message": "Todo API is running"
}
```

---

## Create Todo

**POST /todos**

Request body

```
{
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## Get All Todos

**GET /todos**

Response

```
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  }
]
```

---

## Get Specific Todo

**GET /todos/{id}**

Example

```
/todos/1
```

Response

```
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## Update Todo Completion

**PUT /todos/{id}**

Example

```
/todos/1?completed=true
```

Response

```
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": true
}
```

---

## Delete Todo

**DELETE /todos/{id}**

Response

```
{
  "message": "Todo deleted successfully"
}
```

---

# 💾 Database

The application uses **SQLite**.

The database file:

```
todo.db
```

It is automatically created when the application runs.

---

# ✨ Features

* RESTful API design
* SQLAlchemy ORM integration
* FastAPI automatic documentation
* SQLite lightweight database
* Full CRUD operations
* Boolean completion tracking for todos

---

# 📜 License

This project is open-source and available for learning and educational purposes.
