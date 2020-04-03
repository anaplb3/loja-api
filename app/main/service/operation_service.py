from ..bd import repository
from ..model.models import Operation
from ..service.item_service import ItemService

class OperationService:
    def __init__(self):
        self.connection = repository.create_connection()
        self.cursor = self.connection.cursor()
        self.item_service = ItemService()

    def get_operation(self, id):
        query_get_operation = "SELECT id, id_item, id_client, operation_type, operation_date FROM operations WHERE id = {}".format(id)
        self.cursor.execute(query_get_operation)
        operation = list(self.cursor.fetchone())

        return Operation(operation[0], operation[1], operation[2], operation[3], operation[4])
    
    def insert_operation(self, id_item, id_client, operation_type, operation_date):
        query_insert_operation = """INSERT INTO operations (id_item, id_client, operation_type, operation_date)
        VALUES({}, {}, '{}', '{}')""".format(id_item, id_client, operation_type, operation_date)
        self.cursor.execute(query_insert_operation)

        if operation_type.lower() == 'aluguel' or operation_type.lower() == 'reserva':
            self.item_service.update_is_available(False)
        elif operation_type.lower() == 'cancelamento' or operation_type.lower() == 'devolução':
            self.item_service.update_is_available(True)

        
        self.connection.commit()

    def update_operation(self, id, id_item, id_client, operation_type, operation_date):
        query_update = """UPDATE operations SET id_item = {}, id_client = {}, 
        operation_type = '{}', operation_date = '{}' WHERE id = {}""".format(id_item, id_client, operation_type, operation_date, id)

        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False

    def delete_operation(self, id):
        query_delete = "DELETE FROM operations WHERE id = {}".format(id)
        self.cursor.execute(query_delete)
        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False