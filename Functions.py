FILEPATH = 'todos.txt'

def get_todos(file_address=FILEPATH):
  with open(file_address, 'r') as local_file:
    todos_local = local_file.readlines()
  return todos_local


def set_todos(updated_list, file_address=FILEPATH):
  with open(file_address, 'w') as local_file:
    local_file.writelines(updated_list)