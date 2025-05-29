import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from models import Veiculo, Cliente, Ordem, Local_session


# Main
def main(page: ft.Page):
    # Configurações
    page.title = "Mecânica"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    # Salva as informações!
    def salvar_veiculo(e):
        # Caso eles não possuam valores
        if input_cliente_associado.value == "" or input_modelo.value == "" or input_placa.value == "" or input_ano_fabricacao.value == "" or input_marca.value == "":
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_erro)
            # Vai abrir a mensagem
            msg_erro.open = True
            page.update()
        else:
            obj_user = Veiculo(
                cliente_associado=input_cliente_associado.value,
                modelo=input_modelo.value,
                placa=input_placa.value,
                ano_fabricacao=input_ano_fabricacao.value,
                marca=input_marca.value,

            )
            # Adiciona o Valor de cliente_associado, modelo, placa, ano_fabricacao e marca na Lista
            input_cliente_associado.value = ""
            input_modelo.value = ""
            input_placa.value = ""
            input_ano_fabricacao.value = ""
            input_marca.value = ""
            db_session.add(obj_user)
            db_session.commit()
            # Overlay vai apagar a mensagem anterior
            page.overlay.append(msg_sucesso)
            # Vai abrir a mensagem
            msg_sucesso.open = True
            page.update()

    # FIM do salvamento

    # FIM da exibição da lista

    # Gerencia o caminho das Rotas
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(  # Primeira Página
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_cliente_associado,
                    input_modelo,
                    input_placa,
                    input_ano_fabricacao,
                    input_marca,
                    # Irá salvar os Dados
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_veiculo(e),
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
        # if page.route == "/terceira":
        #     page.views.append(
        #         View(
        #             "/terceira",
        #             [
        #                 AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
        #                 lv_nome,
        #             ],
        #         )
        #     )
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
    input_cliente_associado = ft.TextField(label="Cliente Associado")
    input_modelo = ft.TextField(label="Modelo")
    input_placa = ft.TextField(label="Placa")
    input_ano_fabricacao = ft.TextField(label="Ano de Fabricacao")
    input_marca = ft.TextField(label="Marca")

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