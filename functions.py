def writeFile(todos, filename="ToDoData.txt"):
    with open(filename, "w") as file:
        if todos:
            return file.writelines(sorted(todos))


def readFile(filename="ToDoData.txt"):
    with open(filename) as file:
        todos = file.readlines()
    return todos
