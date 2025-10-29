"""
Main entry point for the Todo application
"""

from todo import TodoList

def main():
    print("=== Todo List Manager ===")
    todo_list = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. Add todo")
        print("2. List todos")
        print("3. Complete todo")
        print("4. Total assigned time")
        print("5. Exit")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == "1":
            title = input("Enter todo title: ").strip()
            description = input("Enter description (optional): ").strip()
            time = input("How many hours will it take? (optional): ").strip()
            todo_list.add_todo(title, description, time)
            print("Todo added!")
        
        elif choice == "2":
            todo_list.list_todos()
        
        elif choice == "3":
            todo_list.list_todos()
            try:
                index = int(input("Enter todo number to complete: ").strip()) - 1
                if todo_list.complete_todo(index):
                    print("Todo marked as complete!")
                else:
                    print("Invalid todo number!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice =="4":
            todo_list.list_todos()
            time = todo_list.compute_todo_time()
            print("This would take {} hours".format(time))

        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
