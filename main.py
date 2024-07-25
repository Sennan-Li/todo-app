
todos = []

while 1:
    user_action = input("What do you want to do? Add? Show? Exit? Please type:").title().strip()
    match user_action:
        case "Add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "Show":
            for item in todos:
                print(item)
        case "Exit":
            break
    print(todos)

