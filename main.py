from sqlalchemy import create_engine, select
from models import Veiculo, Cliente, Ordem, db_session, Atividade
from flask import Flask, request, redirect, url_for, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='AutoTech Serviços',
                         version='1.0.0', )
spec.register(app)


@app.route('/atividades', methods=['GET'])
def atividades():
    sql_atividades = select(Atividade, Cliente, Ordem, Veiculo).join(Cliente, Atividade.cliente_id == Cliente.id)
    resultado_atividades = db_session.execute(sql_atividades).fetchall()
    print(resultado_atividades)
    return jsonify(resultado_atividades)


@app.route('/clientes', methods=['GET'])
def clientes():
    sql_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_clientes).scalars()
    lista_clientes = []
    for cliente in resultado_clientes:
        lista_clientes.append(cliente.serialize_user())
        print(lista_clientes[-1])
    return jsonify(lista_de_clientes=lista_clientes)


@app.route('/clientes', methods=['POST'])
def cadastro_cliente():
    return "eerre"


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
    return "eerre"


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
    return "eerre"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
