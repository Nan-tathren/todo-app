while True:
    user=input("Type add, show, edit, complete or quit\n")
    user=user.strip()
    if user.startswith('add') or user.startswith('new'):
        todo=user[4:]

        with open('todos.txt','r') as file:
                todos=file.readlines()

        with open('todos.txt','w') as file:
                file.writelines(todos)

    elif user.startswith('show'):
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index,item in enumerate(todos):
                item=item.strip('\n')
                print(f'{index+1}-{item}')

    elif user.startswith('edit'):
        try:
            number=int(user[5:])
            number=number-1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

                new_todo=input("Enter edited TODO\n")
                todos[number]=new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Nope, you need to input a number')
            continue

    elif user.startswith('complete'):
        try:
            number = int(user[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index=number-1
            todo_to_remove=todos[index].strip('\n')

            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)

            message=f"TODO '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("Out of range, not that many TODOs.")
            continue

    elif user.startswith('quit') or user.startswith('exit'):
        break

    else:
        print('Command is not valid.')

print('Bye')