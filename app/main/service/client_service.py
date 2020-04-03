from ..bd import repository
from ..model.models import Client

class ClientService:
    def __init__(self):
        self.connection = repository.create_connection()
        self.cursor = self.connection.cursor()

    def get_client(self, id):
        print("get client")

    def insert_client(self, name, cpf):
        print("insert client")

    def update_client(self, id, json):
        print("update client")

    def delete_client(self, id):
        print("delete client")