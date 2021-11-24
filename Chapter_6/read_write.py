def write_to_file():
    """Append User input based on User's confirmation."""
    while True:
        writein = input('Would you like to add a line?: (Y or N) ')

        if writein == 'Y':
            with open('./todos.txt','a') as todos:
                user_line = input('Ok what\'s the line?: ')
                print(user_line, file=todos)
                print('Your line is recorded. Thank you.')
                todos.close()
                read_from_file()
                break
        elif writein == 'N':
            read_from_file()
            break
        else:
            validate_input(writein)


def read_from_file():
    """Display file contents based on User confirmation."""
    while True:
        view_line = input('Would you like to view the file contents?: ')
        if view_line == 'Y':
            with open('./todos.txt') as todos:
                for lines in todos:
                    print(lines)
                break
        elif view_line == 'N':
            print('Ok, Bye!')
            break
        else:
            validate_input(view_line)


def validate_input(user_input):
    """Validate User's input against acceptable Input values."""
    if user_input not in ['Y', 'N']:
        print('Try again')


write_to_file()
