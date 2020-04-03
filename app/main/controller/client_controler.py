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
            item = client_service.get_item(id)
            return jsonify({"data": item.serialize()})
        except:
            return jsonify({'data': 'Cliente não disponível'})

    def delete(self, id):
        client_service.delete_item(id)
        return jsonify({'data': 'Item deletado'})


@api.route("")
class ClientList(Resource):
    @api.doc(body=clients_fields)
    def post(self):
        try:
            json = request.get_json(force=True)
            name = json['name']
            cpf = json['cpf']
            client_service.insert_item(str(name), str(cpf))

            return jsonify({'data': 'Cliente inserido com sucesso'})
        except Exception as e:
            print(str(e))
            return jsonify({'data': 'Cliente não pôde ser inserido, {}'.format(str(e))})