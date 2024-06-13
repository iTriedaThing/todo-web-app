import os.path
FILEPATH = 'todos.txt'


def read_todos(filepath=FILEPATH):
    """
    Retrieves the current items on the todos text file
    :param filepath:
    :return:
    """
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            todo_list = file.readlines()
    else:
        with open(filepath, 'w') as file:
            todo_list = file.readlines()
    return todo_list


def write_todos(todo_list, filepath=FILEPATH):
    """
    Record the list of todos back to the holding file

     """
    with open(filepath, 'w') as file:
        file.writelines(todo_list)

