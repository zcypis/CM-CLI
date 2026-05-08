from data import carregar_dados, salvar_dados
from helpers import ler_email, ler_nome, ler_telefone
from processors import (
    adicionar_contato,
    remover_contato,
    atualizar_contato,
    listar_contatos,
)

from rich.prompt import Confirm, Prompt
from rich.panel import Panel
from rich import print
from time import sleep


def main():
    print(
        Panel(
            "Projeto de gerenciamento de contatos via terminal,\n"
            "Foco do Projeto é testar e consolidar conhecimentos sobre libs e metodos em python.\n\n"
            " [red1]*[/] Author: [orange1]zcypis[/] [blue1]https://github.com/zcypis[/]\n"
            " [red1]*[/] Versão: [cyan]0.1.0-alpha[/]",
            title="[grey53]<[/] :busts_in_silhouette: [bright_magenta]Contacts-CLI[/] [grey53]>[/]",
            border_style="dark_red",
            width=55,
        )
    )
    if not Confirm.ask("Deseja prosseguir para o [yellow]Menu[/]?:"):
        return
    
    dados = carregar_dados()

    while True:
        print(
            "\n" * 30,
            Panel(
                "[yellow1][1][/] - :heavy_plus_sign: Adicionar Contato\n"
                "[yellow1][2][/] - :x: Remover Contato\n"
                "[yellow1][3][/] - :memo: Atualiza Contato\n"
                "[yellow1][4][/] - :bookmark_tabs: Ver Contatos\n"
                "[yellow1][5][/] - :stop_sign: Finalizar",
                title=":busts_in_silhouette: [bright_magenta]Gerenciar Contatos-CLI[/]",
                border_style="dodger_blue2",
                width=50,
            ),
        )
        escolha = Prompt.ask("Escolha uma entre as [yellow]opções[/]")

        if escolha == "1":
            print(
                "\n" * 30,
                Panel(
                    "Preencha os dados abaixos para adicionar um novo contato aos dados",
                    title="[yellow1]Função [1][/] - [white]:heavy_plus_sign: Adicionar Contato[/]",
                    border_style="green1",
                    width=50,
                ),
            )
            while True:
                _nome = ler_nome("Nome do novo contato")

                if _nome.lower() in dados:
                    if not Confirm.ask(
                        "O nome ja esta no banco de dados, deseja cadastrar outro nome?"
                    ):
                        break
                    else:
                        continue

                _telefone = ler_telefone("Informe o telefone")
                _email = ler_email("Email do contato")

                adicionar_contato(_nome, _telefone, _email, dados)
                print(
                    "\n" * 30,
                    Panel(
                        f'Novo contato [yellow1]"{_nome}"[/] cadastrado nos dados.',
                        title="[green]Sucesso ao Cadastrar[/]",
                        border_style="cyan",
                        width=50,
                    ),
                )
                sleep(5)
                break

        elif escolha == "2":
            if not dados:
                print(
                    "\n" * 30,
                    Panel(
                        "Banco de dados esta vazio, impossivel prosseguir.",
                        title="[white]Aviso[/]",
                        border_style="red1",
                        width=50,
                    ),
                )
                sleep(5)
                continue

            print(
                "\n" * 30,
                Panel(
                    "Preencha os campos com as informações necessarias para remover o contato desejado.",
                    title="[yellow1]Função [2][/] - [white]:x: Remover Contato[/]",
                    border_style="green1",
                    width=50,
                ),
            )

            while True:
                remover_nome = ler_nome(
                    "Digite o nome do contato que deseja remover da lista"
                )

                if remover_nome.lower() not in dados:
                    if not Confirm.ask(
                        "Nome inexistente no banco de dados, deseja tentar novamente?"
                    ):
                        break
                    else:
                        continue

                remover_contato(remover_nome, dados)
                print(
                    "\n" * 30,
                    Panel(
                        f'O contato [yellow1]"{remover_nome}"[/] foi removido dos dados',
                        title="[green]Sucesso ao Remover[/]",
                        border_style="cyan",
                        width=50,
                    ),
                )
                sleep(5)
                break

        elif escolha == "3":
            if not dados:
                print(
                    "\n" * 30,
                    Panel(
                        "Dados inexistentes, impossivel atualizar algo",
                        title="[white]Aviso[/]",
                        border_style="red1",
                        width=50,
                    ),
                )
                sleep(5)
                continue

            print(
                "\n" * 30,
                Panel(
                    "Informe um nome de contato ja registrado para prosseguir com a atualização das informações."
                    "\nOpções de edição: [bold bright_cyan]< nome, telefone, email >[/]",
                    title="[yellow1]Função [3][/] - [white]:memo: Atualiza Contato[/]",
                    border_style="green1",
                    width=50,
                ),
            )

            while True:
                atualizar_nome = ler_nome(
                    "Digite o nome do Contato que deseja altualizar"
                )

                if atualizar_nome.lower() not in dados:
                    if not Confirm.ask(
                        "Nome do Contato não presente no banco de dados, deseja buscar por outro nome?"
                    ):
                        break
                    else:
                        continue

                atualizar_contato(atualizar_nome.lower(), dados)
                print(
                    "\n" * 30,
                    Panel(
                        f"Dados do contato [yellow1]{atualizar_nome.title()}[/] atualizados.",
                        title="[green]Sucesso em Atualizar[/]",
                        border_style="cyan",
                        width=50,
                    ),
                )
                sleep(5)
                break

        elif escolha == "4":
            if not dados:
                print(
                    "\n" * 30,
                    Panel(
                        "O banco de dados não possui nenhum dado para informar.",
                        title="[white]Aviso[/]",
                        width=40,
                        border_style="red1",
                    ),
                )
                sleep(5)
                continue

            print(
                "\n" * 30,
                Panel(
                    "Abaixo informações de todos os dados registrado no banco de dados.",
                    title="[yellow1]Função [4][/] - [white]:bookmark_tabs: Ver Contatos[/]",
                    border_style="green1",
                    width=50,
                ),
            )

            print(listar_contatos(dados))
            Prompt.ask("Pressione [yellow1]Enter[/] para voltar ao menu")

        elif escolha == "5":
            print(
                "\n" * 30,
                Panel(
                    "Salvando dados em arquivo: [green1]saved_data.json[/]",
                    title="[bold bright_cyan]Finalizando...[/]",
                    border_style="red1",
                    width=55,
                ),
            )
            salvar_dados(dados)
            sleep(3)
            print(
                "\n" * 30,
                Panel(
                    "Dados salvos, seram mantidos na proxima sessão.",
                    title="[bold bright_cyan]Finalizando...[/]",
                    border_style="red1",
                    width=55,
                ),
            )
            break

        else:
            Prompt.ask(
                "\n[red]Escolha invalida![/] Pressione [yellow]Enter[/] para voltar :end:"
            )


if "__main__" == __name__:
    main()
