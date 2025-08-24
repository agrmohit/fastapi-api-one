# 🚀 FastAPI API One

A simple FastAPI project demonstrating basic API functionalities like path parameters, request bodies, and different HTTP methods. This project is used for learning [FastAPI](https://fastapi.tiangolo.com).

## 📦 Installation

First, ensure you have `uv` installed. Then, install the project dependencies:

```bash
uv sync
```

## ▶️ How to Run

To start the development server with live reloading:

```bash
uv run uvicorn main:app --reload
```

## 📖 API Documentation

FastAPI has Swagger and Redoc support built-in. This project uses [Scalar](https://github.com/scalar/scalar) for enhanced API documentation.

Assuming the default development server URL [localhost:8000](http://localhost:8000), the documentation endpoints are:

- [Scalar `/scalar`](http://localhost:8000/scalar)
- [Swagger `/docs`](http://localhost:8000/docs)
- [Redoc `/redoc`](http://localhost:8000/redoc)

## ✨ Endpoints

Here are some of the available API endpoints:

- `GET /`: Returns a welcome message.
- `GET /items/{item_id}`: Retrieve an item by its ID.
- `PUT /items/{item_id}`: Update an item by its ID with a request body.
- `GET /users/me`: Get information about the current user.
- `GET /users/{user_id}`: Get information about a user by their ID.
