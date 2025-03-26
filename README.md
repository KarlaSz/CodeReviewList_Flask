# Task List Application (Flask)

This is a simple task management application built with Flask, using SQLAlchemy for database management and Flask-Migrate for handling database migrations.
![image](https://github.com/user-attachments/assets/035554ee-08fc-4d21-87dd-24d67764af40)

![image](https://github.com/user-attachments/assets/b440a20b-7287-4f34-80e5-52d449bc92ab)

## Features

- **Add new tasks**: Create new tasks with a name and priority.
- **Edit tasks**: Modify task names.
- **Delete tasks**: Remove tasks from the list.
- **Mark tasks as done**: Toggle task completion status.
- **API support**: The app includes RESTful APIs for task management.
  - **GET** `/api/task` - Retrieve all tasks.
  - **POST** `/api/task` - Create a new task.
  - **POST** `/api/task/<int:task_id>` - EDIT details of a single task.
  - **DELETE** `/delete_task/<int:task_id>` - Delete a task.

## Requirements

- Python 3.7 or later
- Flask
- SQLAlchemy
- Flask-Migrate

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/your-repository.git
