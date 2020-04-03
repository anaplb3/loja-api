from ..service.client_service import ClientService
from flask_restx import Resource, Namespace, fields
from flask import jsonify, request

client_service = ClientService()

api = Namespace('Cliente', 'Operações relacionadas aos clientes da loja')

clients_fields = api.model('Cliente', {
    'name': fields.String,
    'cpf': fields.String
})

@api.route("/<int:id>")
class Client(Resource):
    def get(self, id):
        try:
            client = client_service.get_client(id)
            return jsonify({"data": client.serialize()})
        except Exception as e:
            return jsonify({'data': 'Cliente não disponível, {}'.format(str(e))})
    
    @api.doc(body=clients_fields)
    def put(self, id):
        json = request.get_json(force=True)
        
        try:
            name = json['name']
            cpf = json['cpf']
            status = client_service.update_client(id, name, cpf)

            if status:
                return jsonify({'data': 'Cliente atualizado'})
            else:
                return jsonify({'data': 'Cliente não pôde ser atualizado'})
        except:
            return jsonify({'data': 'Cliente não pôde ser atualizado, campo necessário não foi enviado.'})

    def delete(self, id):
        status = client_service.delete_client(id)
        if status:
            return jsonify({'data': 'Cliente deletado'})
        else:
            return jsonify({'data': 'Cliente não pôde ser deletado'})
        


@api.route("")
class ClientList(Resource):
    @api.doc(body=clients_fields)
    def post(self):
        try:
            json = request.get_json(force=True)
            name = json['name']
            cpf = json['cpf']
            client_service.insert_client(str(name), str(cpf))

            return jsonify({'data': 'Cliente inserido com sucesso'})
        except Exception as e:
            print(str(e))
            return jsonify({'data': 'Cliente não pôde ser inserido, {}'.format(str(e))})