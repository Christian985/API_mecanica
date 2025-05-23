import requests
from sqlalchemy import create_engine, select
from models import Veiculo, Cliente, Ordem, db_session
from flask import Flask, request, redirect, url_for, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='AutoTech Serviços',
                         version='1.0.0', )
spec.register(app)


@app.route('/clientes', methods=['GET'])
def clientes():
    sql_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_clientes).scalars()
    lista_clientes = []
    for cliente in resultado_clientes:
        lista_clientes.append(cliente.serialize_user())
        print(lista_clientes[-1])
    return jsonify(lista_de_clientes=lista_clientes)


@app.route('/cadastro_clientes', methods=['POST'])
def cadastro_cliente():
    dados = request.get_json()
    nome = dados['nome']
    cpf = dados['cpf']
    telefone = dados['telefone']
    email = dados['email']
    senha = dados['senha']

    if not nome or not email or not cpf or not telefone:
        return jsonify({"msg": "Nome de usuário e senha são obrigatórios"}), 400

    db_session = db_session.session()
    try:
        # Verificar se o usuário já existe
        user_check = select(Cliente).where(Cliente.email == email)
        usuario_existente = db_session.execute(user_check).scalar()

        if usuario_existente:
            return jsonify({"msg": "Usuário já existe"}), 400

        novo_usuario = Cliente(nome=nome,cpf=cpf, telefone=telefone, email=email)
        novo_usuario.set_senha_hash(senha)
        db_session.add(novo_usuario)
        db_session.commit()

        user_id = novo_usuario.id
        return jsonify({"msg": "Usuário criado com sucesso", "user_id": user_id}), 201
    except Exception as e:
        db_session.rollback()
        return jsonify({"msg": f"Erro ao registrar usuário: {str(e)}"}), 500
    finally:
        db_session.close()

@app.route('/veiculos', methods=['GET'])
def veiculos():
    sql_veiculos = select(Veiculo)
    resultado_veiculos = db_session.execute(sql_veiculos).scalars()
    lista_veiculos = []
    for veiculo in resultado_veiculos:
        lista_veiculos.append(veiculo.serialize_user())
        print(lista_veiculos[-1])
    return jsonify(lista_de_veiculos=lista_veiculos)


@app.route('/veiculos', methods=['GET'])
def cadastro_veiculo():
    return ""


@app.route('/ordem', methods=['GET'])
def ordens_servicos():
    sql_ordens = select(Ordem)
    resultado_ordens = db_session.execute(sql_ordens).scalars()
    lista_ordens = []
    for ordem in resultado_ordens:
        lista_ordens.append(ordem.serialize_user())
        print(lista_ordens[-1])
    return jsonify(lista_de_ordens=lista_ordens)


@app.route('/ordem', methods=['GET'])
def cadastro_ordens_servicos():
    dados = request.get_json()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
