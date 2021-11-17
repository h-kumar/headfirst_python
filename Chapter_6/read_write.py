def read_write():
    file = open('todos.txt','a')
    typein = input('Would you like to add a line?: ')

    if typein == 'Y':
        user_line = input('Ok what\'s the line?: ')
        print(user_line,file=file)
        file.close()
        print('Your line is recorded. Thank you.')
    else:
        print('Ok Bye Bye!')

read_write()