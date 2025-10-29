"""
Simple Todo Application
A basic command-line todo list manager for learning git commands.
"""

class Todo:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"


class TodoList:
    def __init__(self):
        self.todos = []
    
    def add_todo(self, title, description=""):
        todo = Todo(title, description)
        self.todos.append(todo)
        return todo
    
    def list_todos(self):
        if not self.todos:
            print("No todos yet!")
            return
        
        for i, todo in enumerate(self.todos, 1):
            print(f"{i}. {todo}")
    
    def complete_todo(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index].mark_complete()
            return True
        return False


if __name__ == "__main__":
    todo_list = TodoList()
    
    # Add some initial todos
    todo_list.add_todo("Learn git basics")
    todo_list.add_todo("Practice branching")
    todo_list.add_todo("Try merging")
    
    # Display todos
    todo_list.list_todos()
