'''
Написать мини программу, которая будет проверять пароль пользователя
и если пароль подходит будет авторизировать пользователя:

Программа должна хранить Имена и Пароли в глобальном словаре
Должна содержать три функции:

1. check_password() возвращающая -> bool
2. authenticate() -> bool
3. login() принимающая минимум 2 аргумента username, password возвращающая -> bool
4. функция login() должна быть с декоратором в котором будет вся логика проверки check_password и authenticate
5. у пользователя должно быть 3 попытки после чего программа завершается и выводит сообщение "Попытки истекли!",
при каждой не удачной попытки должно быть сообщение "У вас осталось Н попыток"

Сценарий: пользователь с консоли вводит Имя и Пароль,
программа возвращает текст "Вы в системе!" или "Не правильное Имя или Пароль"
'''

import argparse
from functools import wraps

users = {
    'Alex': "123",
    'Pep': "008",
    'Lex': "123"}


def login_decorator(func):
    @wraps(func)
    def wrapper(username, password):
        if not check_password(username, password):
            print('Не правильное Имя или Пароль')
            return False
        if not authenticate():
            return False
        return func(username, password)

    return wrapper


def check_password(username: str, password: str) -> bool:
    if (username, password) in users.items():
        return True


def authenticate() -> bool:
    print('Вы в системе!')
    return True


@login_decorator
def login(_username: str, _password: str) -> bool:
    return True


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store", help="Username")
    parser.add_argument("-p", "--password", action="store", help='Password')
    args = parser.parse_args()
    return args.username, args.password


if __name__ == "__main__":
    username, password = parse_args()
    if username and password:
        if login(username, password):
            exit()
        else:
            username, password = None, None
    i = 3
    while i > 0:
        if login(username or input('Введите ваш логин:'),
                 password or input('Введите ваш пароль:')):
            break
        i -= 1
        print(f'Оталось попыток: {i}')
    else:
        print('Попытки истекли!')
