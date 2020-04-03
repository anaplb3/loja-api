from ..service.item_service import ItemService
from flask_restx import Resource, Namespace, fields
from flask import jsonify, request

item_service = ItemService()

api = Namespace('Item', 'Operações relacionadas aos items da loja')

items_fields = api.model('Item', {
    'name': fields.String,
    'price': fields.Float,
    'item_type': fields.String,
    'is_available': fields.Boolean
})

@api.route("/<int:id>")
class Item(Resource):
    def get(self, id):
        try:
            item = item_service.get_item(id)
            return jsonify({"data": item.serialize()})
        except:
            return jsonify({'data': 'Item não disponível'})

    @api.doc(body=items_fields)
    def put(self, id):
        json = request.get_json(force=True)
        try:
            name = json['name']
            price = json['price']
            item_type = json['item_type']
            is_available = json['is_available']

            status = item_service.update_item(id, name, price, item_type, is_available)
            if status:
                return jsonify({'data': 'Item atualizado'})
            else:
                return jsonify({'data': 'Item não pôde ser atualizado'})
        except:
            return jsonify({'data': 'Item não pôde ser atualizado, campo necessário não foi enviado.'})
        
        

    def delete(self, id):
        status = item_service.delete_item(id)
        if status:
            return jsonify({'data': 'Item deletado'})
        else:
            return jsonify({'data': 'Item não pôde ser deletado'})
        
    
    
@api.route("")
class ItemList(Resource):
    @api.doc(body=items_fields)
    def post(self):
        try:
            json = request.get_json(force=True)
            name = json['name']
            price = json['price']
            item_type = json['item_type']
            is_available = json['is_available']
            item_service.insert_item(str(name), price, str(item_type), is_available)

            return jsonify({'data': 'Item inserido com sucesso'})
        except Exception as e:
            print(str(e))
            return jsonify({'data': 'Item não pôde ser inserido'})