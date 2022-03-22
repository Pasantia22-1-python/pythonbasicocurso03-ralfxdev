from http import client
from setuptools import Command
import sys


clients = [
    {
        'name': 'Randy',
        'company': 'Google',
        'email': 'randy@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Alexander',
        'company': 'Facebook',
        'email': 'alexander@facebook.com',
        'position': 'Data Engineer',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the clients list')


def read_client():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client_name, updated_client):
    global clients

    flag = False

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            clients[idx] = updated_client
            flag = True

    if (not flag):
        _is_not_client()


def delete_client(client_name):
    global clients

    flag = False

    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            del clients[idx]
            flag = True
        
    if not flag:
        _is_not_client()


def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

    if not client_name:
        sys.exit()

    return client_name


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))
    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
         sys.exit()

    return client_name

def _is_not_client():
    return input('Client is not in clients list')

def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()
    command= input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        read_client()
    if command == 'R':
        read_client()
    elif command == 'U':
        client_name= _get_client_field('name')
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        update_client(client_name, client)
        read_client()
    elif command == 'D':
        client_name= _get_client_field('name')
        delete_client(client_name)
        read_client()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the client list')
        else:
            print('The client: {} is not in our client list'.format(client_name))
else:
    print('Invalid command')