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

username = input('Введите логин: ')
password = input('Введите пароль: ')
users = {
    'Alex': "123",
    'Jon': "321",
    'Lex': "123"}


def login(func):
    def chek(func):
        if not check_password(username, password):
            func()
            return False
        if not authenticate():
            return False

    return chek(func)


def check_password(_username: str, _password: str) -> bool:
    if (username, password) in users.items():
        return True


def authenticate() -> bool:
    if check_password(username, password):
        print('Вы в системе!')
        return True


@login
def decorator():
    print('Не правильное Имя или Пароль')


i = 4
while i > 1:
    if authenticate():
        break
    i -= 1
    print(f'Оталось попыток: {i}')
    username, password = (input('Введите логин: '), (input('Введите пароль: ')))
else:
    print('Попытки истекли!')
