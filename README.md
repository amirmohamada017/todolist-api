# Todo List API

A RESTful API for managing todo list with user authentication using Django, Django REST Framework, and MySQL.

## Features

-   User registration, login, and token refresh.
-   CRUD operations for to-do items (create, read, update, delete).
-   Each user can manage their own to-do list.
-   Only authenticated users can access their own to-do items.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/amirmohamada017/todolist-api.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the MySQL database:

    - Update your `settings.py` with your MySQL configuration.

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

-   Register: `POST /auth/register/`

    -   Request Body: `{ "username": "user", "email": "user@example.com", "password": "password123" }`
    -   Response: 201 Created

-   Login: `POST /auth/login/`

    -   Request Body: `{ "username": "user", "password": "password123" }`
    -   Response: 200 OK (Returns access and refresh tokens)

-   Refresh Token: `POST /auth/refresh/`
    -   Request Body: `{ "refresh": "your-refresh-token" }`
    -   Response: 200 OK (Returns new access token)

### Todo Endpoints (Authenticated Users Only)

-   Create a Todo: `POST /todos/`

    -   Request Body: `{ "title": "Buy groceries", "description": "Milk, eggs, bread" }`
    -   Response: 201 Created

-   Get All Todos: `GET /todos/`

    -   Response: 200 OK (Returns list of todos)

-   Get a Todo by ID: `GET /todos/<id>/`

    -   Response: 200 OK

-   Update a Todo: `PUT /todos/<id>/`

    -   Request Body: `{ "title": "Updated title", "description": "Updated description" }`
    -   Response: 200 OK

-   Delete a Todo: `DELETE /todos/<id>/`
    -   Response: 204 No Content

## Project Source

This project was completed as part of the project ideas listed on [roadmap.sh](https://roadmap.sh/).

[https://roadmap.sh/projects/todo-list-api](https://roadmap.sh/projects/todo-list-api).
