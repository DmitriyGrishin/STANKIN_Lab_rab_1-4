import os

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

from fetch_email import FetchEmail
from helpers import get_hash
from send_email import send_email as send_email_

def sign(path_private_key, path_file, path_elecwriter):
    try:
        f = open(path_private_key, 'r')
        key = RSA.import_key(f.read())
    except FileNotFoundError:
        raise FileNotFoundError('Приватный ключ не найден')

    h = get_hash(path_file)

    elecwriter = pkcs1_15.new(key).sign(h)
    f = open(path_elecwriter, 'wb')
    f.write(elecwriter)
    f.close()

    print(f'elecwriter saved - {path_elecwriter}')


def public_key(path_private_key, path_public_key):
    try:
        f = open(path_private_key, 'r')
        key = RSA.import_key(f.read())
    except FileNotFoundError:
        raise FileNotFoundError('Отсутствует приватный ключ')

    pubkey = key.publickey()
    repr_pubkey = pubkey.export_key('PEM')
    f = open(path_public_key, 'wb')
    f.write(repr_pubkey)
    f.close()

    print(f'Публичный ключ сохранен - {path_public_key}\n'
          f'{repr_pubkey.decode("utf-8")}')


def private_key(path):
    key = RSA.generate(1024, os.urandom)
    repr_key = key.export_key('PEM')
    f = open(path, 'wb')
    f.write(repr_key)
    f.close()

    print(f'Приватный ключ сохранен - {path}\n'
          f'{repr_key.decode("utf-8")}')


def send_email(mail, password, path_public_key, path_file, path_elecwriter, recipient):
    send_email_(
        files=(path_public_key, path_file, path_elecwriter),
        recipients=recipient,
        user=mail,
        password=password)


def fetch_email(mail, password, path):
    walker = FetchEmail(username=mail, password=password)
    msgs = walker.fetch_unread_messages()[0]
    walker.save_attachment(msgs, path)

def verify(path_public_key, path_file, path_elecwriter):
    try:
        f_key = open(path_public_key, 'r')
        pubkey = RSA.import_key(f_key.read())
    except Exception as e:
        raise ValueError(e)

    try:
        f_elecwriter = open(path_elecwriter, 'rb')
        elecwriter = f_elecwriter.read()
    except FileNotFoundError:
        raise FileNotFoundError('elecwriter not found')

    h = get_hash(path_file)
    try:
        pkcs1_15.new(pubkey).verify(h, elecwriter)
    except ValueError:
        print(f'Недействительная подпись {path_file} ')
    else:
        print(f'Подпись действительна {path_file}')

def cli():
    print(f'Выберите команду:\n'
          f'1 - Создать приватный ключ\n'
          f'2 - Создать публичный ключ\n'
          f'3 - Подписать\n'
          f'4 - Отправить письмо\n'
          f'5 - Получить письмо\n'
          f'6 - Проверить подпись\n'
          f'0 - Выйти\n')
    key = int(input())
    if key == 1:
        print('Введите путь куда хотите сохранить приватный ключ')
        path = input()
        private_key(path)
        cli()
    elif key == 2:
        print('Введите путь до приватного ключа')
        path_privat = input()
        print('Введите путь куда хотите сохранить публичный ключ')
        path_public = input()
        public_key(path_privat, path_public)
        cli()
    elif key == 3:
        print('Введите путь до приватного ключа')
        path_privat = input()
        print('Введите путь до файла письма')
        path_file = input()
        print('Введите путь по которому хотите сохранить подпись')
        path_sign = input()
        sign(path_privat, path_file, path_sign)
        cli()
    elif key == 4:
        print('Введите адрес электронной почты с которого хотите отправить письмо')
        mail = input()
        print('Пароль')
        passord = input()
        print('Введите путь до публичного ключа')
        path_private = input()
        print('Введите путь до файла письма')
        path_file = input()
        print('Введите путь до электронной подписи')
        path_sign = input()
        print('Введите почту куда отправить')
        mail_ = input()
        send_email(mail, passord, path_private, path_file, path_sign, mail_)
        cli()
    elif key == 5:
        print('Введите адрес электронной почты')
        mail = input()
        print('Пароль')
        passord = input()
        print('Введите куда сохранить файлы полученные по почте')
        path = input()
        fetch_email(mail, passord, path)
        cli()
    elif key == 6:
        print('Введите путь до полученного публичного ключа')
        path_privat = input()
        print('Введите путь до полученного файла письма')
        path_file = input()
        print('Введите путь по полученной электронной подписи')
        path_sign = input()
        verify(path_privat, path_file, path_sign)
        cli()
    elif key == 0:
        return None
