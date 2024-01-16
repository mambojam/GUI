FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read todos.txt file and return the list of todo items within it """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

  # file = open('todos.txt', 'r')
           # todos = file.readlines()
           # file.close()

        #with open('todos.txt', 'r') as file:
         #   todos = file.readlines()

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo list items in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(todos)