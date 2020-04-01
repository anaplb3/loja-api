from ..service.item_service import ItemService
from flask_restx import Resource, Namespace, fields, reqparse
from flask import jsonify, request

item_service = ItemService()

api = Namespace('Item', 'Operações relacionadas aos items da loja')

@api.route("/<int:id>")
class Item(Resource):
    def get(self, id):
        try:
            item = item_service.get_item(id)
            return jsonify({"data": item.serialize()})
        except:
            return jsonify({'data': 'Item não disponível'})
    
    
@api.route("")
class ItemList(Resource):
    @api.doc(fields={'name': fields.String, 'price': fields.Float, 'item_type': fields.String, 'is_available': fields.Boolean})
    def post(self):
        try:
            json = request.get_json(force=True)
            name = json['name']
            price = json['price']
            item_type = json['item_type']
            is_available = json['is_available']
            item_service.insert_item(name, price, item_type, is_available)

            return jsonify({'data': 'Item inserido com sucesso'})
        except:
            return jsonify({'data': 'Item não pôde ser inserido'})