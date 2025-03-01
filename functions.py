FILEPATH='files/todo.txt'

def get_todos(filename=FILEPATH):
    """Read a file and return the list of todo items"""
    with open(filename, 'r') as file:
            todo_list_local = file.readlines()
    return todo_list_local

def write_todos(todo_arg, filename=FILEPATH):
    """Write the to-do items in a text file"""
    with open(filename, 'w') as file:
            file.writelines(todo_arg)




if __name__ == '__main__':  
    print('hello from functions')