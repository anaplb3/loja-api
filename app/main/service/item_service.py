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
        query_insert_item = """INSERT INTO items (name, price, item_type, is_available)
        VALUES({}, {}, {}, {})
        """.format(name, price, item_type, is_available)
        self.cursor.execute(query_insert_item)
        self.connection.commit()