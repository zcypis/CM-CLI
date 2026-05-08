from validators import validar_email, validar_nome, validar_telefone, validar_opcoes
from typing import Any
from rich import print
from rich.prompt import Prompt


def ler_nome(prompt: str) -> str:
    if not isinstance(prompt, str):
        raise TypeError("O prompt deve ser informado obrigatoriamente em strings.")

    if not prompt.strip():
        raise ValueError("Nenhum prompt foi informado, string vazia.")

    while True:
        nome = Prompt.ask(prompt).strip()

        try:
            validar = validar_nome(nome)

        except (ValueError, TypeError) as error:
            print(error)
            continue

        return validar


def ler_telefone(prompt: str) -> str:
    if not isinstance(prompt, str):
        raise TypeError("O texto do prompt deve ser strings para prosseguir")

    if not prompt.strip():
        raise ValueError("Nada foi informado no arg prompt")

    while True:
        telefone = Prompt.ask(prompt).strip()

        try:
            validar = validar_telefone(telefone)

        except (ValueError, TypeError) as error:
            print(error)
            continue

        return validar


def ler_email(prompt: str) -> str:
    if not isinstance(prompt, str):
        raise TypeError("Tipo informado invalido, informe string")

    if not prompt.strip():
        raise ValueError("string vazia, impossivel prosseguir.")

    while True:
        email = Prompt.ask(prompt).strip()

        try:
            validar = validar_email(email)

        except (ValueError, TypeError) as error:
            print(error)
            continue

        return validar


def escolher_dados(prompt: str, opcoes: list) -> Any:
    if not isinstance(prompt, str):
        raise TypeError("O prompt deve ser obrigatoriamente informado em string.")

    if not prompt.strip():
        raise ValueError("Prompt invalido, string vazia.")

    while True:
        _entrada = Prompt.ask(prompt).strip()

        try:
            validar = validar_opcoes(_entrada, opcoes)

        except (ValueError, TypeError) as error:
            print(error)
            continue

        return validar
