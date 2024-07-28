from todo_functions import get_todos, write_todos
import datetime as dt


while 1:
    user_action = input("What do you want to do? Add? Show? Edit? Complete? Exit? Please type:").lower().title().strip()

    if user_action.startswith("Add"):
        todos = get_todos()
        todo = user_action[3:].strip() + "\n"
        todos.append(todo)

        write_todos("todos.txt", todos)
        print(f"Todo has been added.\n{dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")}")

    elif user_action.startswith("Show"):
        todos = get_todos()
        if len(todos) != 0:
            print(f"Here are all the todos: {dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")}")
            [print(f'{index + 1}.{item.strip("\n")}') for index, item in enumerate(todos)]

        else:
            print("There are no todos.")

    elif user_action.startswith("Edit"):
        todos = get_todos()
        try:
            number = int(user_action[-1])
            index = number - 1
            if not number > len(todos):
                todos[index] = input("Edit the todo: ") + "\n"

                write_todos("todos.txt", todos)
                print(f'Todo {number} has been edited.\n{dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")}')
            else:
                print(f'Todo {number} does not exist.')
                continue
        except ValueError:
            print(f'Please make sure the text ends with number.')

    elif user_action.startswith("Complete"):
        todos = get_todos()
        try:
            number = int(user_action[-1])
            index = number - 1
            if not number > len(todos):
                todos.pop(index)
                write_todos("todos.txt", todos)
                print(f"Todo {number} has been completed.\n{dt.datetime.now().strftime("%d/%m/%y %H:%M:%S")}")
            else:
                print(f'Todo {number} does not exist.')
                continue
        except ValueError:
            print(f'Please make sure the text ends with number.')

    elif user_action.startswith("Exit"):
        break
    else:
        print("It is an invalid command")

print("Bye!")
