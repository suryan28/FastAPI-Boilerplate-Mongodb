# FastAPI Boilerplate with MongoDB

## Overview
This project is a boilerplate for building FastAPI applications with MongoDB. It provides a structured setup, best practices, and pre-built functionalities to accelerate development.

## Features
- **FastAPI Framework** – High-performance web APIs.
- **MongoDB Integration** – Uses `motor` for async database operations.
- **CRUD Operations** – Predefined API endpoints.
- **Auto-generated API Docs** – Swagger & Redoc support.

## Installation
First, ensure you have FastAPI and Motor installed in your environment.

```sh
pip install fastapi[all] motor
```

## Running the Application
Start the FastAPI server:

```sh
python main.py
```

By default, the API will be available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`
