
def write_to_file():
    f = open('./todos.txt', 'a')
    while True:
        writein = input('Would you like to add a line?: (Y or N) ')
        if writein not in ['Y', 'N']:
            print('Try again')
            continue
        else:
            break
    if writein == 'Y':
        user_line = input('Ok what\'s the line?: ')
        print(user_line, file=f)
        print('Your line is recorded. Thank you.')
        f.close()
        read_from_file()
    elif writein == 'N':
        read_from_file()
    else:
        print('Ok, Bye!')


def read_from_file():
    f = open('./todos.txt')
    view_line = input('Would you like to view the file contents?: ')

    if view_line == 'Y':
        for lines in f:
            print(lines, end='')
    else:
        print('Ok, Bye!')
    f.close()


write_to_file()
