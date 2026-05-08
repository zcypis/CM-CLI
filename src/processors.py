from helpers import escolher_dados, ler_email, ler_nome, ler_telefone
from rich.table import Table


def adicionar_contato(nome: str, telefone: str, email: str, cadastro: dict) -> None:
    nome_normalizado = nome.strip().lower()

    if nome_normalizado in cadastro:
        raise ValueError("Esse nome ja esta cadastrado nos dados informado.")

    cadastro[nome_normalizado] = {"telefone": telefone, "email": email}


def remover_contato(nome: str, cadastro: dict) -> None:
    nome_normalizado = nome.strip().lower()

    if nome_normalizado not in cadastro:
        raise ValueError("O nome informado não esta nos dados informados.")

    del cadastro[nome_normalizado]


def atualizar_contato(nome: str, cadastro: dict) -> None:
    nome_normalizado = nome.strip().lower()

    if nome_normalizado not in cadastro:
        raise ValueError("O nome informado não foi encontrado nos dados informados.")

    _entrada = escolher_dados(
        "Informe o tipo de dado que deseja atualizar", ["nome", "telefone", "email"]
    )

    if _entrada == "nome":
        _nome = ler_nome("Digite o nome que deseja atualizar: ")
        cadastro[_nome.lower()] = cadastro.pop(nome_normalizado)

    elif _entrada == "telefone":
        _telefone = ler_telefone("Informe seu numero para atualizar os dados: ")
        cadastro[nome_normalizado]["telefone"] = _telefone

    elif _entrada == "email":
        _email = ler_email("Digite seu nome email para alterar os dados: ")
        cadastro[nome_normalizado]["email"] = _email


def listar_contatos(cadastro: dict) -> Table:
    if not cadastro:
        raise ValueError("O banco de dados informado esta vazio.")

    conteudo = Table(title="Contatos Cadastrados")

    conteudo.add_column(
        ":bust_in_silhouette: [yellow1]Nome[/]", style="underline bold blue1"
    )
    conteudo.add_column(
        ":telephone_receiver: [green1]Telefone[/]", style="bold bright_cyan"
    )
    conteudo.add_column(":incoming_envelope: [red1]Email[/]", style="bold white")

    for nome, dados in cadastro.items():
        conteudo.add_row(nome, dados["telefone"], dados["email"])

    return conteudo
