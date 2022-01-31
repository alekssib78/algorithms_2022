"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha512
from uuid import uuid4

cache = dict()
salt = uuid4().hex

def url_cache():
    url_adr = input("Введите url: ")
    if url_adr != '0':
        if not cache.get(url_adr):
            cache.setdefault(url_adr, sha512(salt.encode() + url_adr.encode()).hexdigest())
            print(f'Хэш {url_adr} был добавлен')
        else:
            print(f"Страница {url_adr} уже есть.Хэш url {cache[url_adr]}")
        return url_cache()


url_cache()
