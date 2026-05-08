import re
from typing import Any


def validar_nome(nome: str) -> str:
    if not isinstance(nome, str):
        raise TypeError("O nome deve ser informado somente em strings.")

    if not nome.strip():
        raise ValueError("Nenhum nome foi informado, impossivel prosseguir.")

    _nome = nome.strip()

    if not 2 <= len(_nome) <= 25:
        raise ValueError("O nome deve conter entre 2 e 25 caracteres.")

    if not re.search(r"^[\w\sÀ-ÿ-]+$", _nome):
        raise ValueError("O nome não segue o padrão proposto.")

    return _nome


def validar_email(email: str) -> str:
    if not isinstance(email, str):
        raise TypeError("Tipo incorreto, informe o email com somente strings.")

    if not email.strip():
        raise ValueError("Nada foi informada, dados invalidos.")

    _email = email.strip()

    if not re.search(r"^\w+@[a-zA-Z]+\.[a-zA-z]{2,4}$", _email):
        raise ValueError("Email invalido, não segue um padrao correto.")

    return _email


def validar_telefone(numero: str) -> str:
    if not isinstance(numero, str):
        raise TypeError("Informe o numero em strings para valida-lo.")

    if not numero.strip():
        raise ValueError("Nenhum caracter foi informado, invalido!.")

    _numero = numero.strip()

    validar = re.sub(r"[-()\s+]", "", _numero)

    if not validar:
        raise ValueError("Nenhum numero foi informado.")

    if not re.search(r"^\d+$", validar):
        raise TypeError("Um numero de telefone deve conter apenas digitos numericos.")

    if not 10 <= len(validar) <= 11:
        raise ValueError(
            f'Numero invalido, quantidade de digitos: "{len(validar)}" nao corresponde ao padrao 10-11'
        )
    if validar[0] * len(validar) == validar:
        raise ValueError("Todos os numeros são iguais, telefone invalido")

    return _numero


def validar_int(numero: int, min: int = 0, max: int = 50) -> int:
    for num in (numero, min, max):
        if not isinstance(num, int) or isinstance(num, bool):
            raise TypeError(f'O valor deve ser informado em int, recebido: {type(num).__name__}.')
        
    if not min <= numero <= max:
        raise ValueError(f'Informe um valor entre {min} e {max} para prosseguir com a função.')
        
    return numero


def validar_float(numero: float, min: float = 0, max: float = 50) -> float:
    for num in (numero, min, max):
        if not isinstance(num, (float, int)) or isinstance(num, bool):
            raise TypeError(f'Tipo informado não corresponde ao esperado: int | float, informado: {type(num).__name__}')
        
    if not min <= numero <= max:
        raise ValueError(f'Informe um valor entre {min} e {max}, para ser aceito pela função.')
    
    return float(numero)


def validar_opcoes(escolha: Any, opcoes: list[Any]) -> Any:
    if not isinstance(opcoes, list):
        raise TypeError('As opcoes validas informadas estao em formato errado, informe uma lista com valores.')
    
    if not opcoes:
        raise ValueError('A lista esta vazia, impossivel prosseguir com a função.')
    
    _escolha = escolha
    
    if isinstance(escolha, str):
        _escolha = escolha.strip()
    
    if _escolha not in opcoes:
        raise ValueError(f'A escolha não se encontra nas opções validas: {opcoes}.')
    
    return _escolha