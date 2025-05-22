from models import Cliente, Veiculo, db_session, Ordem
from sqlalchemy import select


# Inserir dados do Cliente na tabela
def inserir_cliente():
    cliente = Cliente(nome=str(input('Nome: ')),
                      cpf=int(input('CPF: ')),
                      telefone=int(input('Telefone: ')),
                      endereco=str(input('Endereço: ')),
                      )
    print(cliente)
    cliente.save()


# Consultar o Cliente
def consultar_cliente():
    var_cliente = select(Cliente)
    var_cliente = db_session.execute(var_cliente).scalars()
    for cliente in var_cliente:
        print(cliente.nome, cliente.cpf, cliente.telefone, cliente.endereco)


# Atualiza o Cliente
def atualizar_cliente():
    # Seleciona o item a ser alterado
    # Altera o nome do cliente
    var_cliente = select(Cliente).where(str(input('Nome: ')) == Cliente.nome)
    var_cliente = db_session.execute(var_cliente).scalar()

    # Altera o cpf do cliente
    var_cliente = select(Cliente).where(int(input('Cpf: ')) == Cliente.cpf)
    var_cliente = db_session.execute(var_cliente).scalar()

    # Altera o telefone do cliente
    var_cliente = select(Cliente).where(int(input('Telefone: ')) == Cliente.telefone)
    var_cliente = db_session.execute(var_cliente).scalar()

    # Altera o endereço do cliente
    var_cliente = select(Cliente).where(str(input('Endereço: ')) == Cliente.endereco)
    var_cliente = db_session.execute(var_cliente).scalar()

    # Nova informação de cliente
    var_cliente.nome = str(input('Novo Nome: '))
    var_cliente.cpf = str(input('Novo CPF: '))
    var_cliente.telefone = int(input('Novo Telefone: '))
    var_cliente.endereco = str(input('Novo Endereço: '))
    var_cliente.save()


# Deleta o Cliente
def deletar_cliente():
    # Sessões para deletar
    cliente_deletar = input('Quem você deseja deletar? :')
    cliente_deletar_cpf = int(input('Deletar o CPF: '))
    cliente_deletar_tel = int(input('Deletar o Telefone: '))
    cliente_deletar_end = input('Deletar o Endereço: ')

    # Irá pegar os dados
    var_cliente = select(Cliente).where(cliente_deletar == Cliente.nome)
    var_cliente = select(Cliente).where(cliente_deletar_cpf == Cliente.cpf)
    var_cliente = select(Cliente).where(cliente_deletar_tel == Cliente.telefone)
    var_cliente = select(Cliente).where(cliente_deletar_end == Cliente.endereco)
    var_cliente = db_session.execute(var_cliente).scalar()
    var_cliente.delete()


# FIM DO CLIENTE


# Insere o Veículo na tabela
def inserir_veiculo():
    veiculo = Veiculo(cliente_associado=str(input('Cliente Associado: ')),
                      modelo=str(input('Modelo: ')),
                      placa=str(input('Placa: ')),
                      ano_fabricacao=int(input('Ano de Fabricação: ')),
                      marca=str(input('Marca: ')), )
    print(veiculo)
    veiculo.save()


# Consulta o Veículo na tabela
def consultar_veiculo():
    var_veiculo = select(Veiculo)
    var_veiculo = db_session.execute(var_veiculo).scalars()
    for veiculo in var_veiculo:
        print(veiculo.cliente_associado, veiculo.modelo, veiculo.placa, veiculo.ano_fabricacao, veiculo.marca)


# Atualiza o Veículo na tabela
def atualizar_veiculo():
    # Seleciona o cliente do veículo a ser alterado
    var_veiculo = select(Veiculo).where(str(input('Cliente associado: ')) == Veiculo.cliente_associado)
    var_veiculo = db_session.execute(var_veiculo).scalar()

    # Seleciona o modelo do veículo
    var_veiculo = select(Veiculo).where(str(input('Modelo do veiculo: ')) == Veiculo.modelo)
    var_veiculo = db_session.execute(var_veiculo).scalar()

    # Seleciona a placa do veículo
    var_veiculo = select(Veiculo).where(str(input('Placa do veiculo: ')) == Veiculo.placa)
    var_veiculo = db_session.execute(var_veiculo).scalar()

    # Seleciona o ano de fabricação do veículo
    var_veiculo = select(Veiculo).where(str(input('Ano de fabricação: ')) == Veiculo.ano_fabricacao)
    var_veiculo = db_session.execute(var_veiculo).scalar()

    # Seleciona a marca do veículo
    var_veiculo = select(Veiculo).where(str(input('Marca: ')) == Veiculo.marca)
    var_veiculo = db_session.execute(var_veiculo).scalar()

    # Nova informação de modelo do veículo
    var_veiculo.cliente_associado = str(input('Novo Nome: '))
    var_veiculo.modelo = str(input('Novo Modelo: '))
    var_veiculo.placa = str(input('Nova Placa: '))
    var_veiculo.ano_fabricacao = str(input('Novo Ano de Fabricação: '))
    var_veiculo.marca = str(input('Nova Marca: '))
    var_veiculo.save()


# Deleta o Veículo na tabela
def deletar_veiculo():
    # Sessões para deletar
    veiculo_deletar = input('Quem você deseja deletar? :')
    veiculo_deletar_mod = input('Deletar o Modelo do Veículo: ')
    veiculo_deletar_placa = input('Deletar a Placa do Veículo: ')
    veiculo_deletar_ano = input('Deletar o Ano do Veículo: ')
    veiculo_deletar_marca = input('Deletar a Marca: ')

    # Irá pegar os dados
    var_veiculo = select(Veiculo).where(veiculo_deletar == Veiculo.cliente_associado)
    var_veiculo = select(Veiculo).where(veiculo_deletar_mod == Veiculo.modelo)
    var_veiculo = select(Veiculo).where(veiculo_deletar_placa == Veiculo.placa)
    var_veiculo = select(Veiculo).where(veiculo_deletar_ano == Veiculo.ano_fabricacao)
    var_veiculo = select(Veiculo).where(veiculo_deletar_marca == Veiculo.marca)
    var_veiculo = db_session.execute(var_veiculo).scalar()
    var_veiculo.delete()


# FIM DO VEÍCULO

# Insere Ordem na tabela
def inserir_ordem():
    ordem_servicos = Ordem(veiculo_associado=str(input('Veículo associado: ')),
                           data_abertura=str(input('Data abertura: ')),
                           descricao_servico=str(input('Descricao servico: ')),
                           status=str(input('Status: ')),
                           valor_estimado=int(input('Valor estimado: ')),
                           )
    print(ordem_servicos)
    ordem_servicos.save()


# Consulta Ordem na tabela
def consultar_ordem():
    var_ordem = select(Ordem)
    var_ordem = db_session.execute(var_ordem).scalars()
    for ordem in var_ordem:
        print(ordem.veiculo_associado, ordem.data_abertura, ordem.descricao_servico, ordem.status, ordem.valor_estimado)


# Atualiza Ordem na tabela
def atualizar_ordem():
    # Seleciona o veículo associado a ser alterado
    var_ordem = select(Ordem).where(str(input('Veículo associado: ')) == Ordem.veiculo_associado)
    var_ordem = db_session.execute(var_ordem).scalar()

    # Seleciona a data de abertura a ser alterada
    var_ordem = select(Ordem).where(int(input('Data de abertura: ')) == Ordem.data_abertura)
    var_ordem = db_session.execute(var_ordem).scalar()

    # Seleciona a descrição do serviço a ser alterada
    var_ordem = select(Ordem).where(str(input('Descrição do serviço: ')) == Ordem.descricao_servico)
    var_ordem = db_session.execute(var_ordem).scalar()

    # Seleciona o status a ser alterado
    var_ordem = select(Ordem).where(str(input('Status: ')) == Ordem.status)
    var_ordem = db_session.execute(var_ordem).scalar()

    # Seleciona o valor estimado a ser alterado
    var_ordem = select(Ordem).where(int(input('Valor estimado: ')) == Ordem.valor_estimado)
    var_ordem = db_session.execute(var_ordem).scalar()

    # Nova informação
    var_ordem.veiculo_associado = str(input('Novo Veículo associado: '))
    var_ordem.data_abertura = int(input('Nova Data abertura: '))
    var_ordem.descricao_servico = str(input('Nova Descrição serviço: '))
    var_ordem.status = str(input('Novo Status: '))
    var_ordem.valor_estimado = int(input('Novo Valor estimado: '))
    var_ordem.save()


# Deleta Ordem na tabela
def deletar_ordem():
    # Sessões para deletar
    ordem_deletar = input('Quem você deseja deletar? : ')
    ordem_deletar_data = int(input('Deletar Data de Abertura: '))
    ordem_deletar_desc = input('Deletar Descrição do Serviço: ')
    ordem_deletar_status = input('Deletar Status: ')
    ordem_deletar_valor = int(input('Deletar Valor Estimado: '))

    # Irá pegar os dados
    var_ordem = select(Ordem).where(ordem_deletar == Ordem.veiculo_associado)
    var_ordem = select(Ordem).where(ordem_deletar_data == Ordem.data_abertura)
    var_ordem = select(Ordem).where(ordem_deletar_desc == Ordem.descricao_servico)
    var_ordem = select(Ordem).where(ordem_deletar_status == Ordem.status)
    var_ordem = select(Ordem).where(ordem_deletar_valor == Ordem.valor_estimado)
    var_ordem = db_session.execute(var_ordem).scalar()
    var_ordem.delete()


# FIM DA ORDEM E SERVIÇOS


if __name__ == '__main__':

    while True:
        print()
        print('Menu')
        print('1 - Cliente')
        print('2 - Veículo')
        print('3 - Ordens e servicos')
        print('4 - Sair')

        escolha_menu = int(input('Escolha uma opção: '))

        if escolha_menu == 1:
            print('1 - Inserir Cliente')
            print('2 - Consultar Cliente')
            print('3 - Atualizar Cliente')
            print('4 - Deletar Cliente')
            print('5 - Sair')
            escolha = input('Escolha: ')
            if escolha == '1':
                inserir_cliente()
            elif escolha == '2':
                consultar_cliente()
            elif escolha == '3':
                atualizar_cliente()
            elif escolha == '4':
                deletar_cliente()
            elif escolha == '5':
                break

        elif escolha_menu == 2:
            print('1 - Inserir Veiculo')
            print('2 - Consultar Veiculo')
            print('3 - Atualizar Veiculo')
            print('4 - Deletar Veiculo')
            print('5 - Sair')
            escolha = input('Escolha: ')
            if escolha == '1':
                inserir_veiculo()
            elif escolha == '2':
                consultar_veiculo()
            elif escolha == '3':
                atualizar_veiculo()
            elif escolha == '4':
                deletar_veiculo()
            elif escolha == '5':
                break

        elif escolha_menu == 3:
            print('1 - Inserir Ordem')
            print('2 - Consultar Ordem')
            print('3 - Atualizar Ordem')
            print('4 - Deletar Ordem')
            print('5 - Sair')
            escolha = input('Escolha: ')
            if escolha == '1':
                inserir_ordem()
            elif escolha == '2':
                consultar_ordem()
            elif escolha == '3':
                atualizar_ordem()
            elif escolha == '4':
                deletar_ordem()
            elif escolha == '5':
                break

        elif escolha_menu == 4:
            break
