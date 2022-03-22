from http import client
from setuptools import Command
import sys


clients = ['randy', 'alexander']


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the clients list')


def read_client():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        _is_not_client()


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _is_not_client()


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


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
        client_name = _get_client_name()
        create_client(client_name)
        read_client()
    if command == 'R':
        read_client()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the updated client name? ')
        update_client(client_name, updated_name)
        read_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        read_client()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client list')
        else:
            print('The client: {} is not in our client list'.format(client_name))
else:
    print('Invalid command')