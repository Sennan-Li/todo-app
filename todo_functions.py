def get_todos():
    with open("todos.txt", "r") as file:
        todo_list = file.readlines()
        return todo_list

def write_todos(todo_list):
    with open("todos.txt", "w") as file:
        file.writelines(todo_list)
