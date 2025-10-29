"""
Utility functions for the Todo application
"""

import json
from typing import List, Dict


def save_todos_to_file(todos: List[Dict], filename: str = "todos.json"):
    """Save todos to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(todos, f, indent=2)
    print(f"Todos saved to {filename}")


def load_todos_from_file(filename: str = "todos.json"):
    """Load todos from a JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def format_todo_count(count: int) -> str:
    """Format the todo count message"""
    if count == 0:
        return "No todos"
    elif count == 1:
        return "1 todo"
    else:
        return f"{count} todos"
