import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


# Classe do Usuário
class User():
    def __init__(self, nome, profissao, salario):
        self.nome = nome
        self.profissao = profissao
        self.salario = int(salario)


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Trabalho"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

    # Salva as informações
    def salvar_tudo(e):
        # Caso eles não possuam valores
        if input_profissao.value == "" or input_salario.value == "" or input_nome.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = User(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value,
            )
            # Adiciona o Valor de input_nome, input_profissão e input_salário na Lista
            lista.append(obj_user)
            input_nome.value = ""
            input_profissao.value = ""
            input_salario.value = ""
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento

    # Exibe a Lista
    def exibir_lista(e):
        lv_nome.controls.clear()
        for use in lista:
            lv_nome.controls.append(
                ft.Text(value=f'Nome: {use.nome} - Profissão: {use.profissao} - Salário: {use.salario}')
            )
        page.update()

    # FIM da exibição da lista

    # Gerencia o caminho das Rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(  # Primeira Página
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_profissao,
                    input_salario,
                    # Irá salvar os Dados
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_tudo(e),
                    ),
                    # Irá mostrar os Dados
                    ft.Button(
                        text="Exibir lista",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        # Segunda Página
        if page.route == "/segunda" or page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                        ft.Button(
                            text="ir",
                            on_click=lambda _: page.go("/terceira"),
                        )
                    ],
                )
            )
        if page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,
                    ],
                )
            )
        page.update()

    # FIM da Transição de Páginas

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # FIM da seta de Voltar

    # Componentes
    msg_sucesso = ft.SnackBar(
        content=ft.Text("SALVOU"),
        bgcolor=Colors.GREEN
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("ERRO"),
        bgcolor=Colors.RED
    )
    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

    lv_nome = ft.ListView(
        height=500
    )
    # FIM dos Componentes

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)
    # FIM dos Eventos


# Comando que executa o Aplicativo
# Deve estar sempre colado na linha
ft.app(main)
