from ..service.operation_service import OperationService
from flask_restx import Resource, Namespace, fields
from flask import jsonify, request

operation_service = OperationService()

api = Namespace('Operação', 'CRUD das operações da loja')

operations_fields = api.model('Operação', {
    'id_item': fields.Integer(description='ID do item'),
    'id_client': fields.Integer(description='ID do cliente que efetuou a operação'),
    'operation_type': fields.String(description='Operação que foi efetuada(aluguel, reserva, cancelamento ou devolução)'),
    'operation_date': fields.String(description='Data em que a operação ocorreu, no formato AAAA-MM-DD')
})

@api.route("/<int:id>")
class Operation(Resource):
    def get(self, id):
        try:
            operation = operation_service.get_operation(id)
            return jsonify({"data": operation})
        except Exception as e:
            return jsonify({'data': 'Operação não disponível, {}'.format(str(e))})

    @api.doc(body=operations_fields)
    def put(self, id):
        json = request.get_json(force=True)
        try:
            id_item = json['id_item']
            id_client = json['id_client']
            operation_type = json['operation_type']
            operation_date = json['operation_date']

            status = operation_service.update_operation(id, id_item, id_client, operation_type, operation_date)
            if status:
                return jsonify({'data': 'Operação atualizado'})
            else:
                return jsonify({'data': 'Operação não pôde ser atualizado'})
        except:
            return jsonify({'data': 'Operação não pôde ser atualizado, campo necessário não foi enviado.'})
        
        

    def delete(self, id):
        status = operation_service.delete_operation(id)
        if status:
            return jsonify({'data': 'Item deletado'})
        else:
            return jsonify({'data': 'Item não pôde ser deletado'})

@api.route("")
class OperationList(Resource):
    def get(self):
        return jsonify({'data': operation_service.get_operations()})


    @api.doc(body=operations_fields)
    def post(self):
        try:
            json = request.get_json(force=True)
            id_item = json['id_item']
            id_client = json['id_client']
            operation_type = json['operation_type']
            operation_date = json['operation_date']
            operation_service.insert_operation(id_item, id_client, operation_type, operation_date)

            return jsonify({'data': 'Operação inserida com sucesso'})
        except Exception as e:
            return jsonify({'data': 'Operação não pôde ser inserida, {}'.format(str(e))})