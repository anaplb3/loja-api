class Item:
    def __init__(self, name, price, item_type, is_available):
        self.name = name
        self.price = price
        self.item_type = item_type
        self.is_available = is_available

    def serialize(self):
        return {
            'name': self.name,
            'price': self.price,
            'item_type': self.item_type,
            'is_available': self.is_available
        }

class Client:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def serialize(self):
        return {
            'name': self.name,
            'cpf': self.cpf
        }
