"""Console bot helper"""
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter user name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Invalid command format'
    return wrapper


def handle_hello():
    return 'How can I help you?'


@input_error
def handle_contact_add(contacts, command):
    _, name, phone = command
    contacts[name] = phone
    return f'Contact {name} added with phone number {phone}'


@input_error
def handle_contact_change(contacts, command):
    _, name, phone = command
    if contacts.get(name):
        contacts[name] = phone
        return f'Phone number for {name} changed to {phone}'
    else:
        return f'Contact {name} not found'


@input_error
def handle_contact_get_phone(contacts, command):
    name = command[1]
    return f'Phone number for {name} {contacts.get(name,"not found")}'


def handle_contact_get_all(contacts):
    if not contacts:
        return 'No contacts found'
    result = '\n'.join('{:<32}: {:<15}'.format(name, phone) for name, phone in contacts.items())
    return result


def main():
    contacts = {}

    while True:
        user_input = input('Enter command: ')

        # get only user command
        user_command = user_input.lower()

        # get only user data without command word
        user_command_data = user_input.split()

        if user_command in ['good bye', 'close', 'exit'] or '.' in user_input:
            print('Good bye!')
            break
        elif user_command == 'hello':
            print(handle_hello())
        elif user_command.startswith('add'):
            print(handle_contact_add(contacts, user_command_data))
        elif user_command.startswith('change'):
            print(handle_contact_change(contacts, user_command_data))
        elif user_command.startswith('phone'):
            print(handle_contact_get_phone(contacts, user_command_data))
        elif user_command == 'show all':
            print(handle_contact_get_all(contacts))
        else:
            print('Invalid command. Try again.')


if __name__ == '__main__':
    main()
