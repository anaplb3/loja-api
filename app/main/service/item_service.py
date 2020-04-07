from ..bd import repository
from ..model.models import Item

class ItemService:
    def __init__(self):
        self.connection = repository.create_connection()
        self.cursor = self.connection.cursor()

    def get_items(self):
        query = "SELECT * FROM items"
        self.cursor.execute(query)
        items = list(self.cursor.fetchall())
        return self.serialize_items(items)

    def get_item(self, id):
        query_get_item = "SELECT id, name, price, item_type, is_available FROM items WHERE id = {}".format(id)
        self.cursor.execute(query_get_item)
        item = list(self.cursor.fetchone())
    
        return Item(item[0], item[1], item[2], item[3], item[4]).serialize()

    def insert_item(self, name, price, item_type, is_available):
        query_insert_item = """INSERT INTO items (name, price, item_type, is_available)
        VALUES('{}', {}, '{}', {})
        """.format(name, price, item_type, is_available)
        self.cursor.execute(query_insert_item)
        self.connection.commit()

    def update_is_available(self, value, id):
        query = "UPDATE items SET is_available = {} WHERE id = {}".format(value, id)
        self.cursor.execute(query)
        self.connection.commit()

    def update_item(self, id, name, price, item_type, is_available):
        query_update = "UPDATE items SET name = '{}', price = {}, item_type = '{}', is_available = {} WHERE id = {}".format(name, price, item_type, is_available, id)
        self.cursor.execute(query_update)

        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False

    def delete_item(self, id):
        query_delete = "DELETE FROM items WHERE id = {}".format(id)
        self.cursor.execute(query_delete)
        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False

    def serialize_items(self, items):
        results = []
        another = []
        for i in range(len(items)):
            results.append(Item(items[i][0], items[i][1], items[i][2], items[i][3], items[i][4]))
        
        for i in range(len(results)):
            another.append(results[i].serialize())
        
        return another