from ..bd import repository
from ..model.models import Client

class ClientService:
    def __init__(self):
        self.connection = repository.create_connection()
        self.cursor = self.connection.cursor()

    def get_client(self, id):
        query_get_client = "SELECT id, name, cpf FROM clients WHERE id = {}".format(id)
        self.cursor.execute(query_get_client)
        client = list(self.cursor.fetchone())
        #print(client)
        return Client(client[0], client[1], client[2])

    def insert_client(self, name, cpf):
        query_insert_client = "INSERT INTO clients (name, cpf) VALUES ('{}', '{}')".format(name, cpf)
        self.cursor.execute(query_insert_client)
        self.connection.commit()

    def update_client(self, id, name, cpf):
        query_update = "UPDATE clients SET name = '{}', cpf = '{}' WHERE id = {}".format(name, cpf, id)
        self.cursor.execute(query_update)

        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False

    def delete_client(self, id):
        query_delete = "DELETE FROM clients WHERE id = {}".format(id)
        self.cursor.execute(query_delete)
        status = self.cursor.statusmessage
        
        if '1' in status:
            self.connection.commit()
            return True
        else:
            return False