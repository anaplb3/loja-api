from ..bd import repository
from ..model.models import Item

class ItemService:
    def __init__(self):
        self.connection = repository.create_connection()
        self.cursor = self.connection.cursor()

    def get_item(self, id):
        query_get_item = "SELECT id, name, price, item_type, is_available FROM items WHERE id = {}".format(id)
        self.cursor.execute(query_get_item)
        item = list(self.cursor.fetchone())
    
        return Item(item[1], item[2], item[3], item[4])

    def insert_item(self, name, price, item_type, is_available):
        print(name)
        query_insert_item = """INSERT INTO items (name, price, item_type, is_available)
        VALUES('{}', {}, '{}', {})
        """.format(name, price, item_type, is_available)
        print(query_insert_item)
        self.cursor.execute(query_insert_item)
        self.connection.commit()

    def update_item(self, id, json):
        query_update = "UPDATE items "
        try:
            name = json['name']
            query_update + "SET name = '{}' ".format(name)
        except:
            pass

        try:
            price = json['price']
            query_update + "SET price = {} ".format(price)
        except:
            pass

        try:
            item_type = json['item_type']
            query_update + "SET item_type = '{}' ".format(item_type)
        except:
            pass

        try:
            is_available = json['is_available']
            query_update + "SET is_available = '{}' ".format(is_available)
        except:
            pass

    def delete_item(self, id):
        query_delete = "DELETE FROM items WHERE id = {}".format(id)
        self.cursor.execute(query_delete)
        self.connection.commit()