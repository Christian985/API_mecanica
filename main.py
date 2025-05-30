import requests
from sqlalchemy import create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from models import Veiculo, Cliente, Ordem, Local_session
from flask import Flask, request, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route('/clientes', methods=['GET'])
def clientes():
    db_session = Local_session()
    sql_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_clientes).scalars()
    lista_clientes = []
    for cliente in resultado_clientes:
        lista_clientes.append(cliente.serialize_user())
        print(lista_clientes[-1])
    # Fecha a sessão e abre outra, por segurança
    db_session.close()
    return jsonify(lista_de_clientes=lista_clientes)


@app.route('/clientes', methods=['POST'])
def cadastro_cliente():
    dados = request.get_json()
    nome = dados['nome']
    cpf = dados['cpf']
    telefone = dados['telefone']
    email = dados['email']
    senha = dados['senha']

    if not nome or not senha:
        return jsonify({"msg": "Nome de usuário e senha são obrigatórios"}), 400

    db_session = Local_session()
    try:
        # Verificar se o usuário já existe
        user_check = select(Cliente).where(Cliente.email == email)
        usuario_existente = db_session.execute(user_check).scalar()

        if usuario_existente:
            return jsonify({"msg": "Usuário já existe"}), 400

        novo_usuario = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
        novo_usuario.save(db_session)

        user_id = novo_usuario.id
        return jsonify({"msg": "Usuário criado com sucesso", "user_id": user_id}), 201
    except SQLAlchemyError as e:
        return jsonify({"msg": f"Erro ao registrar usuário: {str(e)}"}), 500
    # Fecha a sessão e abre outra, por segurança
    finally:
        db_session.close()


@app.route('/veiculos', methods=['GET'])
def veiculos():
    db_session = Local_session()
    sql_veiculos = select(Veiculo)
    resultado_veiculos = db_session.execute(sql_veiculos).scalars()
    lista_veiculos = []
    for veiculo in resultado_veiculos:
        lista_veiculos.append(veiculo.serialize_user())
        print(lista_veiculos[-1])
    # Fecha a sessão e abre outra, por segurança
    db_session.close()
    return jsonify(lista_de_veiculos=lista_veiculos)


@app.route('/veiculos', methods=['POST'])
def cadastro_veiculo():
    dados = request.get_json()
    cliente_associado = dados['cliente_associado']
    modelo = dados['modelo']
    placa = dados['placa']
    ano_fabricacao = dados['ano_fabricacao']
    marca = dados['marca']

    db_session = Local_session()
    try:
        # Verificar se Já existe
        veiculo_check = select(Veiculo).where(Veiculo.modelo == modelo)
        veiculo_existente = db_session.execute(veiculo_check).scalar()

        if veiculo_existente:
            return jsonify({"msg": "Veículo já existente"}), 400

        novo_veiculo = Veiculo(cliente_associado=cliente_associado, modelo=modelo, placa=placa,
                               ano_fabricacao=ano_fabricacao, marca=marca)
        novo_veiculo.save(db_session)

        veiculo_id = novo_veiculo.id
        return jsonify({"Msg": "Veículo criado com sucesso", "veiculo_id": veiculo_id}), 201
    except SQLAlchemyError as e:
        return jsonify({"msg": f"Erro ao registrar veiculo: {str(e)}"}), 500
    # Fecha a sessão e abre outra, por segurança
    finally:
        db_session.close()


@app.route('/ordem', methods=['GET'])
def ordens_servicos():
    db_session = Local_session()
    sql_ordens = select(Ordem)
    resultado_ordens = db_session.execute(sql_ordens).scalars()
    lista_ordens = []
    for ordem in resultado_ordens:
        lista_ordens.append(ordem.serialize_user())
        print(lista_ordens[-1])
    # Fecha a sessão e abre outra, por segurança
    db_session.close()
    return jsonify(lista_de_ordens=lista_ordens)


@app.route('/ordem', methods=['POST'])
def cadastro_ordens_servicos():
    dados = request.get_json()
    veiculo_associado = dados['veiculo_associado']
    data_abertura = dados['data_abertura']
    descricao_servico = dados['descricao_servico']
    status = dados['status']
    valor_estimado = dados['valor_estimado']

    db_session = Local_session()
    try:
        # Verificar se já existe
        ordem_check = select(Ordem).where(Ordem.status == status)
        ordem_existente = db_session.execute(ordem_check).scalar()

        if ordem_existente:
            return jsonify({"Msg": f"Ordem já existente"}), 400

        nova_ordem = Ordem(veiculo_associado=veiculo_associado, data_abertura=data_abertura, descricao_servico=descricao_servico, status=status,
                           valor_estimado=valor_estimado)
        nova_ordem.save(db_session)

        ordem_id = nova_ordem.id
        return jsonify({"msg": "Ordem criado com sucesso", "ordem_id": ordem_id}), 201
    except SQLAlchemyError as e:
        return jsonify({"Msg": f"Erro ao registrar ordem: {str(e)}"}), 500
    # Fecha a sessão e abre outra, por segurança
    finally:
        db_session.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
