#!/bin/env python
import os
from getpass import getpass
from termcolor import colored
import socket
import hashlib
users = {
'nickname': '',
'password': ''
}
isRoot = False

def ErrorLine(msg):
    print(colored(msg, 'red'))

def PassLine(msg):
    print(colored(msg, 'green'))

PassLine('Konveer started!')
mode = input('[1] Sign up | [2] Sign in: ')
if(mode == '1'):
    users['nickname'] = input('[?] Enter nickname: ')
    isLocked = False
    clients_file = open('.pass', 'r')
    client = clients_file.readline()
    while client:
        _temp_client = client.partition(':')[0]
        if(users['nickname'] == _temp_client):
            isLocked = True
            break
        else:
            client = clients_file.readline()
    clients_file.close()

    if(not isLocked):
        PassLine(f"[*] {users['nickname']} connected!")
        _password = input(f"[?] Enter password for {users['nickname']}: ")
        _password1 = input(f"[?] Verify password for {users['nickname']}: ")
        if _password != '':
            if(_password == _password1):
                users['password'] = hashlib.sha256(bytes(_password, 'utf-8')).hexdigest()
            else:
                ErrorLine('[*] Password uncorrect!')
                exit()
        else:
            exit()

        pass_file = open('.pass', 'a')
        pass_file.write(users['nickname'] + ':' + users['password'] + '\n')
        pass_file.close()
        mode = '2'
    else:
        ErrorLine('Nickname is already in use')

if(mode == '2'):
    print("[*] Enter your login and password")
    _log = input('[?] Login: ')
    _pas = getpass('[?] Password: ')
    isDetected = False
    if(_log != '' and _pas != ''):

        file_password = open('.pass', 'r')
        log = file_password.readline()
        while log:
            logging = log.partition(':')
            if(_log == logging[0]):
                isDetected = True
                break
            else:
                log = file_password.readline()
        file_password.close()

        if(isDetected == True):
            if(str(hashlib.sha256(bytes(_pas, 'utf-8')).hexdigest()) == str(logging[2]).rstrip()):
                PassLine('[!] Entering to system')
                isRoot = True
            else:
                ErrorLine('[*] Password uncorrect!')
        else:
            ErrorLine('[*] User not found!')
    else:
        _log = input('[?] Login: ')
        _pas = getpass('[?] Password: ')

if(isRoot):
    print("[!] Enter 'quit()' to close app.")
    msg = ''
    while(msg.lower() != 'quit()'):
        PassLine('[1] Add new contact | [2] Choose existing: ')
        msg = input(f"{logging[0]} => ")
        if(msg == '1'):
            contact_mode = '1'
        elif(msg == '2'):
            contact_mode = '2'
        else:
            ErrorLine('Undefined Error!')
            break

        _contact_file = open('.contacts', 'r+')
        if(contact_mode == '1'): # Add new contact
            _contact_name = input('Enter contact nickname: ')

            __contact_counter = _contact_file.readline().partition(':')
            _contact_counter = __contact_counter[2]
            print(_contact_counter)

            for i in _contact_counter[0]:
                _temp_contact = _contact_file.readline().partition(':')[i+3]
                if(_contact_name == _temp_contact):
                    print('Contact already added')
                    break
                else:
                    _contact_file.write(_contact_name)
                    print(f'{_contact_name} is added')


            _all_users_list = open('.pass', 'r')

            _all_users_list.close()

        elif(contact_mode == '2'): # Choose contact
            _all_local_contacts = open('.contacts', 'r')
            __temp = _all_local_contacts.readline().partition(':')
            _temp = __temp[2].rstrip(',')
            print(f'Your contacts: {_temp}')

            msg = input(f"{logging[0]} => ")
            for clients in _temp:

                print(clients)

                if(msg == clients):
                    msg = input(f"{logging[0]} => {clients}")
                    break
                else:
                    print('Undefined contact')
                    break

        _contact_file.close()
        msg = input(f"{logging[0]} => ")

    online_file = open('.online', 'w')
    online.write(f"logging[0]")
    online_file.close()

else:
    pass

ErrorLine('[*] Closing...')
