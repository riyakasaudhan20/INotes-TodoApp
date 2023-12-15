# INotes - FastAPI Todo App

INotes is a simple Todo app built with FastAPI that enables users to create and manage their todos. It utilizes a MongoDB database to store and retrieve todo items.

## Features

- **Create Todo**: Users can easily create new todo items by specifying the task details.
- **Store in MongoDB**: Todos are stored persistently in a MongoDB database.
- **Fetch Todos**: Ability to retrieve all todos from the database.

## Requirements

- Python 3.7+
- FastAPI
- MongoDB

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/INotes.git
    cd INotes
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB:
    - Make sure MongoDB is installed and running locally or provide the connection details in the configuration.

4. Run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

## Configuration

In the `config.py` file, you can set up the MongoDB connection details:

```python
MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "inotes_db"
COLLECTION_NAME = "todos"

## Usage

Creating a Todo
Send a POST request to /todos/ endpoint with a JSON payload:
{
  "title": "Finish project",
  "description": "Complete the final report for the project"
}
Fetching Todos
Send a GET request to /todos/ endpoint to retrieve all todos.

##  API Endpoints
POST /todos/: Create a new todo.
GET /todos/: Retrieve all todos.
