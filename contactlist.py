# A program for managing your contact list.


dic = dict()


def add_contact():
    name = input('Enter name:')
    surname = input('Enter surname:')
    phone = input('Enter your number:')
    email = input('Enter email:')

    dic[name] = {'Surname': surname, 'Phone': phone, 'Email': email}
    print(f'Contact {name} added successfully!')


def view():
    print('Contact list')
    for name, item in dic.items():
        print(f'{name}: {item}')


def search():
    search_item = input('Enter your name or phone number to search for:')
    if search_item in dic:
        print(f'Contact found {search_item}: {dic[search_item]}')
    else:
        print(f'No contact with name or number {search_item} found.')


def del_cont():
    contact_del = input('Enter your name or phone number to be deleted:')
    if contact_del in dic:
        del dic[contact_del]
        print(f'Contact {contact_del} successfully deleted!')
    else:
        print(f'No contact with this name or number {contact_del} was found.')


add_contact()
add_contact()
view()
search()
del_cont()
view()