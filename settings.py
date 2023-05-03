"""
Passar tudo para classe para deixar mais fácil de modificar.
    * 1 - Classe Geradora:
        Nela terá as funções para gerar coisas aleatórias

"""

from random import choice
from speaks import *
from main import cursor


def get_random_dsquote():
    ds_quote = choice(ds_quotes)
    return ds_quote


def get_random_deletedquote():
    deleted_quote = choice(deleted_msg_quote)
    return deleted_quote


def get_random_name():
    nome = choice(list(cursor.execute("""SELECT texto FROM DarkSouls WHERE Tema = 'Nome'""")))[0]
    sobrenome = choice(list(cursor.execute("""SELECT Texto FROM DarkSouls WHERE Tema = 'Titulos' """)))[0]
    return f'{nome} {sobrenome}'


def get_random_trace():
    traco = choice(list(cursor.execute("""SELECT texto FROM DarkSouls WHERE Tema = 'Traços'""")))[0]
    return traco


def get_random_cargo():
    cargo = choice(list(cursor.execute("""SELECT texto FROM DarkSouls WHERE Tema = 'Cargo'""")))[0]
    return cargo


def get_random_covenant():
    guilda = choice(list(cursor.execute("""SELECT texto FROM DarkSouls WHERE Tema = 'Guilda'""")))[0]
    return guilda


def get_random_memory():
    memory_frag = choice(ds_memory_frag)
    return memory_frag


def get_random_npc():
    nome = get_random_name()
    personalidade = get_random_trace()
    guilda = get_random_covenant()
    cargo = get_random_cargo()

    return f'Nome: {nome}\nGuilda: {guilda}\nFunção: {cargo}\nPersonalidade: {personalidade}'


def clear_chat(message):
    message.delete()


def get_random_enemy():
    enemy = choice(ds_enemys)
    text = f'{enemy} apareceu'
    return text
