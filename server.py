from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

#Construtor Flask
app = Flask(__name__)
api = Api(app) 

#lista de usuários e linguagens
devs = [
    {
        'id': 1,
        'name': 'Hudson',
        'lang': 'Python'
    },
    {
        'id': 2,
        'name': 'Lucas',
        'lang': 'Java'
    },
    {
        'id': 3,
        'name': 'Gabriel',
        'lang': 'Kotlin'
    }
]

#Definindo o recurso Devs, Declarados métodos Get para tal recurso (Retorna todos os dados de lista devs).
@app.route('/devs', methods=['GET'])
def devs_listAll():
    return jsonify(devs), 200

#Definindo o recurso Devs, Declarados métodos Get para tal recurso (Retorna dados filtrados por 'lang').
@app.route('/devs/<string:lang>', methods=['GET'])
def devs_listByLang(lang):
    devs_per = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per), 200

#Definindo o recurso Devs, Declarados métodos Get para tal recurso (Retorna dados filtrados por 'name').
@app.route('/devs/users/<string:name>', methods=['GET'])
def devs_listByName(name):
    devs_per = [dev for dev in devs if dev['name'] == name]
    return jsonify(devs_per), 200

#Definindo o recurso Devs, Declarados métodos Get para tal recurso (Retorna dados filtrados por 'id').
@app.route('/devs/<int:id>', methods=['GET'])
def devs_listById(id):
    for dev in devs:
        if dev['id'] == id: 
            return jsonify(dev), 200
    return jsonify({'error': 'Not Found'}), 404

#Definindo o recurso Devs, Declaramos métodos Post para tal recurso (Adicionar novo Dev).
@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201

#Definindo o recurso Devs, Declaramos métodos Put para tal recurso (Alterar Dev existente).
@app.route('/devs/<int:id>', methods=['PUT'])
def change_dev(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            return jsonify(dev), 200
    return jsonify({'error: not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)