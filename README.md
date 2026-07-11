# Todo List

A Django web application for managing tasks and tags.

## Features

- Create, update and delete tasks
- Create, update and delete tags
- Mark tasks as completed
- Undo completed tasks
- Optional deadline for tasks
- Multiple tags for a task
- Sidebar navigation
- Django admin panel
- Bootstrap UI

## Models

### Task

- content
- created_at
- deadline
- is_done
- tags

### Tag

- name

## Relationships

- One task can have multiple tags
- One tag can belong to multiple tasks

## Installation

```bash
git clone https://github.com/matus332/Todo-List.git
cd Todo-List
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

## Screenshots

Screenshots are attached to the Pull Request.