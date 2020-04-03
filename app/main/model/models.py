class Item:
    def __init__(self, id, name, price, item_type, is_available):
        self.id = id
        self.name = name
        self.price = price
        self.item_type = item_type
        self.is_available = is_available

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'item_type': self.item_type,
            'is_available': self.is_available
        }

class Client:
    def __init__(self, id, name, cpf):
        self.id = id
        self.name = name
        self.cpf = cpf

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf
        }

class Operation:
    def __init__(self, id, id_item, id_client, operation_type, operation_date):
        self.id = id
        self.id_item = id_item
        self.id_client = id_client
        self.operation_type = operation_type
        self.operation_date = operation_date

    def serialize(self):
        return {
            'id': self.id,
            'id_item': self.id_item,
            'id_client': self.id_client,
            'operation_type': self.operation_type,
            'operation_date': self.operation_date
        }
